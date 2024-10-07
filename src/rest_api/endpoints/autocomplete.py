from fastapi import Depends, Query
from pydantic import BaseModel
from src.core.entities.product import Product

from src.core.use_cases.fetch_products_for_autocompletion import (
    FetchProductsForAutocompletionUseCase,
    FetchProductsForAutocompletionUseCaseInput,
)
from src.di.container import Container
from dependency_injector.wiring import Provide


class AutocompleteProductResponse(BaseModel):
    products: list[Product]


async def autocomplete_product(
    user_input: str = Query(..., description="User input for autocomplete"),
    autocomplete_product_use_case: FetchProductsForAutocompletionUseCase = Depends(
        Provide[Container.fetch_products_for_autocompletion_use_case]
    ),
) -> AutocompleteProductResponse:
    use_case_input = FetchProductsForAutocompletionUseCaseInput(
        user_input=user_input,
    )
    use_case_output = autocomplete_product_use_case.fetch_products_for_autocompletion(
        use_case_input
    )
    print(use_case_output)
    return AutocompleteProductResponse(
        products=use_case_output.products,
    )
