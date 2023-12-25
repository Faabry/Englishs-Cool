from datetime import datetime as dt
import requests


class Greeting:
    def __init__(self):
        # Class atributes
        self.date = dt.now()
        self.hour = self.date.hour
        self.minute = self.date.minute


    def greetings(self):
        # Getting the wheater information from an API 
        url = "https://open-weather13.p.rapidapi.com/city/Araras"

        headers = {
            "X-RapidAPI-Key": "eb398b1c3emsh43bd73881cb151ap15c148jsne2785acdd1bb",
            "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        # Temperature
        temperature = response.json().get("main",{}).get("temp")
        city = response.json().get("name")
        weather_description = response.json().get("weather", [{}])[0].get("description")

         # Get the corresponding emoji for the weather condition
        weather_emoji = self.get_weather_emoji(weather_description)
        
        # Greetings conditional
        if self.hour < 12:
            return f"Bom Dia {weather_emoji}\n{city} {self.fahrenheit_to_celsius(temperature):.0f}ºC"
        
        elif self.hour < 18:
            return f"Boa Tarde ⛅\n{city} {self.fahrenheit_to_celsius(temperature):.0f}ºC"
        
        else:
            return f"Boa Noite 🌙\n{city} {self.fahrenheit_to_celsius(temperature):.0f}ºC"
        
    
    # Getting the hour with minutes
    def get_hour(self):
        self.date = dt.now()
        self.hour = self.date.hour
        self.minute = self.date.minute

        if self.hour < 10:
            self.hour = f"{0}{self.hour}"

        elif self.minute < 10:
            self.minute = f"{0}{self.minute}"
        
        return f"{self.hour}:{self.minute}"


    # Getting the day and month
    def get_day(self):
        self.date = dt.today()
        self.day = self.date.day
        self.month = self.date.month
        self.year = self.date.year
        self.list_months = ["Janeiro", "Fevereiro",
                            "Março", "Abril", 
                            "Maio", "Junho", 
                            "Julho", "Agosto", 
                            "Setembro", "Outubro", 
                            "Novembro", "Dezembro"]
        
        # Received the list of months in the month index
        self.month_name = self.list_months[self.month - 1]    
        return f"{self.day} de {self.month_name} de {self.year}"
    

    # Converting from fahrenheit to celsius
    def fahrenheit_to_celsius(self, temperature):
        return (temperature - 32) * 5 / 9
    

    # Getting the wheater emoji according the the current wheater
    def get_weather_emoji(self, weather_description):
        weather_mapping = {
            "clear sky": "☀️",
            "few clouds": "🌤️",
            "scattered clouds": "🌥️",
            "broken clouds": "☁️",
            "shower rain": "🌧️",
            "rain": "🌧️",
            "thunderstorm": "⛈️",
            "snow": "❄️",
            "mist": "🌫️",
        }
        # Retrieve the emoji based on the weather_description
        return weather_mapping.get(weather_description.lower(), "🌦️")
    

    # Changing the theme dynamically
    def get_theme(self):
        if 6 <= self.hour < 12:
            return 'LightBlue'
        elif 12 <= self.hour < 18:
            return 'DarkAmber'
        else:
            return 'DarkPurple4'


    