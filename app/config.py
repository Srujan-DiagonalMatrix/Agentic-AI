from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    
    # Fast API variable details
    app_name: str = os.getenv("APP_NAME")
    app_env: str = os.getenv("APP_ENV")
    app_host: str = os.getenv("APP_HOST")
    app_port: str = os.getenv("APP_PORT")

    # Azure OpenAI Details
    azure_openai_api_key: str = ""
    azure_openai_endpoint: str = ""
    azure_openai_deployment: str = ""

    # Ollama details
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL")

    # Postgres details
    postgres_host: str = os.getenv("POSTGRES_HOST")
    postgres_port: int = os.getenv("POSTGRES_PORT")
    postgres_db: str = os.getenv("POSTGRES_DB")
    postgres_user: str = os.getenv("POSTGRES_USER")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD")

    model_config = SettingsConfigDict(env_file=".env",
                       env_file_encoding="utf-8",
                       case_sensitive=False,
                       extra="ignore"
                       )
    
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

settings = Settings()

# if __name__ == "__main__":
#     print(settings.database_url)