import requests
from utils.const import SECRET

url = f'http://api.weatherapi.com/v1/forecast.json?key={SECRET}&q=Toronto&days=14&aqi=yes&alerts=yes&hour=no'
response = requests.get(url)
print(response.text)