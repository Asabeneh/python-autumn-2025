# Conditionals
'''
We make decison based on some conditions.
'''
# Integer: - Negative, Zero, Positive
""" number = int(input('What is the number? '))
if type(number) == int:
    if number > 0:
        print(f'{number} is a positive number')
    elif number == 0:
        print(f'{number} is zero')
    elif number < 0:
        print(f'{number} is a negative number')
    else:
        print('Unknow')
else:
    print('This is not a number') """


weather = input('What is today weather like? ').lower()
if weather == 'rainy':
    print('Go with a raincoat or umbrella')
elif weather == 'cloudy':
    print('It may rain')
elif weather == 'sunny':
    print('Go out freely')
elif weather == 'snowy':
    print('Be careful, it might be slippery')
elif weather == 'foggy':
    print('There might be visibility problem')
else:
    print('No one knows today weather')

