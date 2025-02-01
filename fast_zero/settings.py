from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Pede para o Pydantic ler esse arquivo quando a aplicação começar
    # .env, variável de ambiente, foi extraído o bd.
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URL: str
