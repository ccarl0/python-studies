"""
App created by Carlo Cecchetti
I post this starting project just to say that I'm back.
This app aims to get stuff about games giveaways.
I also want to make something that runs in background that sends notifications (plyer)
"""

from plyer import notification
import requests
import tkinter as tk
import webbrowser


"""games = requests.get("https://www.gamerpower.com/api/giveaways?platform=pc")
json = games.json()
for x in range(len(json)):
    print(json[x]['title'] + " -----> " + json[x]["description"])
#print(json)"""

i = 0
def getGamesNews():
    global i, game_link
    games = requests.get("https://www.gamerpower.com/api/giveaways?platform=pc")
    json = games.json()
    try:
        games_title_label['text'] = f"{i+1}. {json[i]['title']}"
        game_link = json[i]['open_giveaway_url']
        i += 1
    except:
        games_title_label['text'] = "GAMES' NEWS HAVE FINISHED"
        i = 0

def link(url):
    webbrowser.open_new(url)

root = tk.Tk()
root.geometry("1200x720") #tab x,y
root.title("XMy Projects")
root.iconphoto(False, tk.PhotoImage(file="icon.png"))

frame = tk.Frame(root, bg = "#0d001a")
frame.place(relwidth=1, relheight=1)

game_link = ""
games_title_label = tk.Label(frame, text = "", fg = "#80aaff", bg = "#0d001a", font=("Helvetica", 30))
games_title_label.pack()
games_title_label.bind("<Button-1>", lambda e: link(game_link))

get_games_button = tk.Button(frame, text = "Get Games News!!", command = getGamesNews)
get_games_button.pack(side = tk.BOTTOM)

root.mainloop()