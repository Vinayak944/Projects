started = False
while True:
    option = input('>').lower()
    if option == 'start':
        if started:
            print('Car already started!')
        else:
            print('Car started... Ready to go!')
            started = True
    elif option == 'stop':
        if not started:
            print('Car already stopped!')
        else:
            print('Car Stopped!')
            started = False
    elif option == 'help':
        print('''
Start - to start the car
Stop - to stop the car
quit - to exit
''')
    elif option == 'quit':
        break
    else:
        print("I don't understand the command")



