#import json
import requests

API_KEY = "5cc85bc4aa9e55421cc266f88b0f6b04"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

try: 
    def get_weather():

        city = input("Enter a city: ")

        response = requests.get(BASE_URL, params = {"q": city, "appid": API_KEY, "units": "metric"})
        weather_data = response.json()
        #print(json.dumps(weather_data, indent=2))


        if weather_data.get("cod") != 200:
            print("Error:", weather_data.get("message", "Something went wrong."))
        else: 
            weather_list = weather_data.get("weather")
            if weather_list and isinstance(weather_list, list):
                weather = weather_list[0].get("description", "No description available.")
            else: 
                weather = "No description available."
                
            temp = weather_data.get("main", {}).get("temp", "N/A")
            feels_like = weather_data.get("main", {}).get("feels_like", "N/A")
            temp_min = weather_data.get("main", {}).get("temp_min", "N/A")
            temp_max = weather_data.get("main", {}).get("temp_max", "N/A")

            print(f"The weather in the {city} is {weather}.")
            print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
            print(f"The minimun temperare is {temp_min} with the maximum being {temp_max}.")
            print("-" * 40)

    while True:  
        user_continue = (input("Would you like to choose a city? y/n:" ))
        if user_continue == "y":
            get_weather()
        elif user_continue == "n":
            print("Okay have a good day.")
            break
        else:
            print("Sorry can you type that again: ")
except: 
    print("There was an issue in the code")
