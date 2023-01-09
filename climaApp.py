from tkinter import *
from unicodedata import name
import requests

#28ec67e302ac1dcc41a4ae6accb2c6c8
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def mostrar_repuesta(clima):
    try:
        mostrar_nombre = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]

        ciudad["text"] = mostrar_nombre
        temperatura["text"] = str(int(temp)) + "ºC"
        descripcion["text"] = desc
    except:
        ciudad["text"] = "intenta nuevamente"

def clima_JSON(ciudad):
    try:
        API_key = "28ec67e302ac1dcc41a4ae6accb2c6c8"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID" : API_key, "q": ciudad, "units": "metric", "lang": "es"}
        response = requests.get(URL, params = parametros)
        clima = response.json()
        mostrar_repuesta(clima)    
    except:
        print("Error")

ventana = Tk()
ventana.geometry("350x550")

texto_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify = "center")
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text = "obtener clima", font = ("Courier", 20, "normal"), command = lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font = ("Courier", 20, "normal" ))
ciudad.pack(padx = 20, pady = 20 ) 

temperatura = Label(font = ("Courier", 50, "normal" ))
temperatura.pack(padx = 10, pady = 10 ) 

descripcion = Label(font = ("Courier", 20, "normal" ))
descripcion.pack(padx = 10, pady = 10 )





ventana.mainloop()  