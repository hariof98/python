from datetime import date
from datetime import time

message = input('> ')

if message:
    print('Login to access me')
    login = input('Login: ')

    if login == '':
        print(f'Welcome {login}')

        request = input('>> ')

        today = date.today()

        if request == '```':
            print(f'Hello Hari...Today is {today}')
        else:
            print('bye')