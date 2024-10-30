import requests
from reflex import Reflex

class WeatherApp(Reflex):
    def __init__(self, api_key):
        self.api_key = api_key
        self.city = ""
        self.weather_data = None

    def get_weather(self):
        if not self.city:
            return
        url = f"http://opendata.fmi.fi/wfs"#;http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            self.weather_data = response.json()
        else:
            self.weather_data = None


    def render(self):
        self.clear()
        self.text("Weather Application")
        self.input("Enter city name", on_change=self.set_city)
        self.button("Get Weather", on_click=self.get_weather)
        if self.weather_data:
            self.text(f"City: {self.weather_data['name']}")
            self.text(f"Temperature: {self.weather_data['main']['temp']}°C")
            self.text(f"Weather: {self.weather_data['weather'][0]['description']}")
        else:
            self.text("No weather data available")

    def set_city(self, city):
        self.city = city

if __name__ == "__main__":
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    app = WeatherApp(api_key)
    app.run()