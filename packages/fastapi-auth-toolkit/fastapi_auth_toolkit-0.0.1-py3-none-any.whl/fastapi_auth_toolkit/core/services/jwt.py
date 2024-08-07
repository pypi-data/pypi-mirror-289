from datetime import datetime, timedelta

from bson import ObjectId
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

import jwt
from fastapi_auth_toolkit.config import settings

JWT_SECRET_KEY = settings.jwt.secret_key
JWT_ALGORITHM = settings.jwt.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.jwt.access_token_expire_minutes
REFRESH_TOKEN_EXPIRE_DAYS = settings.jwt.refresh_token_expire_days  # Add this in your settings


class JWTServices(HTTPBearer):
    def __init__(self):
        super().__init__()

    @staticmethod
    async def create_access_token(user_id: str) -> str:
        expire_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        data_payload = {
            "user_id": str(user_id),
            "type_token": "access",
            "exp": expire_time
        }
        return jwt.encode(data_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    @staticmethod
    async def create_refresh_token(user_id: ObjectId) -> str:
        expire_time = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        data_payload = {
            "user_id": str(user_id),
            "type_token": "refresh",
            "exp": expire_time
        }
        return jwt.encode(data_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    @staticmethod
    async def decode_token(token: str) -> dict:
        try:
            return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )

    @staticmethod
    async def verify_token(credentials: HTTPAuthorizationCredentials, credentials_exception: HTTPException) -> str:
        try:
            payload = jwt.decode(credentials.credentials, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            user_id = payload.get("sub")
            if user_id is None:
                raise credentials_exception
            return user_id
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            raise credentials_exception
