from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST : str
    DB_PORT : str
    DB_USER : str
    DB_PASS : str
    DB_NAME : str

    @property
    def DATABASE_URL(self):
        """
        Возвращает готовую строку подключения к базе данных PostgreSQL
        """
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    SECRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file=".env")
    #откуда импортитруем переменные это вариант со старой версии Pydantic, class Config был заменен на атрибут model_config
    # class Config:
    #     env_file = ".env"

settings = Settings()
# print(settings.DATABASE_URL)