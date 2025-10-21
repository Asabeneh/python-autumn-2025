
""" try:
    birth_year  = input('Birth year: ') # string
    print(type(birth_year))
    current_year = 2025  # int
    age = current_year - int(birth_year) # TypeError
    print(age)
except:
    print('Something goes wrong')
else:
    print('I work if the try works')
finally:
    print('No matter what i will be printed out')
 """

# try:
#     print(10 + '5')
# except:
#     print('Something went wrong')

""" try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    current_year = 2025
    age = current_year - year_born
    print(f'You are {name}. And your age is {age}.')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
except SyntaxError:
    print('Syntax Error')
except KeyError:
    print('A key error')
except TypeError:
    print('Type error occured') """
    
    
try:
    # name = input('Enter your name:')
    # year_born = input('Year you were born:')
    # current_year = 2025
    # age = current_year - year_born
    # print(f'You are {name}. And your age is {age}.')
    # print([1, 2,3][4])
    print(name)
except Exception as e:
    print('Error: ', e)

