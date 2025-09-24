import tkinter as tk
from tkinter import ttk, messagebox
import threading
from exercises import run_exercise

# --- GUI Setup ---
root = tk.Tk()
root.title("FitMentor - Exercise Trainer")
root.geometry("400x400")
root.configure(bg="#f0f4f8")
root.resizable(True, True)

# Center the window
def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')

center_window(root)

# Modern button style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton",
                font=("Segoe UI", 12, "bold"),
                foreground="white",
                background="#4CAF50",
                padding=10)
style.map("TButton",
          background=[('active', '#45a049')])

# Label
title_label = ttk.Label(root, text="Choose Your Exercise", font=("Segoe UI", 16, "bold"), background="#f0f4f8")
title_label.pack(pady=20)

# Loading label
loading_label = ttk.Label(root, text="", font=("Segoe UI", 10), background="#f0f4f8", foreground="gray")
loading_label.pack(pady=10)

# Function to run exercise in a separate thread
def start_exercise(exercise_name):
    loading_label.config(text="Loading webcam...")
    threading.Thread(target=launch_exercise, args=(exercise_name,), daemon=True).start()

def launch_exercise(name):
    try:
        run_exercise(name)
    finally:
        loading_label.config(text="")

# Button list
exercises = ["Squats", "Biceps", "Lunges", "Shoulders", "Jumping Jacks"]

for ex in exercises:
    ttk.Button(root, text=ex, command=lambda e=ex: start_exercise(e)).pack(pady=8, ipadx=10, fill="x", padx=40)

# Exit Button
ttk.Button(root, text="Exit", command=root.quit).pack(pady=20, ipadx=10)

root.mainloop()
