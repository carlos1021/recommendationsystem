import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def update_progress_label():
    return f"Current Progress: {progress_bar['value']}%"

def progress():
    if progress_bar['value'] < 100:
        progress_bar['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')

# Creating the window object
window = tk.Tk()
window.title("Recommendation System Desktop App")
window.geometry("600x400")
window.configure(bg="#f0f0f0")

# Creating a frame for content
content_frame = tk.Frame(window, bg="#f0f0f0")
content_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Creating a label with enhanced styling
new_Label = tk.Label(
    content_frame,
    text="Visit the Recommendation System Desktop App to find synonyms for your favorite Pokemon.",
    font=("Arial", 14),
    wraplength=500,
    padx=20,
    pady=20,
    bg="#f0f0f0",
)
new_Label.pack(fill=tk.BOTH, expand=True)

# Create a progress bar widget
progress_bar = ttk.Progressbar(
    content_frame, orient="horizontal", length=300, maximum=100, mode="determinate"
)
progress_bar.pack(pady=10)

value_label = ttk.Label(
    content_frame,
    text=update_progress_label(),
    font=("Arial", 12),
    bg="#f0f0f0",
)
value_label.pack()

# Create a frame for buttons
button_frame = tk.Frame(content_frame, bg="#f0f0f0")
button_frame.pack(pady=20)

# Create start button with enhanced styling
start_button = ttk.Button(
    button_frame,
    text="START",
    command=progress,
    style="Custom.TButton",
)
start_button.pack(side=tk.LEFT, padx=10)

# Create stop button with enhanced styling
stop_button = ttk.Button(
    button_frame,
    text="STOP",
    command=progress_bar.stop,
    style="Custom.TButton",
)
stop_button.pack(side=tk.LEFT, padx=10)

# Create custom style for buttons
style = ttk.Style()
style.configure(
    "Custom.TButton",
    font=("Arial", 12),
    padding=10,
    relief="flat",
    foreground="#ffffff",
    background="#007acc",
)
style.map(
    "Custom.TButton",
    background=[("active", "#005a8e")],
    foreground=[("active", "#ffffff")],
)

window.mainloop()
