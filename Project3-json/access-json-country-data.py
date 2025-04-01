import requests

url = 'https://restcountries.com/v3.1/all'
response = requests.get(url)

country = "mexico"

content = response.json()

for c in content:
    country_name = c['name']['common']
    if country_name == country:
        capital = c['capital']
print(capital)