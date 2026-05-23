import requests, time

print(a:="-:| Weather App(West Bengal) |:-")
print("-"*len(a))

wb_data = [
        "Kolkata", "Howrah", "North 24 Parganas", "South 24 Parganas", "Hooghly",
        "Darjeeling", "Kalimpong", "Jalpaiguri", "Alipurduar", "Cooch Behar",
        "Uttar Dinajpur", "Dakshin Dinajpur", "Malda", "Murshidabad", "Birbhum",
        "Nadia", "Purba Bardhaman", "Paschim Bardhaman", "Bankura", "Purulia",
        "Jhargram", "Purba Medinipur", "Paschim Medinipur"
]
for i, district in enumerate(wb_data, start = 1):
        print(f"{i}) {district}")

api_key = "54707cdf03354dbf8f571707261805"

city = input("\nEnter the nearest District:-\n: ").title()
if city not in wb_data:
    time.sleep(1)
    print("\nError: Invalid Input")
    exit()
    
url = "http://api.weatherapi.com/v1/current.json"
params = {
          "key": api_key,
          "q":   f"{city}, West Bengal, India"
          }

time.sleep(0.5)
print("\nFetching Data....")

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    location_info = data['location']
    forecast_info = data['current']
    print("\n| Location |")
    print("-"*36)
    print(f"City : {location_info['name']}")
    print(f"State : {location_info['region']}")
    print(f"Country : {location_info['country']}")
    print(f"Current time : {location_info['localtime']}")
    print("-"*36)
    print("\n| Forecast |")
    print("-"*36)
    print(f"Temprature : {forecast_info['temp_c']}°C")
    print(f"Feels like : {forecast_info['feelslike_c']}°C")
    print(f"Humidity : {forecast_info['humidity']}%")
    print(f"Status : {forecast_info['condition']['text']}")
    print("-"*36)
else:
    print(f"Error: {response.status_code}")