'''
Variables are containers, they store data
- Python variable should be lowercase
- If it is from compound words, it should have underscore(first_name)
- It cannot start with number(1num)
- It can have numbers(num1, year1)
- Sometimes if we want to use reserved words as a varible, we use _ at the front(_if)
'''
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
mass = 76.5
height = 172.5
is_married = True 
skills = ['HTML', 'Python','Go','Pandas']
shopping_list = ['Milk', 'Potatos','Mango','Meat','Honey'] # list -  modifiable/mutable
tpl = ('Asabeneh', True, 250) # Tuple - unmodifiable/immutable
st = {'Finnish','Finnish','Swedish','Swedish','English','English','French'}
# Dictionary allows to organize data
user = {
    'first_name':'Asabeneh',
    'username':'asabeneh',
    'password':'123123',
    'created_at':'09/09/2025 19:22',
    'logged_in':False
}


fullname = first_name + ' '+ last_name

print(fullname)

# type 

print(type(first_name))
print(type(age))
print(type(height))
print(type(skills))
print(type(tpl))
print(type(st))
print(type(user))

'''
Numbers(int, float, complex)
String
Booleans (True or False)
List
Set
Tuple
Dictionary
'''

names = ['Emily','Kaapo','Beata']

value = 1 + 4j
print('Complex number:- ', 'value:', value, 'type:', type(value))



txt = '''
Python is a high-level programming language for general-purpose programming. It is an open source, interpreted, objected-oriented programming language. Python was created by a Dutch programmer, Guido van Rossum. The name of the Python programming language was derived from a British sketch comedy series, Monty Python's Flying Circus. The first version was released on February 20, 1991. This 30 days of Python challenge will help you learn the latest version of Python, Python 3 step by step. The topics are broken down into 30 days, where each day contains several topics with easy-to-understand explanations, real-world examples, and many hands on exercises and projects.

This challenge is designed for beginners and professionals who want to learn python programming language. It may take 30 to 100 days to complete the challenge. People who actively participate in the telegram group have a high probability of completing the challenge.

'''

'''

Between (2, 3) and (10, 8)

'''
x1 = 2
x2 = 3

y1 = 10
y2 = 8

d = ((y1 - x1) ** 2 + (y2 - x2) ** 2) ** 0.5
print(' The Euclidian distance between (2, 3) and (10, 8) is', round(d, 2))