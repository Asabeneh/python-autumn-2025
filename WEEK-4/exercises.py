from countries import countries
from pprint import pprint
# pprint(countries)

# for country in countries:
#     if country.startswith('C'):
#         print(country, countries.count(country))

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lst = []
for letter in alphabets:
    count = 0
    new_lst = []
    for country in countries:
        if country.startswith(letter):
            count = count + 1
            new_lst.append(country)
    dct = {
        'letter':letter,
        'count':count,
        # 'countries':new_lst
    }
    lst.append(dct)
    


pprint(sorted(lst, key = lambda x: x['count'], reverse=True))