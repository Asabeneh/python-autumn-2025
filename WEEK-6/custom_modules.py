def do_something(activity):
    return f'I am {activity}'
    
def add_two_nums(a, b):
    return a + b

def calculate_weight(mass, gravity = 9.81):
    return mass * gravity


def add_numbers(*args):
    return sum(args)
   
def print_country_info(name, capital, population, language):
    print('before the something before the return')
    return f'Country:{name}, capital:{capital}, population:{population}, language:{language}.'


def kwargs_sample_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


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