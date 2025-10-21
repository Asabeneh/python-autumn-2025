'''

map, filter, reduce

[1, 2, 3] => [1, 4, 9]
['Finland', 'Sweden', 'Norway'] => ['Helsinki', 'Stockholm', 'Oslo']

'''
nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]

""" def mapper(lst):
    new_lst = []
    for num in lst:
        new_lst.append(num * 100)
    return new_lst

print(mapper(nums))
 """
from countries_data import data
from pprint import pprint

# new_list = list( map(lambda country: {'name':country['name'], 'flag':country['flag']}, data))
# pprint(new_list)

# countries_code = list( map(lambda country: country['name'].upper()[:3], data))
# pprint(countries_code)


""" country_list = []
for country in data:
    country_list.append(country['name'].upper()[:3])
print(country_list) """

""" populations = []
for country in data:
    populations.append(country['population'])
print(populations) """

""" def xyz(country):
    return country['population']

populations = list(map(xyz, data))
print(populations) """

""" xyz = lambda country: country['population']

populations = list(map(xyz, data))
print(populations) """


# populations = list(map(lambda country: country['population'], data))
# print(populations)

# Filter => 

""" nums = [1, 2, -3, 4, 6, 0, 8]

def get_even_nums(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

def get_odd_nums(lst):
    odds = []
    for num in lst:
        if num % 2 != 0:
            odds.append(num)
    return odds

print(get_even_nums(nums))
print(get_odd_nums(nums))

for country in data:
    if 'land' in country['name']:
        print(country['name']) """

nums = [1, 2, -3, 4, 6, 0, 8]
evens = list(filter(lambda num: num % 2 == 0, nums))
odds = list(filter(lambda num: num % 2 != 0, nums))
print(evens)
print(odds)
countries_with_land  = list(filter(lambda country: 'land' in country['name'], data))
print(list(map(lambda country: country['name'], countries_with_land)))

# Reduce -> 
from functools import reduce

print(reduce(lambda acc, cur: acc + cur, nums))

total = 0 
for num in nums:
    total = total + num 
    
print(total)

world_population = reduce(lambda acc, cur: acc + cur['population'], data, 0)
print(world_population)