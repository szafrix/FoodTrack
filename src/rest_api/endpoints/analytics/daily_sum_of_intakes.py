from fastapi import Depends
from pydantic import BaseModel
from datetime import date
from fastapi import Query
from src.core.use_cases.get_daily_sum_of_intakes import (
    GetDailySumOfIntakesUseCase,
    GetDailySumOfIntakesUseCaseInput,
    GetDailySumOfIntakesUseCaseOutput,
)
from src.di.container import Container
from dependency_injector.wiring import Provide
from datetime import timedelta
from pydantic import TypeAdapter
from datetime import datetime


class DailySumOfIntakesResponse(BaseModel):
    dates: list[date]
    calories: list[float]
    fats: list[float]
    carbohydrates: list[float]
    proteins: list[float]


async def get_daily_sum_of_intakes(
    start_date: date = Query(..., description="Start date"),
    end_date: date = Query(..., description="End date"),
    get_daily_sum_of_intakes_use_case: GetDailySumOfIntakesUseCase = Depends(
        Provide[Container.get_daily_sum_of_intakes_use_case]
    ),
) -> DailySumOfIntakesResponse:
    all_dates = [
        start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)
    ]
    use_case_input = GetDailySumOfIntakesUseCaseInput(dates=all_dates)
    use_case_output: GetDailySumOfIntakesUseCaseOutput = (
        get_daily_sum_of_intakes_use_case.execute(use_case_input)
    )

    return DailySumOfIntakesResponse(
        dates=[date.date() for date in use_case_output.dates],
        calories=use_case_output.kcal_daily_intakes,
        fats=use_case_output.fats_daily_intakes,
        carbohydrates=use_case_output.carbs_daily_intakes,
        proteins=use_case_output.proteins_daily_intakes,
    )
