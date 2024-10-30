import requests
import reflex as rfx

#class WeatherApp(rfx):
 #  def __init__(rfx):
        #rfx.api_key = api_key
        #rfx.city = ""
        #rfx.weather_data = None



def render() -> rfx.Component:       
    return rfx.hstack(
        rfx.text("Weather App"),
        rfx.button("Get Weather", on_click=get_weather()),
        rfx.text(weather_data),
            #rfx.text(f"City: {rfx.weather_data['name']}")
            #rfx.text(f"Temperature: {weather_data['main']['temp']}°C")
            #rfx.text(f"Weather: {weather_data['weather'][0]['description']}")
        #rfx.input("Enter city name", on_change=set_city)
        )

def get_weather():        
        url = f"http://opendata.fmi.fi/wfs"#;http://api.openweathermap.org/data/2.5/weather?q={rfx.city}&appid={rfx.api_key}&units=metric"
        response = requests.get(url)
        global weather_data 
        weather_data = None
        
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = "Eipä mittään"
        
#def set_city(rfx):
        #rfx.city = city
def index() -> rfx.Component:
    return rfx.container(
        rfx.box(
            "What is Reflex?",
            # The user's question is on the right.
            text_align="right",
        ),
        rfx.box(
            "A way to build web apps in pure Python!",
            # The answer is on the left.
            text_align="left",
        ),
    )
if __name__ == "__main__":
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    app = rfx.App()
    app.add_page(index)
    #app.add_page(render)