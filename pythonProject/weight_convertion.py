weight = input('Please enter your weight: ')
unit = input('Is it in (K)g or (L)bs: ')
weight = float(weight)
if unit == 'K' or unit == 'k':
    weight = weight * 2.205
    print(f'Your weight in pounds is {weight}lbs')
else:
    weight = weight * 0.453592
    print(f'Your weight in kilograms is {weight}kg')
