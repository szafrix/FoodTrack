from enum import Enum
from typing import Self
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, model_validator, field_validator


class ProductRepositories(Enum):
    DUMMY = "dummy"
    SQLITE = "sqlite"


class IntakeRepositories(Enum):
    DUMMY = "dummy"
    SQLITE = "sqlite"


class ImageRecognitionServices(Enum):
    DUMMY = "dummy"
    OPENAI = "openai"


class EnvConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class ProductRepositoryConfig(EnvConfig):
    name: ProductRepositories = Field(alias="PRODUCT_REPOSITORY_SERVICE")


class IntakeRepositoryConfig(EnvConfig):
    name: IntakeRepositories = Field(alias="INTAKE_REPOSITORY_SERVICE")


class ImageRecognitionConfig(EnvConfig):
    name: ImageRecognitionServices = Field(alias="IMAGE_RECOGNITION_SERVICE")


class RestApiConfig(EnvConfig):
    host: str = Field(alias="REST_API_HOST")
    port: int = Field(alias="REST_API_PORT")


class NgrokConfig(EnvConfig):
    use_ngrok: bool = Field(alias="USE_NGROK")
    auth_token: str | None = Field(alias="NGROK_AUTH_TOKEN", default=None)
    allowed_emails: list[str] | None = Field(
        alias="ALLOWED_EMAILS",
        default=None,
        description="Comma-separated list of allowed emails",
    )

    @model_validator(mode="after")
    def check_auth_token(self) -> Self:
        if self.use_ngrok and self.auth_token is None:
            raise ValueError("NGROK_AUTH_TOKEN must be provided if USE_NGROK is true")
        return self

    @field_validator("allowed_emails", mode="before")
    def parse_allowed_emails(cls, value):
        if isinstance(value, str):
            return [email.strip() for email in value.split(",") if email.strip()]
        return value


class AppConfig(EnvConfig):
    product_repository: ProductRepositoryConfig = ProductRepositoryConfig()
    intake_repository: IntakeRepositoryConfig = IntakeRepositoryConfig()
    image_recognition: ImageRecognitionConfig = ImageRecognitionConfig()
    rest_api: RestApiConfig = RestApiConfig()
    ngrok: NgrokConfig = NgrokConfig()
