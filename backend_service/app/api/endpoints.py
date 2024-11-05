from fastapi import APIRouter
from app.services.api_client import APIClient
from app.services.business_logic import BusinessLogic

router = APIRouter()

@router.get("/process")
def process_data():
    api_client = APIClient()
    business_logic = BusinessLogic(api_client)
    
    processed_data = business_logic.process_data()
    return {"message": "Data processed", "data": processed_data}
