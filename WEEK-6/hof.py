'''
Higher order function: function that return another function or takes a function as a parameter

'''
""" 
def hof_1(func):
    pass 



def hof_2():
    def func ():
        pass 
    
    return func
 """

def make_square(n):
    return n * n


print(make_square(10))


def make_cub(func, n):
    return func(n) * n


print(make_cub(make_square, 10))


""" def do_math(n):
    def add_ten():
        return n + 10
    return add_ten

print(do_math(99)()) """


def do_math(a, b):
    def add():
        return a + b
    def multiply():
        return a * b 
    def subtract():
        return a - b 
    def division():
        return a / b
    return {
        'add':add,
         'multiply':multiply,
         'subtract':subtract,
         'division':division
    }
    
print(do_math(11, 9)['multiply']())



