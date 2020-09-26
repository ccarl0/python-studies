"""
App created by Carlo
This will show all the information you need
"""
import tkinter as tk
from datetime import datetime
import os

root = tk.Tk() #initialization of the GUI

screen_height = 1080
screen_width = 1920

frame = tk.Frame(root, bg = "#08395E") #changing bg color
frame.place(relwidth=1, relheight=1) #these 2 1s means the part of the canvas to color. 1 is 100%
#getting time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string) #debug

time_label = tk.Label(frame, text = dt_string) #label to write time (must be update because it doesn't update
time_label.grid(row = 0, column = 5)

textBox = tk.Text(frame, height = 1, width = 20) #Place write the City
textBox.grid(row = 0, column = 0) #Placing in the top right corner

button = tk.Button(frame, text = "Search", bg = "#3574D4", fg = "#05445E") #What will be the search button
button.grid(row = 0, column = 1) #placing in the first row second column

root.mainloop() #like the while loop in pygame