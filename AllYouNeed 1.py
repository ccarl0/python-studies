"""
Starting to create my own app
"""
import tkinter as tk
import os

root = tk.Tk() #initialization of the GUI

"""#screen resolution in order to open a full screen tab
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
"""
screen_height = 1080
screen_width = 1920

canvas = tk.Canvas(root, height = screen_height, width = screen_width) #tellin how big to do the "page"
canvas.pack()

frame = tk.Frame(root, bg = "#333333") #changing bg color
frame.place(relwidth=1, relheight=1) #these 2 1s means the part of the canvas to color. 1 is 100%

button = tk.Button(frame, text = "Test", bg = "#990000", fg = "#008fb3")
button.pack(side = "top", fill = "x", expand = "True")
"""cpu = os.cpu_count()
print(cpu)"""

root.mainloop() #like the while loop in pygame