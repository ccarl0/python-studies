"""
App created by Carlo Cecchetti
I post this starting project just to say that I'm back.
This app aims to get stuff about games giveaways.
I also want to make something that runs in background that sends notifications (plyer)
"""


import requests
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
import urllib.request


i = 0
def get_games_news():
    global i, game_link, image2
    games = requests.get("https://www.gamerpower.com/api/giveaways")
    json = games.json()
    try:
        games_title_label['text'] = f"{i+1}. {json[i]['title']} \n"
        game_link = json[i]['open_giveaway_url']
        game_desc_label['text'] = f"{json[i]['description']}\n"
        #Thumbnail
        urllib.request.urlretrieve(json[i]['thumbnail'], "thumbnail.png")
        image2 = urllib.request.urlretrieve(json[i+1]['thumbnail'], "thumbnail.png")


        i += 1
    except:
        games_title_label['text'] = "GAMES' NEWS HAVE FINISHED"
        i = 0

def link(url):
    webbrowser.open_new(url)

def change_pic():
    global image2
    thumbnail_label.configure(image = image2)

"""def callback():
    global image2
    panel.configure(image=image2)
    panel.image = image2"""

#-----------------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.geometry("1200x720") #tab x,y
root.title("XMy Projects")
root.iconphoto(False, tk.PhotoImage(file="icon.png"))

frame = tk.Frame(root, bg = "#0d001a")
frame.place(relwidth=1, relheight=1)

games_title_label = tk.Label(frame, text = "", fg = "#d279a6", bg = "#0d001a", font=("Helvetica", 40), heigh = 4)
games_title_label.pack()

game_desc_label = tk.Label(frame, text = "", fg = "#993366", bg = "#0d001a", font=("Arial", 24), wraplength = 700)
game_desc_label.pack()


image = ImageTk.PhotoImage(Image.open("thumbnail.png"))
thumbnail_label = tk.Label(image=image)
thumbnail_label.pack()



get_games_button = tk.Button(frame, text = "Get Games News!!", command = lambda : [get_games_news,change_pic], heigh = 2, font=("Arial", 12), bg = "#660066", activebackground = "#4d004d")
get_games_button.pack(side = tk.BOTTOM, fill = tk.X)
game_link = ""
games_title_label.bind("<Button-1>", lambda e: link(game_link))

root.mainloop()