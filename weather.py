import requests 

API_KEY = "ee1e5021a060906d52965749d0525d75"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather is: " + weather)
    temperature = data["main"]["temp"]
    temperature = temperature - 273.15
    temperature = (temperature * 9/5) + 32
    unit = " degrees fahrenheit"
    print(f"{temperature}{unit}")
else: 
    print("An error has occured")