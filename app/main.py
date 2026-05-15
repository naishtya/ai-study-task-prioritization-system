from app.services.task_service import TaskService


class StudyAssistant:
    def __init__(self):
        self.task_service = TaskService()

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

                    self.task_service.add_task(
                        subject,
                        deadline,
                        difficulty
                    )

                    print("✅ Task added!\n")

                except ValueError:
                    print("❌ Invalid input.\n")

            elif choice == '2':
                self.display_tasks(
                    self.task_service.get_tasks()
                )

            elif choice == '3':
                task = self.task_service.get_recommendation()

                if not task:
                    print("⚠️ No tasks available.\n")

                else:
                    print("\n🎯 Top Priority Task:")
                    print(f"📘 {task.subject}")
                    print(
                        f"🔥 Priority Score: "
                        f"{task.get_priority():.2f}\n"
                    )

            elif choice == '4':
                self.display_tasks(
                    self.task_service.get_sorted_tasks()
                )

            elif choice == '5':
                self.display_tasks(
                    self.task_service.get_tasks()
                )

                try:
                    idx = int(input("Task number: ")) - 1

                    subject = input("New subject: ")

                    deadline = int(input("New deadline: "))

                    difficulty = int(
                        input("New difficulty: ")
                    )

                    updated = self.task_service.update_task(
                        idx,
                        subject,
                        deadline,
                        difficulty
                    )

                    if updated:
                        print("✅ Updated!\n")
                    else:
                        print("❌ Invalid index.\n")

                except ValueError:
                    print("❌ Invalid input.\n")

            elif choice == '6':
                self.display_tasks(
                    self.task_service.get_tasks()
                )

                try:
                    idx = int(input("Task number: ")) - 1

                    deleted = self.task_service.delete_task(idx)

                    if deleted:
                        print(f"🗑️ {deleted.subject} deleted.\n")
                    else:
                        print("❌ Invalid index.\n")

                except ValueError:
                    print("❌ Invalid input.\n")

            elif choice == '7':
                print("💾 Data saved. Bye!")
                break

            else:
                print("❌ Invalid choice.\n")