import base64
from fastapi import Depends, UploadFile, File, Form
from pydantic import BaseModel
from src.core.entities.product import Product
from src.core.use_cases.read_nutriments_from_photo import (
    ReadNutrimentsFromPhotoUseCase,
    ReadNutrimentsFromPhotoUseCaseInput,
)
from src.core.use_cases.register_product_in_repository import (
    RegisterProductInRepositoryUseCase,
    RegisterProductInRepositoryUseCaseInput,
)
from src.di.container import Container
from dependency_injector.wiring import Provide

# TODO: decouple the two endpoints


class RegisterProductImageInputRequest(BaseModel):
    name: str
    image: UploadFile


class RegisterProductImageInputResponse(BaseModel):
    product: Product


async def register_product_image_input(
    name: str = Form(...),
    image: UploadFile = File(...),
    read_nutriments_from_photo_use_case: ReadNutrimentsFromPhotoUseCase = Depends(
        Provide[Container.read_nutriments_from_photo_use_case]
    ),
) -> RegisterProductImageInputResponse:
    request = RegisterProductImageInputRequest(name=name, image=image)
    image_content = await request.image.read()
    base64_image = base64.b64encode(image_content).decode("utf-8")
    read_image_use_case_input = ReadNutrimentsFromPhotoUseCaseInput(
        name=request.name,
        photo=base64_image,
    )
    read_image_use_case_output = read_nutriments_from_photo_use_case.execute(
        read_image_use_case_input
    )
    return RegisterProductImageInputResponse(
        product=read_image_use_case_output.product,
    )


async def confirm_product_image_input(
    product: Product,
    register_product_use_case: RegisterProductInRepositoryUseCase = Depends(
        Provide[Container.register_product_in_repository_use_case]
    ),
) -> RegisterProductImageInputResponse:
    register_product_use_case_input = RegisterProductInRepositoryUseCaseInput(
        product=product,
    )
    register_product_use_case_output = register_product_use_case.execute(
        register_product_use_case_input
    )
    return RegisterProductImageInputResponse(
        product=register_product_use_case_output.product,
    )
