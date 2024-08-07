from pydantic import Field
from pydantic_settings import BaseSettings

from fastapi_auth_toolkit.settings import JWTSettings


class Settings(BaseSettings):
    # jwt configuration and credentials settings
    jwt: JWTSettings = Field(default_factory=JWTSettings)


settings = Settings()
