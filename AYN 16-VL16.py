"""
App created by Cecchetti Carlo
ViewLoon, A view of all
Beta Version
"""
import time #Clock
import tkinter as tk #GUI
from configparser import ConfigParser #Config. API
from tkinter import messagebox #Error MSG

import requests #APIs req.

weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}" #Weather API
#get API key
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config["api_key"]["key"]

def get_weather(city):      #Requests/Getting
    result = requests.get(weather_url.format(city, api_key))
    if result:
        json = result.json() #read json file
        city = json["name"]
        country = json["sys"]["country"]
        temp_kelvin = int(json["main"]["temp"]) #API return only K
        temp_celsius = temp_kelvin - 273.15 #K to C
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32 #K to F
        weather = json["weather"][0]["main"]
        icon = json["weather"][0]["icon"]

        final = (city, country, temp_celsius, temp_fahrenheit, weather, icon)
        return final

    else:
        return None

def search():       #Setting
    #get city name and run function that requests and get info
    city = city_text.get().capitalize()
    weather = get_weather(city)
    if weather:
        location_label["text"] = f"{weather[0]},{[weather[1]]}" #set parameter "text" of location_label
        temperatures_label["text"] = "{}°C\t{}°F".format(round(weather[2],2),round(weather[3],2)) #limiting number of digits
        weather_label["text"] = weather[4]
        image["file"] = f"{weather[5]}.png"
        #print(f"{weather[5]}.png")

    else:
        tk.messagebox.showerror("Error",f"Cannot find city {city}")
    return weather

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
    wiki_how_label["text"] = f"{json['1']}"
    wiki_how_label.after(3000, wiki_how) #new advice each 3 seconds
    #print(wiki_how_label["text"])


def covid():        #get covid news from https://documenter.getpostman.com/view/10808728/SzS8rjbc API
    country = covid_country_text.get().capitalize()
    url = "https://api.covid19api.com/summary" #API URL
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    json = response.json()

    city_dict = {} #define the dict that will contain the list of all the countries
    for x in range(len(json["Countries"])): #create dict
        city_dict.update({json["Countries"][x]["Country"]: x})

    if country not in city_dict and country != "":
        tk.messagebox.showerror(f'Country not found', f'Cannot find the following country:\n "{country}"')

    if country == '': #no country -> world news
        covid_text = f"Today's New Confirmed: {json['Global']['NewConfirmed']}" \
                     f"\nTotal Confirmed: {json['Global']['TotalConfirmed']}" \
                     f"\n\nNew Deaths {json['Global']['NewDeaths']}" \
                     f"\nTotal Deaths: {json['Global']['TotalDeaths']}" \
                     f"\n\nNew Recovered: {json['Global']['NewRecovered']}" \
                     f"\nTotal Recovered: {json['Global']['TotalRecovered']}"

    else: #give given country's news
        country = city_dict.get(country)
        covid_text = f"COVID-19 in {json['Countries'][country]['Country']}:" \
                     f"\nNew Confirmed: {json['Countries'][country]['NewConfirmed']}" \
                     f"\nTotal Confirmed: {json['Countries'][country]['TotalConfirmed']}" \
                     f"\n\nNew Deaths: {json['Countries'][country]['NewDeaths']}" \
                     f"\nTotal Deaths: {json['Countries'][country]['TotalDeaths']}" \
                     f"\n\nNew Recovered: {json['Countries'][country]['NewRecovered']}" \
                     f"\nTotal Recovered: {json['Countries'][country]['TotalRecovered']}"

    #print(covid_text)
    covid_news_label["text"] = covid_text #set covid_new_label(text) parameter

#function to update time
def display_time():
    current_time = time.strftime("%I:%M:%S\n%d/%b/%Y") #format
    clock_label["text"] = current_time
    clock_label.after(100, display_time) #recall itself each second

#-----------------------------------------------------------------------------------------------------------------------

root = tk.Tk() #init the GUI
root.geometry("1200x720") #tab x,y
root.title("ViewLoon")
root.iconphoto(False, tk.PhotoImage(file="icon.png"))

frame = tk.Frame(root, bg = "#0d001a")
frame.place(relwidth=1, relheight=1)

#clock
clock_label = tk.Label(frame, font = "verdana 15", bg = "#0c001a", fg = "#e0ccff")
clock_label.pack(anchor = "e", side = "bottom")
display_time()
#weather
weather_frame = tk.Frame(frame, bg = "#28004d")
weather_frame.pack()

city_text = tk.StringVar()
city_entry = tk.Entry(weather_frame, textvariable = city_text)
city_entry.pack()

search_button = tk.Button(weather_frame, text = "SEARCH", bg = "#001f4d", fg = "#e6f0ff", width = 12, command=search)
search_button.pack() #placing in the first row second column

location_label = tk.Label(weather_frame, text = "", font="bold 14", bg = "#28004d", fg = "#e0ccff")
location_label.pack()

temperatures_label = tk.Label(weather_frame, text = "", font="bold 11", bg = "#28004d", fg = "#e0ccff")
temperatures_label.pack()

weather_label = tk.Label(weather_frame, text = "", font = "bold 14", bg = "#28004d", fg = "#e0ccff")
weather_label.pack()

image = tk.PhotoImage(file="")
icon_label = tk.Label(weather_frame, image=image, bg = "#28004d", fg = "#e0ccff")
icon_label.pack()
#wikihow
wiki_how_label = tk.Label(frame, text= " ", font="bold 15", bg = "#000033", fg = "#9999ff")
wiki_how_label.pack(side = tk.BOTTOM)
wiki_how()
#covid
covid_news_label = tk.Label(frame, text = " ", font = "Arial 18", bg = "#0a001a", fg = "#f2e6ff")
covid_news_label.pack(anchor = "w", side = "bottom")

covid_news_button = tk.Button(frame, text="Get Covid-19 News!", command = covid, font = "ariel 14", bg = "#002966", fg = "#e6f0ff")
covid_news_button.pack(anchor = "w", side = "bottom")

covid_country_text = tk.StringVar()
covid_country_entry = tk.Entry(frame, textvariable = covid_country_text, font = "ariel 12")
covid_country_entry.pack(anchor = "w", side = "bottom")

root.mainloop() #like the while loop in pygame
