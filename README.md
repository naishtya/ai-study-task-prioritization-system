# 🎓 AI-Based Study Task Prioritization System

An intelligent command-line application that helps students manage and prioritize study tasks using a rule-based decision-making approach.

---

## 🚀 Overview

This project is designed to improve student productivity by identifying which tasks should be prioritized based on urgency and difficulty.

By applying a simple yet effective priority scoring system, the application simulates basic AI behavior to assist decision-making in study planning.

---

## ✨ Key Features

* 📌 Add, update, and delete study tasks
* 📊 Automatic priority calculation
* 🎯 Smart task recommendation (highest priority)
* 📈 Sort tasks based on urgency
* 💾 Persistent storage using JSON
* 🧠 Object-Oriented Programming (OOP) design

---

## 🧠 How It Works

Each task consists of:

* **Subject**
* **Deadline (in days)**
* **Difficulty (scale 1–10)**

The system calculates priority using:

```
priority = difficulty / deadline
```

Tasks with higher scores are considered more urgent.

---

## 🔄 System Flow

User Input → Task Stored → Priority Calculated → Recommendation Generated → Task Updated/Deleted

---

## 🛠 Tech Stack

* **Python**
* **Object-Oriented Programming (OOP)**
* **JSON (for data persistence)**

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📸 Example Output

```
🎯 Top Priority Task:
📘 Math
🔥 Priority Score: 2.50
```

---

## 📁 Project Structure

```
smart-study-assistant/
│
├── main.py
├── README.md
└── .gitignore
```

---

## 📌 Future Improvements

* 🖥 GUI version (Tkinter)
* 🌐 Web-based version (Streamlit / Flask)
* 🤖 Advanced AI-based recommendations
* ⏰ Task reminders and notifications

---

## ✨ Author

**Naima Sahitya**
Artificial Intelligence Student — IPB University

---

## ⭐ Final Note

This project demonstrates fundamental concepts in software development, including structured programming, algorithmic thinking, and object-oriented design, while applying a simple AI-inspired approach to real-world productivity problems.
