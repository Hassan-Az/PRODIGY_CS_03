import tkinter as tk
from tkinter import ttk
import string

# Calculate password strength score based on criteria
def calculate_strength(password):
    length = len(password)
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)
    
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if upper:
        score += 1
    if lower:
        score += 1
    if digit:
        score += 1
    if special:
        score += 1
    return score

# Map score to (label, color)
def get_strength_label_and_color(score):
    if score <= 2:
        return "Weak", "#e74c3c"       # Red
    elif score <= 4:
        return "Moderate", "#f1c40f"   # Yellow
    else:
        return "Strong", "#2ecc71"     # Green

def on_key_release(event=None):
    password = entry.get()
    score = calculate_strength(password)
    label, color = get_strength_label_and_color(score)
    strength_var.set(f"Strength: {label}")
    percent = int((score / 6) * 100)
    progress['value'] = percent
    progress_style.configure("Strength.Horizontal.TProgressbar", background=color)
    strength_label_widget.config(foreground=color)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("360x180")
root.resizable(False, False)
root.configure(bg="#f5f7fa")  # Light subtle background

# Main container frame with padding and background
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill='both', expand=True)

# Configure style for ttk widgets to use Helvetica font
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 11))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TFrame', background="#f5f7fa")

# Label for password entry with custom color
label = ttk.Label(main_frame, text="Enter Password:")
label.grid(row=0, column=0, sticky="w", pady=(0,6))
label.configure(foreground="#34495e")

# Password entry (visible text)
entry = ttk.Entry(main_frame, show="", width=30)
entry.grid(row=1, column=0, sticky="ew")
entry.bind('<KeyRelease>', on_key_release)

# Strength label with bold Helvetica and initial color
strength_var = tk.StringVar(value="Strength: ")
strength_label_widget = ttk.Label(main_frame, textvariable=strength_var, font=('Helvetica', 12, 'bold'))
strength_label_widget.grid(row=2, column=0, pady=12, sticky="w")
strength_label_widget.configure(foreground="#2c3e50")

# Style for progress bar
progress_style = ttk.Style()
progress_style.theme_use("clam")
progress_style.configure("Strength.Horizontal.TProgressbar",
                         thickness=18,
                         troughcolor="#dcdde1",
                         background="#e74c3c")
progress = ttk.Progressbar(main_frame,
                           length=280,
                           mode="determinate",
                           maximum=100,
                           style="Strength.Horizontal.TProgressbar")
progress.grid(row=3, column=0, pady=4)

# Set uniform column weight for resizing if needed
main_frame.columnconfigure(0, weight=1)

# Start with empty progress and label
on_key_release()

root.mainloop()
