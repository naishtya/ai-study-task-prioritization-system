class Task:
    def __init__(self, subject, deadline, difficulty):
        self.subject = subject
        self.deadline = deadline
        self.difficulty = difficulty

    def get_priority(self):
        return self.difficulty / self.deadline if self.deadline != 0 else 0

    def to_dict(self):
        return {
            "subject": self.subject,
            "deadline": self.deadline,
            "difficulty": self.difficulty
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["subject"],
            data["deadline"],
            data["difficulty"]
        )