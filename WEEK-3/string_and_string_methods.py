'''
String and String meths:

.lower()
.upper()
.title()
.index()
.find()
.starswith()
.endswith
'''
pet = 'cat'
print(len(pet))
print(pet[0])
print(pet[1])
print(pet[2])
last_index = len(pet) - 1
print(pet[last_index])
print(pet[-1])
print(pet[-2])
print(pet[-3])

country = 'Finland'
print(country[0:3])
print(country[:3])

print(country[3:])
print(country[3:7])
print(country[3:6])

print(country[-7:-4])

# String concatenation

first_name = 'Asab'
last_name = 'Yeta'
age = 250
country = 'Finland'
fullname = first_name + ' ' +  last_name
height = 1.73089

print(f'I am {fullname}. I live in {country}. I am {age} years old.')
print('I am {}. I live in {}. I am {} years old.'.format(fullname, country, age))
print('I am {1}. I live in {2}. I am {0} years old.'.format(fullname, country, age))
print('I am {}. I live in {}. I am {} years old. I am {:.2f} meter tall.'.format(fullname, country, age, height))
print('I am %s. I live in %s. I am %d years old. I am %.2f meter tall.' %(fullname, country, age, height))






