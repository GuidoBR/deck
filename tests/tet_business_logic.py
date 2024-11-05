from unittest.mock import MagicMock
from app.services.business_logic import BusinessLogic

def test_business_logic_process_data():
    # Arrange
    mock_api_client = MagicMock()
    mock_message_queue = MagicMock()
    mock_api_client.fetch_data.return_value = {"id": 1, "name": "Sample Data", "value": 100}
    business_logic = BusinessLogic(api_client=mock_api_client, message_queue=mock_message_queue, num_workers=1)

    # Act
    business_logic.fetch_and_process_data()

    # Assert
    mock_api_client.fetch_data.assert_called_once()
    mock_message_queue.send_message.assert_called_once()
    expected_processed_data = {
        "transformed_data": '{"id": 1, "name": "Sample Data", "value": 100}',
        "status": "processed"
    }
    mock_message_queue.send_message.assert_called_with(expected_processed_data)
