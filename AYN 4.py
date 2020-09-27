"""
App created by Carlo
This will show all the information you need
"""
import tkinter as tk
import time
import os

#function to update time
def display_time():
    current_time = time.strftime("%I:%M:%S\n%d/%b/%Y") #format
    clock_label["text"] = current_time
    clock_label.after(200, display_time) #continues to recall itself

root = tk.Tk() #initialization of the GUI

root.title("AllYouNeed") #changing the title

"""#screen dimensions
screen_height = 1080
screen_width = 1920"""

frame = tk.Frame(root, bg = "#595856") #changing bg color
frame.place(relwidth=1, relheight=1) #these 2 1s means the part of the canvas to color. 1 is 100%

clock_label = tk.Label(frame, font = "verdana 15") #giving the format
clock_label.pack(anchor = "e", side = "bottom") #position
display_time() #calling the function

textBox = tk.Text(frame, height = 1, width = 20) #Place write the City
textBox.pack() #Placing in the top right corner

button = tk.Button(frame, text = "SEARCH", bg = "#D9D0C7", fg = "#05445E") #What will be the search button
button.pack() #placing in the first row second column

root.mainloop() #like the while loop in pygame