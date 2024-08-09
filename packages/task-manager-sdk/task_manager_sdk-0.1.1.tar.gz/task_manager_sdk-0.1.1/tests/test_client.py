import unittest
from task_manager_sdk.client import TaskManagerClient

class TestTaskManagerClient(unittest.TestCase):
    def setUp(self):
        self.client = TaskManagerClient(api_key="test_api_key")

    def test_get_headers(self):
        headers = self.client._get_headers()
        self.assertIn("Authorization", headers)
        self.assertIn("Content-Type", headers)

if __name__ == "__main__":
    unittest.main()
