import streamlit as st

from app.services.task_service import TaskService


task_service = TaskService()

st.set_page_config(
    page_title="AI Study Task Prioritization System",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Study Task Prioritization System")

st.write(
    "An intelligent productivity application "
    "for managing study tasks."
)

st.divider()

st.header("➕ Add New Task")

subject = st.text_input("Subject")

deadline = st.number_input(
    "Deadline (days)",
    min_value=1,
    step=1
)

difficulty = st.slider(
    "Difficulty",
    min_value=1,
    max_value=10
)

if st.button("Add Task"):
    if subject.strip():

        task_service.add_task(
            subject,
            int(deadline),
            int(difficulty)
        )

        st.success("✅ Task added successfully!")

    else:
        st.error("❌ Subject cannot be empty.")

st.divider()

st.header("📋 Current Tasks")

tasks = task_service.get_sorted_tasks()

if tasks:

    for task in tasks:

        priority = task.get_priority()

        if priority > 5:
            level = "🔥 High"

        elif priority > 2:
            level = "⚡ Medium"

        else:
            level = "🌱 Low"

        st.subheader(f"📘 {task.subject}")

        st.write(f"⏳ Deadline: {task.deadline} days")

        st.write(f"💪 Difficulty: {task.difficulty}")

        st.write(
            f"🔥 Priority Score: "
            f"{priority:.2f} ({level})"
        )

        st.divider()

else:
    st.info("No tasks available.")

st.header("🎯 Smart Recommendation")

recommendation = task_service.get_recommendation()

if recommendation:

    st.success(
        f"Focus on: {recommendation.subject}"
    )

    st.write(
        f"Priority Score: "
        f"{recommendation.get_priority():.2f}"
    )

else:
    st.warning("No recommendation available.")