from fastapi import FastAPI
from .routes import product, intake

app = FastAPI()

app.include_router(product.router)
app.include_router(intake.router)
