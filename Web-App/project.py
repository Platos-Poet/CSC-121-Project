# import pygame package
import PySimpleGUI as la
from requests import get, post
from IP import IP
from datetime import datetime
# import board
# import adafruit_dht
# sensor = adafruit_dht.DHT11(board.D13)

def currentTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

city = "ruston"
temp = ""
pres = ""
hum = ""
rise = ""
set = ""
speed = ""
first = False

def tickspeed():
    return 2000

la.theme("Topanga")
def One():
    layout = [[la.Push(), la.Text(f"Current Time: {currentTime()}", key = "time", font = ("Helvetica", 42)), la.Push()],
    [la.Text(f"Current Weather: {temp}", key = "desc", font = ("Helvetica", 42)), la.Push(), la.Text(f"Inside Temperature: ", key = "itemp", font = ("Helvetica", 42))],
    [la.Text(f"Temperature: {temp}", key = "temp", font = ("Helvetica", 42)), la.Push(), la.Text(f"Inside Humidity: ", key = "ihum", font = ("Helvetica", 42))],
    [la.Text(f"Pressure: {pres}", key = "pres" ,font = ("Helvetica", 42)),la.Push()],
    [la.Text(f"Humidity: {hum}", key = "hum" , font = ("Helvetica", 42)),la.Push()],
    [la.Text(f"Sun Rise: {rise}", key = "rise", font = ("Helvetica", 42)),la.Push()],
    [la.Text(f"Sun Set: {set}", key = "set", font = ("Helvetica", 42)),la.Push()],
    [la.Text(f"Wind Speed: {speed}", key = "speed", font = ("Helvetica", 42)),la.Push()],
    [la.Push(), la.Text("What is your city?", font = ("Helvetica", 42)), la.Push()],
    [la.Push(), la.Input("Ruston", font = ("Helvetica", 42), key = "input", size = (20, 50)), la.Push()],
    [la.Push(), la.Button("Enter", font = ("Helvetica", 42)), la.Push()]
    ]

    window = la.Window('Window Title', layout, finalize=True, no_titlebar=True, location=(0,0))
    window.maximize()

    while True:
        event, values = window.read(timeout=tickspeed())
        if event == la.WIN_CLOSED:
            break
        global first
        if first == True:
            if event == la.TIMEOUT_KEY:
                data = get(f"http://{IP}:5000/weather/{city}").json()
                weather = data["Weather Description"]
                tem = data["Temperature"]
                pre = data["Pressure"]
                humi = data["Humidity"]
                Srise = data["Sunrise"]
                Sset = data["Sunset"]
                Sspeed = data["Wind Speed"]
                # itemp = (sensor.temperature * 9/5 + 32)
                # ihum = sensor.humidity
                window["time"].update(f"Current Time: {currentTime()}")
                window["desc"].update(f"Current Weather: {weather}")
                window["temp"].update(f"Temperature: {tem}")
                window["pres"].update(f"Pressure: {pre}")
                window["hum"].update(f"Humidity: {humi}")
                window["rise"].update(f"Sun Rise: {Srise}")
                window["set"].update(f"Sun Set: {Sset}")
                window["speed"].update(f"Wind Speed: {Sspeed}")
                # window['ihum'].update(f"Inside Humidity: {ihum}%")
                # window['itemp'].update(f"Inside Temperature: {itemp}°F")
        if event == "Enter":
            city = values["input"]
            data = get(f"http://{IP}:5000/weather/{city}").json()
            weather = data["Weather Description"]
            tem = data["Temperature"]
            pre = data["Pressure"]
            humi = data["Humidity"]
            Srise = data["Sunrise"]
            Sset = data["Sunset"]
            Sspeed = data["Wind Speed"]
            # itemp = (sensor.temperature * 9/5 + 32)
            # ihum = sensor.humidity
            window["time"].update(f"Current Time: {currentTime()}")
            window["desc"].update(f"Current Weather: {weather}")
            window["temp"].update(f"Temperature: {tem}")
            window["pres"].update(f"Pressure: {pre}")
            window["hum"].update(f"Humidity: {humi}")
            window["rise"].update(f"Sun Rise: {Srise}")
            window["set"].update(f"Sun Set: {Sset}")
            window["speed"].update(f"Wind Speed: {Sspeed}")
            # window['ihum'].update(f"Inside Humidity: {ihum}%")
            # window['itemp'].update(f"Inside Temperature: {itemp}°F")
            first = True
        

    window.close()


One()