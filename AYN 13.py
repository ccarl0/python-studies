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
        #(City, Country, temp_celsius, temp_fahrenheit, icon, weather) This is the tuple it will be printed
        city = json["name"]
        country = json["sys"]["country"]
        temp_kelvin = int(json["main"]["temp"]) #getting the temp in kelvin because it's the only temperature given by the API
        temp_celsius = temp_kelvin - 273.15 #K to C formula
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32 #K to F formul
        weather = json["weather"][0]["main"]
        icon = json["weather"][0]["icon"]
        #here there are all the pieces of information
        final = (city, country, temp_celsius, temp_fahrenheit, weather, icon)

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
        temperatures_label["text"] = "{}°C\t{}°F".format(round(weather[2],2),round(weather[3],2)) #limiting number of digits
        weather_label["text"] = weather[4]
        #weather_icon_canvas["image"] = tk.PhotoImage(file=f"{weather[5]}.png")


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
    #wiki_how_text = f"1. {json['1']}\n2. {json['2']}\n3. {json['3']}\n3. {json['4']}" On demand
    wiki_how_label["text"] = f"{json['1']}"
    wiki_how_label.after(3000, wiki_how) #new advice each 3 seconds
    print(wiki_how_label["text"])

#function to get covid news from https://documenter.getpostman.com/view/10808728/SzS8rjbc API


def covid():
    country = covid_country_text.get()
    #I could use a dict, but listing all the nation is faster.
    #this will be used to get the index to read json file in the right country
    city_list = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina","Armenia",
                 "Australia","Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
                 "Belize", "Benin","Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana,", "Brazil", "Brunei",
                 "Bulgaria","Burkina Faso","Burundi"]

    url = "https://api.covid19api.com/summary" #API URL

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    json = response.json()

    if country == '': #If nothing is written in the label, give world news
        covid_text = f"Today's New Confirmed: {json['Global']['NewConfirmed']}" \
                     f"\nTotal Confirmed: {json['Global']['TotalConfirmed']}" \
                     f"\n\nNew Deaths {json['Global']['NewDeaths']}" \
                     f"\nTotal Deaths: {json['Global']['TotalDeaths']}" \
                     f"\n\nNew Recovered: {json['Global']['NewRecovered']}" \
                     f"\nTotal Recovered: {json['Global']['TotalRecovered']}"

    else: #else gives the country's information
        country = city_list.index(country)
        covid_text = f"COVID-19 in {json['Countries'][country]['Country']}:" \
                     f"\nNew Confirmed: {json['Countries'][country]['NewConfirmed']}" \
                     f"\nTotal Confirmed: {json['Countries'][country]['TotalConfirmed']}" \
                     f"\n\nNew Deaths: {json['Countries'][country]['NewDeaths']}" \
                     f"\nTotal Deaths: {json['Countries'][country]['TotalDeaths']}" \
                     f"\n\nNew Recovered: {json['Countries'][country]['NewRecovered']}" \
                     f"\nTotal Recovered: {json['Countries'][country]['TotalRecovered']}"

    #print(covid_text) #debug
    covid_news_label["text"] = covid_text #the covid label has now the text

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


weather_icon_canvas = tk.Canvas(frame, bg = "#595856")
weather_icon_canvas.pack(fill = tk.BOTH)
weather_icon_canvas.config(width=100, height=100)
weather_icon_canvas.create_image(10, 10, image="", anchor=tk.NW)



"""wiki_how_button = tk.Button(frame, text = "WikiHow Advice", bg = "#D9D0C7", fg = "#05445E", width = 12, command=wiki_how) 
wiki_how_button.pack(side="bottom") #placing in the first row second column""" #for on demand

wiki_how_label = tk.Label(frame, text= " ", font="bold 12")
wiki_how_label.pack(side = tk.BOTTOM)
#wiki_how()

covid_news_label = tk.Label(frame, text = " ", font = "Arial 18")
covid_news_label.pack(anchor = "w", side = "bottom")

covid_news_button = tk.Button(frame, text="Get Covid-19 News!", command = covid, font = "ariel 14")
covid_news_button.pack(anchor = "w", side = "bottom")

covid_country_text = tk.StringVar()
covid_country_entry = tk.Entry(frame, textvariable = covid_country_text, font = "ariel 12")
covid_country_entry.pack(anchor = "w", side = "bottom")

root.mainloop() #like the while loop in pygame