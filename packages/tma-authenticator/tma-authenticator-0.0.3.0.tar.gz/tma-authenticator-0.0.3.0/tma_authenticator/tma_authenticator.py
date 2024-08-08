import base64
import json
import hashlib
import hmac


from urllib.parse import unquote
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .users import User, UserDB
from .token import TokenResponse, Token
from .storage_provider import StorageProvider



class TMAAuthenticator:
    bot_token: str
    admin_password: str
    storage_provider: StorageProvider

    def __init__(self, bot_token: str, admin_password: str, storage_provider: StorageProvider):
        self.bot_token = bot_token
        self.admin_password = admin_password
        self.storage_provider = storage_provider

    authorization_router = APIRouter(
        prefix="/token",
        tags=["Authorization"],
        responses={404: {"description": "Not found"}},
    )

    @authorization_router.post('/',
                               summary='Create user authorization token.',
                               response_model=TokenResponse,
                               tags=["Authorization"])
    async def retrieve_access_token(self, token_data: OAuth2PasswordRequestForm = Depends()):
        return await self.create_access_token(token_data=token_data)

    async def create_access_token(self, token_data: OAuth2PasswordRequestForm) -> TokenResponse:
        if not token_data.username.isdigit():
            raise HTTPException(status_code=400, detail='username should be integer.')
        if token_data.password != self.admin_password:
            raise HTTPException(status_code=403, detail=f'Invalid credentials.')
        tg_id = int(token_data.username)

        user = await self.storage_provider.retrieve_user(search_query={'tg_id': tg_id})
        if user:
            user = UserDB(**user)
        else:
            user = UserDB(
                tg_id=tg_id,
                username=token_data.username,
                first_name='admin',
                last_name='admin',
                tg_language='en'
            )

        # TODO: This is not safe for Client Side services. This token MUST be used only for internal services.
        token = Token(first_name=user.first_name,
                      last_name=user.last_name,
                      username=user.username,
                      tg_id=user.tg_id,
                      tg_language=user.tg_language,
                      initData=token_data.password)
        token = json.dumps(token.model_dump(mode='json'))
        encoded_token = base64.b64encode(token.encode('utf-8')).decode('utf-8')
        return TokenResponse(access_token=encoded_token)

    async def oauth_verify_token(self, Authorization: str = Depends(OAuth2PasswordBearer(tokenUrl="/token/"))):
        return await self.verify_token(authorization=Authorization)

    def is_valid_user_info(self, web_app_data, bot_token: str):
        exception = HTTPException(status_code=403, detail='Invalid credentials.')

        try:
            data_check_string = unquote(web_app_data)
            data_check_arr = data_check_string.split('&')
            needle = 'hash='
            hash_item = next((item for item in data_check_arr if item.startswith(needle)), '')
            tg_hash = hash_item[len(needle):]
            data_check_arr.remove(hash_item)
            data_check_arr.sort()
            data_check_string = "\n".join(data_check_arr)
            secret_key = hmac.new("WebAppData".encode(), bot_token.encode(), hashlib.sha256).digest()
            calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

            if calculated_hash != tg_hash:
                secret_key = hmac.new("WebAppData".encode(), self.bot_token.encode(),
                                      hashlib.sha256).digest()
                calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
                if calculated_hash != tg_hash:
                    raise exception
        except Exception:
            raise exception
        return True

    def get_user_data_dict(self, unquote_user_data: str) -> dict:
        start_index_value = 'user='
        end_index_value = '&chat_instance=' if 'start_param' in unquote_user_data else '&auth_date='

        start_index = unquote_user_data.find(start_index_value) + len(start_index_value)
        end_index = unquote_user_data.find(end_index_value)
        user_data_string = unquote_user_data[start_index:end_index]
        return json.loads(user_data_string)

    def get_user_tg_language(self, user_init_data: str) -> str:
        try:
            if user_init_data == self.admin_password:
                # TODO: в этом аттрибуте может скрываться админ пароль, язык не сможем получить
                return 'admin'

            decoded_user_init_data = unquote(user_init_data)
            decoded_user_init_data = unquote(decoded_user_init_data)

            user_data_dict = self.storage_provider.get_user_data_dict(unquote_user_data=decoded_user_init_data)

            return user_data_dict['language_code']
        except Exception as err:
            return ''

    async def verify_token(self, authorization: str) -> UserDB:
        try:
            decoded_bytes = base64.b64decode(authorization)
            decoded_data = json.loads(decoded_bytes.decode('utf-8'))

            user = User(**decoded_data)
            # Admin login without user updating in the DB.
            if decoded_data['initData'] != self.admin_password:
                self.is_valid_user_info(web_app_data=decoded_data['initData'], bot_token=self.bot_token)

                user_tg_language = self.storage_provider.get_user_tg_language(user_init_data=decoded_data['initData'])

                user.tg_language = user_tg_language
                user = User(**user.model_dump())
                # TODO: extract ID from response of create_or_update_user function
                matched_count, upserted_id = await self.storage_provider.create_or_update_user(user_data=user.model_dump())
                return UserDB(id=str(upserted_id), **user.model_dump())
            else:
                db_user = await self.storage_provider.retrieve_user(search_query={'tg_id': user.tg_id})
                if db_user:
                    return UserDB(**db_user)

                matched_count, upserted_id = await self.storage_provider.create_or_update_user(user_data=user.model_dump())
                return UserDB(id=str(upserted_id), **user.model_dump())

        except Exception as err:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail=f"Could not validate credentials. {err}",
                                headers={"Authorization": "Bearer"})
