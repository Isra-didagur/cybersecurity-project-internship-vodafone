# 🔐 GUI-Based Keyboard Event Logger (Educational)

A Python-based **GUI Keyboard Event Monitoring Application** developed using **Tkinter** and **pynput**.  
This project is intended strictly for **educational purposes** to demonstrate keyboard event handling, GUI development, multithreading, and file logging in Python.

---

## 📌 Project Description

This project implements a graphical user interface (GUI) based application that captures keyboard events such as key press, key hold, and key release. The application allows users to start and stop logging through a simple interface while ensuring system responsiveness using multithreading.

The captured keyboard events are stored in both structured and human-readable formats, making the application suitable for learning system-level programming and basic cybersecurity concepts in a controlled environment.

---

## 🎯 Objective

- To understand keyboard event handling at the system level  
- To design a user-friendly GUI using Tkinter  
- To store keyboard events in structured (JSON) and readable (TXT) formats  
- To implement multithreading to prevent GUI freezing  
- To follow ethical and educational software practices  

---

## 🚀 Features

- GUI-based interface using Tkinter  
- Start and Stop logging using buttons  
- Logs stored in:
  - `logs.json` (structured format)
  - `logs.txt` (human-readable format)
- Multithreaded execution
- Clean and beginner-friendly Python code  

---

## 📸 Screenshots

### 🔹 Logger Running State
![Key Logger Running](screenshots/gui_running.png)

### 🔹 Logger Stopped State
![Key Logger Stopped](screenshots/gui_stopped.png)

---

## 🛠 Technology Used

- Python 3  
- Tkinter  
- pynput  
- threading  
- JSON  
- Text File Handling  
- Git & GitHub  

---

## 👥 End Users

- Computer Science / Information Science students  
- Cybersecurity learners and beginners  
- Software developers exploring event-driven programming  
- Academic institutions for lab demonstrations  

---

## 📂 Project Structure

cybersecurity-internship/
├── keylogger/
│   ├── key_logger_gui.py        # Main Python program (GUI + key logging)
│   ├── README.md                # Project documentation
│   ├── .gitignore               # Git ignore rules (excludes logs & cache)
│   └── screenshots/
│       ├── gui_running.png      # Screenshot when logger is running
│       └── gui_stopped.png      # Screenshot when logger is stopped

