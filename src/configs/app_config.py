from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class AvailableImageRecognitionServices(Enum):
    DUMMY = "dummy"


class AvailableProductRepositories(Enum):
    DUMMY = "dummy"


class EnvConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class ImageRecognitionConfig(EnvConfig):
    service: AvailableImageRecognitionServices = Field(
        alias="IMAGE_RECOGNITION_SERVICE"
    )


class ProductRepositoryConfig(EnvConfig):
    service: AvailableProductRepositories = Field(alias="PRODUCT_REPOSITORY_SERVICE")


class AppConfig(EnvConfig):
    image_recognition: ImageRecognitionConfig
    product_repository: ProductRepositoryConfig


def create_app_config() -> AppConfig:
    return AppConfig(
        image_recognition=ImageRecognitionConfig(),
        product_repository=ProductRepositoryConfig(),
    )
