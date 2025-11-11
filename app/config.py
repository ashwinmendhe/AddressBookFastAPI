from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    app_name: str = "Address Book API"
    database_url: str = "sqlite:///./addresses.db"

settings = Settings()