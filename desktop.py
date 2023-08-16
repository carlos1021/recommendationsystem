import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import time

#Creating the window object
window = tk.Tk()

#Giving the window a title
window.title("Recommendation System Desktop App")
#Setting the window size
window.geometry("600x400")
#Creating a label object
new_Label = tk.Label(window, text = "Vist the Recommendation System Desktop App to find synonyms for your favorite Pokemon.")

#Place the label onto the window
new_Label.grid(column= 0, row = 0)

#Create a progress bar widget
progress_bar = ttk.Progressbar(window, orient = "horizontal", length=300, maximum = 100, mode="determinate")
#Place the progress bar widget onto the window
progress_bar.grid(column = 0, row = 5)

def update_progress_label():
    return f"Current Progress: {progress_bar['value']}%"

value_label = ttk.Label(window, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)


def progress():
    if progress_bar['value'] < 100:
        progress_bar['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')




#Create start button
start_button = ttk.Button(window, text = "START", command = progress)
#Place the start button onto the window
start_button.grid(column = 0, row = 8, padx = 10, pady = 10)
#Create start button
stop_button = ttk.Button(window, text = "STOP", command = progress_bar.stop)
#Place the start button onto the window
stop_button.grid(column = 2, row = 8, padx = 10, pady = 10)


window.mainloop()








# class Pokemon:
#     def __init__(self):
#         self.name = ""
#         self.weight = 10
#         self.type = "Water"

# pikachu = Pokemon()
# print(pikachu.type)
# pikachu.type = "Electric"
# print(pikachu.type)