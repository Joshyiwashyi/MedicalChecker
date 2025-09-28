from fastapi import APIRouter
from services import db_service

router = APIRouter()

@router.get("/")
def get_symptoms():
    return {"symptoms": db_service.get_all_symptoms()}
