import os
while True:
    print('Select a number: ')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Exit')
    ch = input('Enter your choice: ')
    if ch == '1':
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        print(f'{a} + {b} is {a+b}')
    elif ch == '2': 
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        print(f'{a} - {b} is {a-b}')
    elif ch == '3': 
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        print(f'{a} * {b} is {a*b}')
    elif ch == '4':
        print('Exiting...')
        break
    else:
        print('Invalid choice')
    input('Press enter to continue...')
    os.system('cls')   