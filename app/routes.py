import codecs
import csv
from fastapi import APIRouter, File, UploadFile

from app.repository import OrderRepository


router = APIRouter()


@router.get("/upload", tags=["file", "upload"])
async def upload(file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, "utf-8"))
    data = {}

    for rows in csvReader:
        row = rows["order_id"]
        
        OrderRepository.upload_csv_row(row)

    file.file.close()

    return data


@router.get("/orders", tags=["file", "upload"])
async def download():
    return ...
