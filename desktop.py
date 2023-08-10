import tkinter as tk

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