from __future__ import annotations
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    
    # Fast API variable details
    app_name: str = Field(default=os.getenv("APP_NAME"), alias="APP_NAME") 
    app_env: str = Field(default=os.getenv("APP_ENV"), alias="APP_ENV")
    app_host: str = Field(default=os.getenv("APP_HOST"), alias="APP_HOST")
    app_port: str = Field(default=os.getenv("APP_PORT"), alias="APP_PORT")

    # Azure OpenAI Details
    azure_openai_api_key: str = ""
    azure_openai_endpoint: str = ""
    azure_openai_deployment: str = ""

    # Ollama details
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL")

    # Postgres details
    postgres_host: str = Field(default=os.getenv("POSTGRES_HOST"), alias="POSTGRES_HOST")
    postgres_port: int = Field(default=os.getenv("POSTGRES_PORT"), alias="POSTGRES_PORT")
    postgres_db: str = Field(default=os.getenv("POSTGRES_DB"), alias="POSTGRES_DB")
    postgres_user: str = Field(default=os.getenv("POSTGRES_USER"), alias="POSTGRES_USER")
    postgres_password: str = Field(default=os.getenv("POSTGRES_PASSWORD"), alias="POSTGRES_PASSWORD")

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