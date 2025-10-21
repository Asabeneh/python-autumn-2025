def do_something(activity):
    print(f'I am {activity}')
    
    
do_something('teaching')
do_something('learning')
do_something('running')

# def add_two_nums(a, b):
#     total = a + b
#     return total

def add_two_nums(a, b):
    return a + b


    
print(add_two_nums(1, 9))
print(add_two_nums(10, 90))
print(add_two_nums(-1, -9))

def calculate_weight(mass, gravity = 9.81):
    return mass * gravity

print(calculate_weight(75))
print(calculate_weight(75, 1.62))


""" def add_numbers(*args):
    total = 0 
    for num in args:
        total = total + num
    return total """

def add_numbers(*args):
    sum(args)
   


print(add_numbers(1, 2, 3, -4, 10))
print(add_numbers(100, 200, 300))


def print_country_info(name, capital, population, language):
    print('before the something before the return')
    return f'Country:{name}, capital:{capital}, population:{population}, language:{language}.'

    
    
print(print_country_info('Finland', 'Helsinki', '6M','Finnish'))
print(print_country_info(population='6M', capital='Helsinki', name='Finland', language='Finnish'))
    
print(print_country_info('China', 'Beijing', '1.2B','Chinese'))

# After break, let us get about at 18: 46
""" def kwargs_sample_function(**kwargs):
    for key in kwargs:
        print(key, kwargs[key]) """
        
        
""" def kwargs_sample_function(**kwargs):
    for item in kwargs.items():
        print(item[0], item[1]) """

def kwargs_sample_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


kwargs_sample_function(name='Asab', country='Finland', city='Helsinki', age = 50, height = 1.73, skills = ['Python', 'MySQL','Node','ML'])