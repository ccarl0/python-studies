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
        games_title_label['text'] = f"{i+1}. {json[i]['title']} \n"
        game_link = json[i]['open_giveaway_url']
        game_desc_label['text'] = json[i]['description']
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

games_title_label = tk.Label(frame, text = "", fg = "#d279a6", bg = "#0d001a", font=("Helvetica", 40), heigh = 4)
games_title_label.pack()

game_desc_label = tk.Label(frame, text = "", fg = "#993366", bg = "#0d001a", font=("Arial", 24), wraplength = 700)
game_desc_label.pack()

get_games_button = tk.Button(frame, text = "Get Games News!!", command = getGamesNews, heigh = 2, font=("Arial", 12), bg = "#660066", activebackground = "#4d004d")
get_games_button.pack(side = tk.BOTTOM, fill = tk.X)
game_link = ""
games_title_label.bind("<Button-1>", lambda e: link(game_link))

root.mainloop()