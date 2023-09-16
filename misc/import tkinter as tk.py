import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import time

def update_progress_label(progress_value):
    return f"Current Progress: {progress_value}%"

def progress():
    if progress_bar['value'] < 100:
        progress_bar['value'] += 20
        value_label['text'] = update_progress_label(progress_bar['value'])
    else:
        showinfo(message='The progress completed!')

def create_fancy_button(parent, text, command):
    button = ttk.Button(parent, text=text, command=command, style="Fancy.TButton")
    return button

# Creating the window object
window = tk.Tk()

window.configure(bg="light blue")

# Giving the window a title
window.title("Recommendation System Desktop App")

# Setting the window size
window.geometry("600x400")

# Creating a label object with improved text formatting
new_Label = tk.Label(
    window,
    text="Visit the Recommendation System Desktop App to find synonyms for your favorite Pokemon.",
    font=("Arial", 14),
    padx=20,
    pady=20
)
new_Label.grid(column=0, row=0, columnspan=3)

# Create a progress bar widget
progress_bar = ttk.Progressbar(window, orient="horizontal", length=300, maximum=100, mode="determinate")
progress_bar.grid(column=0, row=5, columnspan=3, padx=20, pady=10)

# Create a label to display progress percentage
value_label = ttk.Label(window, text=update_progress_label(progress_bar['value']), font=("Comic Sans", 12))
value_label.grid(column=0, row=1, columnspan=3, padx=20, pady=10)

# Style for the fancy button
style = ttk.Style()
style.configure("Fancy.TButton", font=("Comic Sans", 12))

# Create start button with improved formatting
start_button = create_fancy_button(window, "START", progress)
start_button.grid(column=0, row=8, padx=10, pady=10)

# Create stop button with improved formatting
stop_button = create_fancy_button(window, "STOP", progress_bar.stop)
stop_button.grid(column=2, row=8, padx=10, pady=10)

window.mainloop()
