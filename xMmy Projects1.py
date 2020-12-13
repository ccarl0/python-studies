"""
App created by Carlo Cecchetti
I post this starting project just to say that I'm back.
This app aims to get stuff about games giveaways.
I also want to make something that runs in background that sends notifications (plyer)
"""

from plyer import notification
import requests
import tkinter as tk

games = requests.get("https://www.gamerpower.com/api/giveaways?platform=pc")
json = games.json()
for x in range(len(json)):
    print(json[x]['title'] + " -----> " + json[x]["description"])
#print(json)

def getGamesNews():
    games = requests.get("https://www.gamerpower.com/api/giveaways?platform=pc")
    json = games.json()

    games_list = []
    for x in range(len(json)):
        games_list.append(json[x]['title'])


    games_title_label['text'] = games_list



root = tk.Tk()
root.geometry("1200x720") #tab x,y
root.title("XMy Projects")
root.iconphoto(False, tk.PhotoImage(file="icon.png"))

frame = tk.Frame(root, bg = "#0d001a")
frame.place(relwidth=1, relheight=1)

games_title_label = tk.Label(frame, text = "aaaaaaaaaa", fg = "#80aaff", bg = "#0d001a", width = 50)
games_title_label.pack(anchor = tk.NW)

get_games_button = tk.Button(frame, text = "Get Games News!!", command = getGamesNews())
get_games_button.pack(side = tk.BOTTOM)

root.mainloop()