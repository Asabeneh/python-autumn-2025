'''
List is a set of items  which are indexed order and can be mutated or modified'
'''
empty_list = [] 
print(type(empty_list), len(empty_list))
nums = [1, 2, 3, 4, 5]
print(nums)
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])

last_index = len(nums) - 1
print(nums[last_index])
print(nums[1:4])
print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])
print(nums[-5])
print(nums[-4:-1])
print(nums)

for num in nums:
    print(num, num ** 2, num ** 3)
    
# print(nums)

# print(list(range(10, 101, 10)))
# print(list(range(100, 1001, 100)))
# print(list(range(0, 101, 5)))

# tens = range(10, 101, 10)
# for num in tens:
#     print(num)

""" items = ['Milk', 'Tomato','Coffee','Honey','Sugar','Tea','Cheese']
for item in items:
    if item!='Coffee':
        print(item, item.upper())
        
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
for company in it_companies:
    if company != 'IBM':
        print(company, company.upper()) """
        
        
        
items = ['Milk', 'Tomato','Coffee']
items.append('Honey')
print(items)
items.append('Bread')
print(items)
items.extend(['Avocado','Banana','Apple'])
print(items)
items.insert(4, 'Sugar')

print(items)
items.pop(3)
print(items)
items.remove('Banana')
print(items)
countries =  ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
print('Finland' in countries)
print('Avocado' in items)
countries[0] = 'Nomanland'
print(countries)
countries[-1] = 'Norman'

print(countries)

new_countries = []
for i in range(len(countries)):
    country = '#' +  countries[i]
    new_countries.append(country)
    
print(new_countries)

print(items)
items[3] = 'Honey'
print(items)
print(items)

print(items)
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[3:]
print(fruits)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print(nums1 + nums2)

# nums1.extend(nums2)
# print(nums1)
# nums2.extend(nums1)
# print(nums2)
nums2_backup = nums2.copy()

nums2.append(500)
print(nums2)
print(nums2_backup)

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
words = ['i', 'love', 'people', 'if', 'you', 'do', 'not', 'love', 'people', 'what', 'else', 'do', 'you', 'love']
print(words.count('love'), words.count('people'))
print(words.index('love'))

list_methods = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
list_methods.reverse()

print(list_methods)
countries.reverse()
print(countries)

countries =  ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway','Iceland']
countries_copy = countries.copy()

""" countries_copy.reverse()
print('original:', countries)
print('reversed:', countries_copy) """

countries_copy.sort(reverse=False)
print('original:', countries)
print('sorted:', countries_copy) 








