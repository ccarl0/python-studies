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

games = requests.get("https://www.gamerpower.com/api/giveaways")
json = games.json()
titles_list = []
for dict in json:
    titles_list.append(json[len(titles_list)].get('title'))

i = 0
def next_page():
    global i
    i += 1
    get_games_news(i)

def previous_page():
    global i
    i -= 1
    get_games_news(i)

def get_games_news(i):
    global game_link, json

    #Game's title
    games_title_label['text'] = f"{titles_list.index(json[i-1]['title'])+1}. {json[i-1]['title']} \n"
    #Getting game link
    game_link = json[i]['open_giveaway_url']
    #Getting game description
    game_desc_label['text'] = f"{json[i-1]['description']}\n"
    #Thumbnail
    urllib.request.urlretrieve(json[i-1]['thumbnail'],"thumbnail.png")
    print(json[i-1]['thumbnail'])

def link(url):
    webbrowser.open_new(url)

#-----------------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.geometry("1600x800") #tab x,y
root.title("XMy Projects")
root.iconphoto(False, tk.PhotoImage(file="icon.png"))

frame = tk.Frame(root, bg = "#0d001a")
frame.place(relwidth=1, relheight=1)
#Page Buttons
previous_page_button_side = tk.Button(frame, text = "Previous Page", command = lambda : previous_page(), heigh = 12, width = 11, font=("Arial", 12), bg = "#ffb3ff", activebackground = "#660066")
previous_page_button_side.pack(side = tk.LEFT)

next_page_button_side = tk.Button(frame, text = "Next Page", command = lambda : next_page(), heigh = 12, width = 11, font=("Arial", 12), bg = "#ffb3ff", activebackground = "#4d004d")
next_page_button_side.pack(side = tk.RIGHT)
#Game's title
games_title_label = tk.Label(frame, text = "", fg = "#d279a6", bg = "#0d001a", font=("Helvetica", 40), heigh = 4)
games_title_label.pack()
#Game's description
game_desc_label = tk.Label(frame, text = "", fg = "#6666ff", bg = "#0d001a", font=("Arial", 24), wraplength = 700)
game_desc_label.pack()
#Link to deal webpage
game_link = ""
games_title_label.bind("<Button-1>", lambda e: link(game_link))


root.mainloop()