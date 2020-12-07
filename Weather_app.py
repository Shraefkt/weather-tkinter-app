import tkinter as tk
from tkinter import font
import requests
from PIL import ImageTk, Image
import PIL
import json
HEIGHT = 700
WIDTH = 800
favourites = []
def menu():
    menu = tk.Menu(root)
    root.config(menu=menu)

    homemenu = tk.Menu(menu, activebackground="blue",tearoff = 0)
    menu.add_cascade(label="Menu", menu=homemenu)
    homemenu.add_command(label="Search", command=lambda: searchpage())
    homemenu.add_command(label="About", command=lambda: aboutpage())
    homemenu.add_command(label="Favourites", command=lambda: favourite_page())
def setup():
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    menu()
def searchpage(city = None):
    changepage()
    setup()
    def get_weather(entry):
        weather_key = "a2ee5948b995968376bf6312695d9996"
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"APPID": weather_key,
                  "q": entry,
                  "units": "metric"}

        response = requests.get(url, params=params)
        weather = response.json()
        label["text"] = format_response(weather)

    def format_response(weather):
        try:
            city_name = weather["name"]
            description = weather["weather"][0]["description"]
            temperature = weather["main"]["temp"]
            final_str = "\nCity: %s \nConditions: %s\nTemperature (°C):  %s" % (city_name, description, temperature)
            label["font"] = ("Haettenschweiler", 40)
        except:
            final_str = "There was a problem retrieving information"
            label["font"] = ("Blackadder ITC", 30)
        else:
            favourite_button = tk.Button(lower_frame,relief = "flat",fg = "black",anchor = "n",font = ("javanese text",20),text="★ Add place to favourites",bg = "#ffd27f",command = lambda:favourite(weather),activebackground = "#ffd45f")
            favourite_button.place(relwidth = 0.5,relheight = 0.17,relx = 0.25,rely = 0.7)
        return final_str


    def image(image):
        img = ImageTk.PhotoImage(Image.open(image))
        l = tk.Label(root, image=img)
        l.pack(expand=True)

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,bg = "#000010")
    canvas.place(relheight = 1,relwidth = 1, relx = 0, rely =0)

    frame = tk.Frame(root, bg="#000010", bd=5)
    frame.place(relheight=0.1, relwidth=0.85, relx=0.5, rely=0.1, anchor="n")

    button = tk.Button(frame, cursor="exchange", font=("tw cen mt condensed", 25, "bold"), text="Search", bg="#be9d6a", fg="black",
                       command=lambda: get_weather(entry.get()),relief = "solid",activeforeground = "black",
activebackground = "#907647")
    button.place(relx=0.75, rely=0, relheight=1, relwidth=0.25)

    global entry
    entry = tk.Entry(frame, font=("tw cen mt condensed", 25),fg = "black", bg = "#c8ae81")
    entry.place(relwidth=0.73, relheight= 1)

    lower_frame = tk.Frame(root, bg="black", bd = 10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.6, anchor="n")

    label = tk.Label(lower_frame, bg="black",fg = "#263038", anchor = "n")
    label.place(relwidth=1, relheight=1)

    if city:
        entry.insert(0,city)
def aboutpage():
    changepage()
    setup()
    about_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
    about_canvas.place(relheight=1, relwidth=1, relx=0, rely=0)
    about_frame = tk.Frame(root, bg="#b9c7d6", bd=15)
    about_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.75, anchor="n")
    description = tk.Label(about_frame, justify="left", wraplength=500,
                           text="About:",
                           bg="black", font=("harlow solid italic", 40),anchor = "nw",fg = "#818b95",borderwidth = 30)

    description.place(relwidth=1, relheight=1,relx = 0, rely = 0 )

    about_label = tk.Label(about_frame, justify="left", wraplength=500,
                           text="This is a simple weather app.\nTo check the weather ;\nGo to the searchpage and search for weather via city or country name.\nClick add place to favourites to view quickly through favourites.",
                           bg="black", font=("Elephant", 25),anchor = "nw",fg = "#b9c7d6",borderwidth = 30)
    about_label.place(relwidth=1, relheight=0.8,relx = 0,rely = 0.2)
def favourite(weather):
    if weather["name"] not in favourites:
        favourites.insert(0,weather["name"])
def favourite_page():
    changepage()
    setup()
    if not favourites:
        str = "No Favourites yet, go search for cities to add."
    else:
        str = ""
    bg_colors = ["#2a0108","#c3312d","#5e1000","#1f0004","#51010c"]
    for i in range(5):
        bg = bg_colors[i]
        decorative_frame = tk.Frame(root, bg=bg, bd=10)
        decorative_frame.place(relx = i * 0.2,rely = 0,relwidth = 0.2,relheight = 1)

    fav_frame = tk.Frame(root, bg="black", bd=0)
    fav_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.75, anchor="n")
    fav_label = tk.Label(fav_frame,text = "\nFavourite cities (click to get weather) : \n" + str,fg = "#fbd48a", bg = "black",font = ("tw cen mt condensed",25),anchor = "n",justify = "left")
    fav_label.place(relwidth=1, relheight=1,relx = 0.5,rely = 0,anchor = "n")
    try:
        R1 = tk.Radiobutton(fav_frame, text=favourites[0],bg = "black",fg = "white",font = ("tw cen mt condensed",20),command = lambda: searchpage(favourites[0]))
        R1.place(relwidth = 0.4,relheight = 0.1,relx = 0.05,rely = 0.25)
        R2 = tk.Radiobutton(fav_frame, text=favourites[1],bg = "black",fg = "white", font=("tw cen mt condensed", 20),command = lambda: searchpage(favourites[1]))
        R2.place(relwidth=0.4, relheight=0.1, relx=0.05, rely=0.5)
        R3 = tk.Radiobutton(fav_frame, text=favourites[2],bg = "black",fg = "white",font=("tw cen mt condensed", 20),command = lambda: searchpage(favourites[2]))
        R3.place(relwidth=0.4, relheight=0.1, relx=0.05, rely=0.75)
    except:
        pass
def changepage():
    global root
    for widget in root.winfo_children():
        widget.destroy()


#main
root = tk.Tk()
aboutpage()
root.mainloop()