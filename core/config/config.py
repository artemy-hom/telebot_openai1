from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class BotConfig(BaseSettings):
    class Config:
        env_file = ".env"

    BOT_TOKEN: str
    ACCESS_TOKEN: str


def get_config():
    load_dotenv()
    _config = BotConfig()
    return _config