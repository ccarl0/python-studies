"""
App created by Carlo
This will show all the information you need
"""
import tkinter as tk
from tkinter import messagebox
import time
import os
from configparser import ConfigParser #Need to get the key from the config.ini file
import requests


weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}" #URL from the API of weather site

config_file = "config.ini" #the config file
config = ConfigParser() #calling the class
config.read(config_file) #use read module from Config class
api_key = config["api_key"]["key"] #api_key is getting by "indexing" the config file

def get_weather(city):
    result = requests.get(weather_url.format(city, api_key))
    if result:
        json = result.json() #to read the json information provided by the weather site
        #(City, Country, temp_celsius, temp_fahrenheit, weather) This is the tuple it will be printed
        #getting the indo by "index" the json information
        city = json["name"]
        country = json["sys"]["country"]
        temp_kelvin = int(json["main"]["temp"]) #getting the temp in kelvin because it's the only temperature given by the API
        temp_celsius = temp_kelvin - 273.15 #K to C formula
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32 #K to F formula
        weather = json["weather"][0]["main"]
        #here there is all the piece of information
        final = (city, country, temp_kelvin, temp_celsius, temp_fahrenheit, weather)
        return final

    else:
        return None

def search():
    global image
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        #the tuple of information is now weather, so index is to weather since it gets info from there
        location_label["text"] = f"{weather[0]},{[weather[1]]}"
        image["bitmap"] = "{}.png".format(weather[5]) #bitmap error
        temperatures_label["text"] = "{}°C\t{}°F".format(round(weather[3],2),round(weather[4],2)) #limiting number of digits
        weather_label["text"] = weather[6]
    else:
        tk.messagebox.showerror("Error","Cannot find city {}".format(city))
    return weather

#This function return a new label each 5 seconds for advice
def wiki_how():
    #getting
    wki_how_url = "https://hargrimm-wikihow-v1.p.rapidapi.com/steps"  # wiki_how steps API

    querystring = {"count": "5"}

    headers = {
        'x-rapidapi-host': "hargrimm-wikihow-v1.p.rapidapi.com",
        'x-rapidapi-key': "9b7b35517amsha9a79527dd2c8fdp1b59eejsnf96e8b1bb440"
    }

    response = requests.request("GET", wki_how_url, headers=headers, params=querystring)
    #formatting
    json = response.json()
    #wiki_how_text = f"1. {json['1']}\n2. {json['2']}\n3. {json['3']}\n3. {json['4']}" #just to save this.
    wiki_how_label["text"] = f"{json['1']}"
    wiki_how_label.after(5000, wiki_how)
    print(wiki_how_label["text"])

#function to update time
def display_time():
    current_time = time.strftime("%I:%M:%S\n%d/%b/%Y") #format
    clock_label["text"] = current_time
    clock_label.after(100, display_time) #continues to recall itself

#-----------------------------------------------------------------------------------------------------------------------

root = tk.Tk() #initialization of the GUI

root.title("AllYouNeed") #changing the title

frame = tk.Frame(root, bg = "#595856") #changing bg color
frame.place(relwidth=1, relheight=1) #these 2 1s means the part of the canvas to color. 1 is 100%

clock_label = tk.Label(frame, font = "verdana 15") #giving the format
clock_label.pack(anchor = "e", side = "bottom") #position
display_time() #calling the function

city_text = tk.StringVar()
city_entry = tk.Entry(frame, textvariable = city_text)
city_entry.pack()

search_button = tk.Button(frame, text = "SEARCH", bg = "#D9D0C7", fg = "#05445E", width = 12, command=search) #What will be the search button
search_button.pack() #placing in the first row second column

location_label = tk.Label(frame, text = ":", font="bold 14")
location_label.pack()

temperatures_label = tk.Label(frame, text = "", font="bold 11")
temperatures_label.pack()

weather_label = tk.Label(frame, text = "", font = "bold 14")
weather_label.pack()

"""wiki_how_button = tk.Button(frame, text = "WikiHow Advice", bg = "#D9D0C7", fg = "#05445E", width = 12, command=wiki_how) #What will be the search button
wiki_how_button.pack(side="bottom") #placing in the first row second column""" #

wiki_how_label = tk.Label(frame, text= " ", font="bold 14")
wiki_how_label.pack(side = tk.BOTTOM)
wiki_how()

root.mainloop() #like the while loop in pygame