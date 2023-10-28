from os import getenv
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    db_url: str = "sqlite+qiosqlite:/// ./db.slite3"


settings = Settings()



