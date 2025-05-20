from pydantic_settings import BaseSettings


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

    #откуда импортитруем переменные
    class Config:
        env_file = ".env"

settings = Settings()
# print(settings.DATABASE_URL)