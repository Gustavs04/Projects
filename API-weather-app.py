import requests

API_KEY = "f95575702de57ef3ea881c47a8f87d4e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather: ", weather)
    print("Tempeature: ", temperature, "celsius")

else:
    print("An error occurred.")
