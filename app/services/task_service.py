from app.models.task import Task
from app.storage.json_storage import JSONStorage


class TaskService:
    def __init__(self):
        self.storage = JSONStorage()
        self.tasks = self.storage.load_tasks()

    def add_task(self, subject, deadline, difficulty):
        task = Task(subject, deadline, difficulty)
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)

    def get_tasks(self):
        return self.tasks

    def get_sorted_tasks(self):
        return sorted(
            self.tasks,
            key=lambda t: t.get_priority(),
            reverse=True
        )

    def get_recommendation(self):
        if not self.tasks:
            return None

        return max(
            self.tasks,
            key=lambda t: t.get_priority()
        )

    def update_task(self, index, subject, deadline, difficulty):
        if 0 <= index < len(self.tasks):
            self.tasks[index].subject = subject
            self.tasks[index].deadline = deadline
            self.tasks[index].difficulty = difficulty

            self.storage.save_tasks(self.tasks)
            return True

        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted = self.tasks.pop(index)
            self.storage.save_tasks(self.tasks)
            return deleted

        return None