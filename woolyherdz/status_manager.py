class StatusManager:
    def __init__(self):
        self.statuses = {}  # Task ID to status mapping

    def update_status(self, task_id, status):
        self.statuses[task_id] = status

    def get_status(self, task_id):
        return self.statuses.get(task_id, "Unknown Task")
