from typing import Self

from flask import Flask, jsonify, request
from pydantic import BaseModel, Field

from src.core.interactors.register_product import (
    RegisterProductInteractor,
    RegisterProductInteractorInput,
    RegisterProductInteractorOutput,
)
from dependency_injector.wiring import inject, Provide
from di.container import Container


class RegisterProductManualInputRequest(BaseModel):
    name: str = Field(..., description="The name of the product")
    kcal_100g: float = Field(..., description="The kcal value per 100g")
    proteins_100g: float = Field(..., description="The proteins value per 100g")
    carbs_100g: float = Field(..., description="The carbs value per 100g")
    fats_100g: float = Field(..., description="The fats value per 100g")


class RegisterProductManualInputResponse(BaseModel):
    success: bool
    error: str | None


class RegisterProductImageInputRequest(BaseModel):
    name: str = Field(..., description="The name of the product")
    nutrients_image: str = Field(..., description="The image of the product")


class RegisterProductImageInputResponse(BaseModel):
    success: bool
    error: str | None


@inject
def create_app(
    register_product_Interactor: RegisterProductInteractor = Provide(
        Container.register_product_Interactor
    ),
):
    app = Flask(__name__)

    @app.route("/register_product_manual_input/try_to_fetch", methods=["POST"])
    def register_product_manual_input_try_to_fetch():
        input_ = RegisterProductManualInputRequest(**request.json)
        register_product_input = RegisterProductInteractorInput(
            name=input_.name,
            kcal_100g=input_.kcal_100g,
            proteins_100g=input_.proteins_100g,
            carbs_100g=input_.carbs_100g,
            fats_100g=input_.fats_100g,
            try_to_fetch_product=True,
            nutrients_image=None,
        )
        register_product_output = register_product_Interactor.execute(
            register_product_input
        )
        return RegisterProductManualInputResponse(
            success=register_product_output.success,
            error=register_product_output.error,
        ).model_dump()

    @app.route("/register_product_image_input/try_to_fetch", methods=["POST"])
    def register_product_image_input_try_to_fetch():
        input_ = RegisterProductImageInputRequest(**request.json)
        register_product_input = RegisterProductInteractorInput(
            name=input_.name,
            nutrients_image=input_.nutrients_image,
            try_to_fetch_product=True,
        )
        register_product_output = register_product_Interactor.execute(
            register_product_input
        )
        return RegisterProductImageInputResponse(
            success=register_product_output.success,
            error=register_product_output.error,
        ).model_dump()

    @app.route("/register_product_manual_input/do_not_fetch", methods=["POST"])
    def register_product_manual_input_do_not_fetch():

        input_ = RegisterProductManualInputRequest(**request.json)
        register_product_input = RegisterProductInteractorInput(
            name=input_.name,
            kcal_100g=input_.kcal_100g,
            proteins_100g=input_.proteins_100g,
            carbs_100g=input_.carbs_100g,
            fats_100g=input_.fats_100g,
            try_to_fetch_product=False,
        )
        register_product_output = register_product_Interactor.execute(
            register_product_input
        )
        return RegisterProductManualInputResponse(
            success=register_product_output.success,
            error=register_product_output.error,
        ).model_dump()

    @app.route("/register_product_image_input/do_not_fetch", methods=["POST"])
    def register_product_image_input_do_not_fetch():
        input_ = RegisterProductImageInputRequest(**request.json)
        register_product_input = RegisterProductInteractorInput(
            name=input_.name,
            nutrients_image=input_.nutrients_image,
            try_to_fetch_product=False,
        )
        register_product_output = register_product_Interactor.execute(
            register_product_input
        )
        return RegisterProductImageInputResponse(
            success=register_product_output.success,
            error=register_product_output.error,
        ).model_dump()

    return app
