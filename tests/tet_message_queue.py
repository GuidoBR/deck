import unittest
from message_queue import MessageQueue

class TestMessageQueue(unittest.TestCase):

    def setUp(self):
        """
        This method runs before each test case. It sets up a fresh instance of MessageQueue.
        """
        self.mq = MessageQueue()

    def test_send_message(self):
        """
        Test if the message is properly sent to the queue.
        """
        message = {"id": 1, "content": "Test message"}
        
        self.assertEqual(self.mq.queue_length(), 0)
        
        self.mq.send_message(message)
        
        self.assertEqual(self.mq.queue_length(), 1)

    def test_receive_message(self):
        """
        Test if the message is properly received from the queue.
        """
        message = {"id": 2, "content": "Test message 2"}
        
        self.mq.send_message(message)
        
        received_message = self.mq.receive_message()
        
        self.assertEqual(received_message, message)
        
        self.assertEqual(self.mq.queue_length(), 0)

    def test_queue_length(self):
        """
        Test if the queue length is updated correctly when messages are sent and received.
        """
        self.assertEqual(self.mq.queue_length(), 0)
        
        self.mq.send_message({"id": 1, "content": "Test message 1"})
        self.mq.send_message({"id": 2, "content": "Test message 2"})
        
        self.assertEqual(self.mq.queue_length(), 2)
        
        self.mq.receive_message()
        self.assertEqual(self.mq.queue_length(), 1)

        self.mq.receive_message()
        self.assertEqual(self.mq.queue_length(), 0)

    def test_receive_from_empty_queue(self):
        """
        Test receiving a message from an empty queue.
        """
        self.assertEqual(self.mq.queue_length(), 0)
        
        received_message = self.mq.receive_message()
        
        self.assertEqual(received_message, {})
