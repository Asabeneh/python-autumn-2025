import requests
from pprint import pprint

url = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(url)
data = response.json()
pprint(data[0])


countries = []
for cat in data:
    # print(cat['name'], cat['origin'], cat['life_span'])
      country = cat['origin']
      countries.append(country)
print(countries)


life_spans = []
for cat in data:
      life_span = cat['life_span']
      lowest = life_span.split(' - ')[0]
      highest = life_span.split(' - ')[1]
      average = ( int(lowest) + int(highest)) / 2
      life_spans.append(average)

average_life_span = sum(life_spans) / len(life_spans)
print(average_life_span)