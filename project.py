# import pygame package
import PySimpleGUI as la
from requests import get, post
from datetime import datetime

city = "ruston"
temp = ""
pres = ""
hum = ""
rise = ""
set = ""
speed = ""


la.theme("Topanga")
def One():
    layout_template = [[la.Text(f"Temperature: {temp}", key = "temp", font = ("Helvetica", 15)), la.Push(), la.Text(f"Inside Temperature: ", font = ("Helvetica", 15))],
    [la.Text(f"Pressure: {pres}", key = "pres" ,font = ("Helvetica", 15)), la.Push(), la.Text(f"Inside Pressure: ", font = ("Helvetica", 15))],
    [la.Text(f"Humidity: {hum}", key = "hum" , font = ("Helvetica", 15)), la.Push(), la.Text(f"Inside Humidity: ", font = ("Helvetica", 15))],
    [la.Text(f"Sun Rise: {rise}", key = "rise", font = ("Helvetica", 15))],
    [la.Text(f"Sun Set: {set}", key = "set", font = ("Helvetica", 15))],
    [la.Text(f"Wind Speed: {speed}", key = "speed", font = ("Helvetica", 15))],
    [la.Push(), la.Text("What is your city?", font = ("Helvetica", 15)), la.Push()],
    [la.Push(), la.Input("", font = ("Helvetica", 15), key = "input", size = (20, 50)), la.Push()],
    [la.Button("Enter", font = ("Helvetica", 15), pad=(215, 0))]
    ]

    layout = [[la.Column(layout_template, element_justification = "left")]]

    window = la.Window("Weather Report", layout)

    while True:
        event, values = window.read()
        if event == la.WIN_CLOSED:
            break
        if event == "Enter":
            city = values["input"]
            data = get(f"http://138.47.139.207:5000/weather/{city}").json()
            tem = data["temperature"]
            pre = data["pressure"]
            humi = data["humidity"]
            Srise = data["sunrise"]
            sunrisedt = datetime.fromtimestamp(Srise)
            sunriseT = sunrisedt.strftime("%I:%M:%S %p")
            Sset = data["sunset"]
            sunsetdt = datetime.fromtimestamp(Sset)
            sunsetT = sunsetdt.strftime("%I:%M:%S %p")
            Sspeed = data["windSpeed"]
            window["temp"].update(f"Temperature: {tem}°F")
            window["pres"].update(f"Pressure: {pre} mb")
            window["hum"].update(f"Humidity: {humi}%")
            window["rise"].update(f"Sun Rise: {sunriseT}")
            window["set"].update(f"Sun Set: {sunsetT}")
            window["speed"].update(f"Wind Speed: {Sspeed} mp/h")
            


    window.close()


One()