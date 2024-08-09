import unittest
from unittest.mock import MagicMock
from task_manager_sdk.tasks import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        client = MagicMock()
        self.task_manager = TaskManager(client)

    def test_create_task(self):
        self.task_manager.create_task("Test Task", "Test Description")
        self.task_manager.client.post.assert_called_once_with(
            "tasks",
            {"title": "Test Task", "description": "Test Description"}
        )

if __name__ == "__main__":
    unittest.main()
