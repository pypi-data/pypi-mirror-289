class TaskManager:
    def __init__(self, client):
        self.client = client

    def create_task(self, title, description):
        data = {
            "title": title,
            "description": description,
        }
        return self.client.post("tasks", data)

    def get_task(self, task_id):
        return self.client.get(f"tasks/{task_id}")

    def update_task(self, task_id, title=None, description=None):
        data = {
            "title": title,
            "description": description,
        }
        return self.client.put(f"tasks/{task_id}", data)

    def delete_task(self, task_id):
        return self.client.delete(f"tasks/{task_id}")
