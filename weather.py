import requests
api_key = "53049bc3c15db71fff12be30a52c2dc3"
city = input("Enter City Name :")
data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
)
print(f"Temperature: {data.json().get('main')['temp']}°C")