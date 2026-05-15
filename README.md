# 🎓 AI Study Task Prioritization System

An intelligent productivity application designed to help students manage, organize, and prioritize study tasks efficiently using AI-inspired decision-making logic.

---

# 🚀 Project Overview

AI Study Task Prioritization System is a modular Python-based application that assists students in determining which academic tasks should be completed first based on urgency and difficulty.

This project was initially developed as a simple command-line prototype and has been progressively upgraded into a more professional, scalable, maintainable, and modern productivity application.

The system applies AI-inspired prioritization logic to recommend which tasks should be prioritized first.

---

# ✨ Features

## 📌 Task Management

* Add study tasks
* Update existing tasks
* Delete tasks
* Display all tasks
* Sort tasks by priority

---

## 🧠 Smart Recommendation System

The application automatically calculates task priority based on:

* task difficulty
* deadline urgency

Priority formula:

Priority Score = Difficulty / Deadline

Tasks with higher scores are considered more urgent and important.

---

## 💾 Persistent Storage

* Local JSON-based data persistence
* Automatically saves tasks
* Automatically loads previous tasks

---

## 🖥 Modern Web Interface

* Interactive Streamlit dashboard
* Clean and user-friendly UI
* Sidebar navigation
* Real-time task management

---

# 🏗 Project Architecture

```text id="lgjlwm"
ai-study-task-prioritization-system/
│
├── app/
│   ├── models/
│   │   └── task.py
│   │
│   ├── services/
│   │   └── task_service.py
│   │
│   ├── storage/
│   │   └── json_storage.py
│   │
│   ├── utils/
│   │
│   └── main.py
│
├── data/
│   └── tasks.json
│
├── streamlit_app.py
├── run.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# 🧱 Architecture Design

The project follows a modular architecture with separation of concerns:

```text id="jlwm8x"
Frontend (Streamlit UI)
        ↓
Service Layer
        ↓
Storage Layer
        ↓
JSON Database
```

---

# 🛠 Tech Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core programming language |
| Streamlit    | Web application interface |
| OOP          | Application architecture  |
| JSON         | Local data persistence    |
| Type Hints   | Better maintainability    |
| Git & GitHub | Version control           |

---

# ▶️ Installation & Setup

## 1. Clone Repository

```bash id="jlwmq8"
git clone <https://github.com/naishtya/ai-study-task-prioritization-system>
```

---

## 2. Move into Project Directory

```bash id="2jlwmq"
cd ai-study-task-prioritization-system
```

---

## 3. Create Virtual Environment

### Windows

```bash id="jlwm94"
python -m venv .venv
```

---

## 4. Activate Virtual Environment

### Windows (PowerShell)

```bash id="jlwm4p"
.venv\Scripts\Activate.ps1
```

---

## 5. Install Dependencies

```bash id="jlwm07"
pip install -r requirements.txt
```

---

# 🚀 Run Application

## Run Streamlit Dashboard

```bash id="jlwmr7"
streamlit run streamlit_app.py
```

---

# 📸 Example Features

* 📋 Smart task dashboard
* 🎯 AI-inspired task recommendation
* 📊 Priority-based task organization
* 💾 Automatic task persistence

---

# 🎯 Current Development Status

✅ Modular architecture
✅ Streamlit web dashboard
✅ Service-based structure
✅ JSON persistence
✅ Type hints
✅ Environment configuration
✅ GitHub-ready project structure

---

# 🚀 Future Improvements

Planned upgrades for future development:

* SQLite / PostgreSQL database
* REST API using FastAPI
* Authentication system
* Advanced analytics dashboard
* AI-based recommendation engine
* Machine learning prioritization
* Notification & reminder system
* Docker support
* CI/CD automation
* Cloud deployment

---

# 📚 Learning Objectives

This project demonstrates:

* Clean code practices
* Modular Python architecture
* Object-oriented programming
* Software engineering fundamentals
* AI-inspired decision systems
* Refactoring techniques
* Maintainable code structure
* Basic productivity system design

---

# 👩‍💻 Author

**Naima Sahitya Andini**
Artificial Intelligence Student — IPB University

---

# ⭐ Project Status

🚧 Currently under active development and modernization.
