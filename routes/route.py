from fastapi import APIRouter
from models.countries import Country
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/country")
async def get_countries():
    countries = list_serial(collection_name.find())
    return countries

@router.post("/country")
async def create_country(country: Country):
    collection_name.insert_one(dict(country))

@router.put("/country/{id()}")
async def update_country(id: str, country: Country):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(country)})

@router.delete("/country/{id()}")
async def delete_country(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
