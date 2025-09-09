'''

Functions:
- Builtin Functions
- Custom Functions


'''



'''
print()
len()
abs()
min()
max()
sum()
round()
str()
float()
# bool()
list()
range()
input()

'''

# print function is a take a single or multiple input and it display

print(20)
print(20 * 10)
print('I love','Python', 2025, [1, 2, 3, 4, 5], {1, 2, 3}, (1, 2, 3), {'kirja':'book','talo':'house'})

# len() takes one input and give the lengh of the input
print(len('cat'))
print(len('Finland'))
print(len([1, 2, 3, 4, 5, 5])) # list
print(len({1, 2, 3})) # set
print(len({1, 2, 3, 3})) # set
print(len({'kirja':'book','talo':'house'}))

# 
print(abs(-10))
print(abs(-10) == 10)

print(min(10, -5, 9, 10, 20))
print(max(10, -5, 9, 10, 20))

print(sum([10, -5, 9, 10, 20]))

'''
Calculate the area of a circle:
area = pi * radius * radius
'''
print(3.14 * 8.55 * 8.55)
print(round(3.14 * 8.55 * 8.55))
print(round(3.14 * 8.55 * 8.55, 1))
print(round(3.14 * 8.55 * 8.55, 100))

print('python' + str(3))

print('I am ' + str(250) + ' years old.')

print( int('10') * 25)

print('9.81')
print(float('1.62') * 75)

# boolean: True or False

print(10 > 5)
print(len('cat') == len('dog'))

print(bool(1))
print(list())
print(list('abcdefghijklmnopqrstuvwxyz'))

print(list({1, 2, 3, 3}))


print(range(0, 11, 1))
print(list(range(0, 11, 1)))

print(list(range(100, 1001, 100)))

print(list(range(0, 101, 2)))

print(list(range(1, 101, 2)))

name = input('Enter name: ')
birth_year = input('When were you born? ')

current_year = 2025
age = current_year - int(birth_year)
print(f'You are {name}. You are {age} years old.')






