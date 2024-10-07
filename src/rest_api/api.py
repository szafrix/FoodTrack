from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from rest_api.endpoints.intake.register import (
    register_intake,
    RegisterIntakeResponse,
)
from rest_api.endpoints.product.register_product_manual import (
    register_product_manual_input,
    RegisterProductManualInputResponse,
)
from rest_api.endpoints.product.register_product_image import (
    register_product_image_input,
    confirm_product_image_input,
    RegisterProductImageInputResponse,
)
from rest_api.endpoints.autocomplete import (
    autocomplete_product,
    AutocompleteProductResponse,
)


def create_app(origins: list[str]) -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

    app.mount("/static", StaticFiles(directory="src/frontend"), name="static")

    @app.get("/")
    async def read_index():
        return FileResponse("src/frontend/index.html")

    @app.get("/favicon.ico", include_in_schema=False)
    async def favicon():
        return FileResponse("src/frontend/favicon.ico")

    app.post("/intake/register", response_model=RegisterIntakeResponse)(register_intake)
    app.post(
        "/product/register-manual-input",
        response_model=RegisterProductManualInputResponse,
    )(register_product_manual_input)
    app.post(
        "/product/register-image-input",
        response_model=RegisterProductImageInputResponse,
    )(register_product_image_input)
    app.post(
        "/product/register-confirm-image-input",
        response_model=RegisterProductImageInputResponse,
    )(confirm_product_image_input)
    app.get("/autocomplete", response_model=AutocompleteProductResponse)(
        autocomplete_product
    )
    return app
