print('Welcome to driving simulator! Please take these keys 🔑 and start!')
print("Type 'help' if you need the instructions!")
car = '🚘'
stopped = True
while True:
    instruction = input(f'{car}').lower()
    if instruction == 'help':
        print("""To drive forward the car type 'go'
To stop the car type 'stop'
To exit the car type 'quit'
""")
    elif instruction == 'go':
        if stopped:
            stopped = False
            print('Starting!')
        else:
            car = '  ' + car
            print('*Vroom!💨')
    elif instruction == 'quit':
        print('Have a nice day!')
        break
    elif instruction == 'stop':
        car = car
        if not stopped:
            stopped = True
            print('Stopping!')
        else:
            print('The car already stopped!')

    else:
        print("Sorry, I don't understand that...")
print('Thank you for driving with us! Come again soon!')