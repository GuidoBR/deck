from fastapi import APIRouter
from app.services.api_client import APIClient
from app.services.business_logic import BusinessLogic
from app.services.message_queue import MessageQueue

router = APIRouter()

@router.get("/process")
def process_data():
    api_client = APIClient()
    message_queue = MessageQueue()
    business_logic = BusinessLogic(api_client, message_queue)
    
    processed_data = business_logic.fetch_and_process_data()
    return {"message": "Data processed", "data": processed_data}
