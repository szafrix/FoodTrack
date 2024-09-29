from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

app = FastAPI()

class ProductNameIntakeRequest(BaseModel):
    product_name: str
    # Add other fields like quantity, date, etc.


class BarcodeIntakeRequest(BaseModel):
    # Add other fields like quantity, date, etc.
    pass


@app.post("/intake/by-name")
async def register_intake_by_name(intake: ProductNameIntakeRequest):
    # Logic to handle intake by product name
    return {"message": "Intake registered by product name"}


@app.post("/intake/by-barcode")
async def register_intake_by_barcode(barcode_image: UploadFile = File(...), intake: BarcodeIntakeRequest = None):
    # Logic to handle intake by barcode image
    return {"message": "Intake registered by barcode"}