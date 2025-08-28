import requests
import tkinter as tk
from tkinter import messagebox

# Function to get weather data
def get_weather(city):
    api_key = "d2733020e095be9f41e9cb3ac2d7185d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    return response.json()

# Function to display weather
def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    if weather_data['cod'] == '404':
        messagebox.showerror("Error", "City not found")
        return
    main = weather_data['main']
    wind = weather_data['wind']
    weather_desc = weather_data['weather'][0]['description']
    temp = main['temp'] - 273.15  # Convert from Kelvin to Celsius
    pressure = main['pressure']
    humidity = main['humidity']
    wind_speed = wind['speed']
    weather_info = f"Temperature: {temp:.2f} °C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {weather_desc}"
    weather_label.config(text=weather_info)

# Setting up the GUI
app = tk.Tk()
app.title("Weather App")
app.geometry("400x400")
app.config(bg="#87CEEB")  # Light blue background

# Title label
title_label = tk.Label(app, text="Weather App", font=("Helvetica", 18, "bold"), bg="#87CEEB", fg="white")
title_label.pack(pady=10)

city_label = tk.Label(app, text="Enter City:", font=("Helvetica", 14, "bold"), bg="#87CEEB", fg="white")
city_label.pack(pady=10)

city_entry = tk.Entry(app, width=25, font=("Helvetica", 14))
city_entry.pack(pady=5)

search_button = tk.Button(app, text="Get Weather", command=show_weather, font=("Helvetica", 14, "bold"), bg="#4682B4", fg="white")
search_button.pack(pady=10)

weather_label = tk.Label(app, text="", font=("Helvetica", 14), bg="#87CEEB", fg="white")
weather_label.pack(pady=20)

app.mainloop()
