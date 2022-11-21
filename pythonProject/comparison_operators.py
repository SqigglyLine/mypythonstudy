name = input('What is your name?')
if len(name) < 3:
    print('Your name, ' + name + ' must be at least 3 characters')
elif len(name) > 50:
    print('Your name, ' + name + ' must be a maximum of 50 characters')
else:
    print('Thats a nice name! :)')