def get_weather(city):
    API_key = "your api key(after creating a account im openweathermap.org you get a api)"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    if res.status_code == 404:
        messagebox.showerror("Error 404!")
        return None
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp']-273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    #city = weather['timezone']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url,temperature,description,city,country)
def search():
    city = city_inp.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city, country = result
    location_lbl.configure(text=f"{city},{country}")
    img = Image.open(requests.get(icon_url,stream=True).raw)
    icon = ImageTk.PhotoImage(img)
    icon_lbl.configure(image=icon)
    icon_lbl.image = icon

    temp_lbl.configure(text=f"Temperature : {temperature:.2f}C")
    descrip_lbl.configure(text=f"Description : {description}")

import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import ttkbootstrap

win = ttkbootstrap.Window(themename='morph')
win.title("Weather App")
win.geometry('400x400')

city_inp = ttkbootstrap.Entry(win,font="Helvetica,18")
city_inp.pack(pady=10)

src_btn = ttkbootstrap.Button(win,text="Search",command=search, bootstyle="success")
src_btn.pack(pady=10)

location_lbl = tk.Label(win,font="Helvetica,25")
location_lbl.pack(pady=20)

icon_lbl = tk.Label(win)
icon_lbl.pack()

temp_lbl = tk.Label(win,font="Helvetica,25")
temp_lbl.pack()

descrip_lbl = tk.Label(win,font="Helvetica,25")
descrip_lbl.pack()


win.mainloop()
