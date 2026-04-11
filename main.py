import json

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
        return Task(data["subject"], data["deadline"], data["difficulty"])


class Student:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def get_recommendation(self):
        if not self.tasks:
            return None
        return max(self.tasks, key=lambda t: t.get_priority())

    def get_sorted_tasks(self):
        return sorted(self.tasks, key=lambda t: t.get_priority(), reverse=True)

    def update_task(self, index, subject, deadline, difficulty):
        if 0 <= index < len(self.tasks):
            self.tasks[index].subject = subject
            self.tasks[index].deadline = deadline
            self.tasks[index].difficulty = difficulty
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        return None

    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f)

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []


class StudyAssistant:
    def __init__(self):
        self.student = Student()
        self.student.load_from_file()

    def display_tasks(self, tasks):
        if not tasks:
            print("⚠️ No tasks available.\n")
            return

        for i, task in enumerate(tasks, start=1):
            priority = task.get_priority()

            if priority > 5:
                level = "🔥 High"
            elif priority > 2:
                level = "⚡ Medium"
            else:
                level = "🌱 Low"

            print(f"{i}. 📘 {task.subject}")
            print(f"   ⏳ Deadline: {task.deadline} days")
            print(f"   💪 Difficulty: {task.difficulty}")
            print(f"   🔥 Priority: {priority:.2f} ({level})\n")

    def run(self):
        while True:
            print("\nSMART STUDY ASSISTANT")
            print("1. Add Task")
            print("2. Show Tasks")
            print("3. Get Recommendation")
            print("4. Show Sorted Tasks")
            print("5. Update Task")
            print("6. Delete Task")
            print("7. Exit")

            choice = input("Choose (1-7): ")

            if choice == '1':
                subject = input("Subject: ")
                try:
                    deadline = int(input("Deadline (days): "))
                    difficulty = int(input("Difficulty (1-10): "))

                    if deadline <= 0 or not (1 <= difficulty <= 10):
                        print("❌ Invalid values.\n")
                        continue

                    self.student.add_task(Task(subject, deadline, difficulty))
                    self.student.save_to_file()
                    print("✅ Task added!\n")

                except ValueError:
                    print("❌ Invalid input.\n")

            elif choice == '2':
                self.display_tasks(self.student.get_tasks())

            elif choice == '3':
                task = self.student.get_recommendation()
                if not task:
                    print("⚠️ No tasks available.\n")
                else:
                    print("\n🎯 Top Priority Task:")
                    print(f"📘 {task.subject}")
                    print(f"🔥 Priority Score: {task.get_priority():.2f}\n")

            elif choice == '4':
                self.display_tasks(self.student.get_sorted_tasks())

            elif choice == '5':
                self.display_tasks(self.student.get_tasks())
                try:
                    idx = int(input("Task number: ")) - 1
                    subject = input("New subject: ")
                    deadline = int(input("New deadline: "))
                    difficulty = int(input("New difficulty: "))

                    if deadline <= 0 or not (1 <= difficulty <= 10):
                        print("❌ Invalid values.\n")
                        continue

                    if self.student.update_task(idx, subject, deadline, difficulty):
                        self.student.save_to_file()
                        print("✅ Updated!\n")
                    else:
                        print("❌ Invalid index.\n")

                except ValueError:
                    print("❌ Invalid input.\n")

            elif choice == '6':
                self.display_tasks(self.student.get_tasks())
                try:
                    idx = int(input("Task number: ")) - 1
                    deleted = self.student.delete_task(idx)

                    if deleted:
                        self.student.save_to_file()
                        print(f"🗑️ {deleted.subject} deleted.\n")
                    else:
                        print("❌ Invalid index.\n")

                except ValueError:
                    print("❌ Invalid input.\n")

            elif choice == '7':
                self.student.save_to_file()
                print("💾 Data saved. Bye!")
                break

            else:
                print("❌ Invalid choice.\n")


if __name__ == "__main__":
    app = StudyAssistant()
    app.run()