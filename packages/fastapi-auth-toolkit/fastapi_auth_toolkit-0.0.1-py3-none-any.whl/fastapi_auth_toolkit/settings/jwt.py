import secrets

from pydantic import BaseModel


class JWTSettings(BaseModel):
    secret_key: str = secrets.token_urlsafe(32)
    refresh_token_expire_days: int = 30
    access_token_expire_minutes: int = 30
    algorithm: str = "HS256"
    token_type: str = "bearer"

    class Config:
        extra = "ignore"  # Ignore extra fields
