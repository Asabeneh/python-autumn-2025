from functools import reduce
from countries import countries

nums = [1, 2, 3, 4] # [1, 4, 9, 16]

""" new_nums = []
for num in nums:
    new_nums.append(num ** 2)

print(new_nums) """

""" new_list = list(map(lambda num: num **2, nums))
print(new_list)

even_nums = list(filter(lambda num: num % 2 == 0, nums))
print(even_nums)

total = reduce(lambda acc, cur: acc + cur, nums)
print(total)
 """

print([num ** 2 for num in nums])

countries_with_uppercase = [country.upper() for country in countries]
print(countries_with_uppercase)

country_codes = [country.upper()[:3] for country in countries]
print(country_codes)

def filter_countries_with_land(data):
    return [country for country in data if 'land' in country]

print(filter_countries_with_land(countries))
nums = [1, 2, 3]

print([num * 100 for num in nums])

lst = [[1, 2, 3],[4, 5, 6], [7, 8, 9]] # [1, 2, 3, 4, 5, 6, 7, 8,9]

flat_lst = []
for item in lst:
    for num in item:
        flat_lst.append(num)
print(flat_lst)

# print([num for item in lst for num in item])
print(lst[0])