# 🔐 GUI-Based Keyboard Event Logger (Educational)

A Python-based **GUI Keyboard Event Monitoring Application** built using **Tkinter** and **pynput**.  
This project is developed strictly for **educational purposes** to understand keyboard event handling, GUI development, multithreading, and file logging in Python.

---

## 📌 Project Description

This project implements a graphical user interface (GUI) based application that captures keyboard events such as key press, key hold, and key release. The application provides simple **Start** and **Stop** controls while ensuring the GUI remains responsive through multithreading.

The logged keyboard events are stored in both **structured (JSON)** and **human-readable (TXT)** formats, making the project useful for learning system-level programming concepts and introductory cybersecurity practices in a controlled environment.

---

## 🎯 Objectives

- To understand system-level keyboard event handling  
- To design a user-friendly GUI using Tkinter  
- To log keyboard events in structured and readable formats  
- To implement multithreading to avoid GUI freezing  
- To follow ethical software development practices  

---

## 🚀 Features

- GUI-based interface using Tkinter  
- Start and Stop logging controls  
- Logs stored in:
  - `logs.json` (structured format)
  - `logs.txt` (human-readable format)
- Multithreaded execution
- Clean and beginner-friendly Python code  

---

## 📸 Screenshots

### Logger Running State
![Logger Running](screenshots/gui_running.png)

### Logger Stopped State
![Logger Stopped](screenshots/gui_stopped.png)

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

```text
cybersecurity-internship/
|-- keylogger/
|   |-- key_logger_gui.py        # Main Python program (GUI + key logging)
|   |-- README.md                # Project documentation
|   |-- .gitignore               # Git ignore rules (excludes logs & cache)
|   `-- screenshots/
|       |-- gui_running.png      # Logger running state screenshot
|       `-- gui_stopped.png      # Logger stopped state screenshot
