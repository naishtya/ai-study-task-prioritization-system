import json
from app.models.task import Task


class JSONStorage:
    def __init__(self, filename="data/tasks.json"):
        self.filename = filename

    def save_tasks(self, tasks):
        with open(self.filename, "w") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Task.from_dict(d) for d in data]

        except (FileNotFoundError, json.JSONDecodeError):
            return []