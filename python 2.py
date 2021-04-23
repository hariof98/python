# Guessing Game
"""secret_number = 7
guess_count = 3
your_guess = 0

while your_guess < guess_count:
    guess = int(input('Guess:'))
    your_guess += 1
    if guess == secret_number:
        print('You have won')
        break
    elif your_guess > guess_count:
        print('Game Over')
        break
    else:
        print('oops try again!')
"""

# Car game
"""
user = 'hari@py.com'
passwords = 'hari'

command = input('email:')

if command == user:
 password = input('pass:')
 if password == passwords:
   print('Login Success')
   request = input('>').lower()

   while command and password:

     if request == 'start':
      print('The car has started successfully!')
      request = input('>').lower()

     elif request == 'stop':
      print('The car is stopped successfully!')
      request = input('>').lower()

     elif request == 'help':
      print('Start - To start the car')
      print('Stop - To stop the car')
      print('Quit - To abort the program')
      request = input('>').lower()

     elif request == 'quit':
      print('Program aborted!')
      break

     else:
      print("Sorry I didn't understand")
      request = input('>').lower()

 else:
  print('Password is incorrect!')

else:
 print("Email doesn't exist")
"""


# for loops
"""
for count in 'python':
 print(count)
 

# for loop in lists

for count in [1, 2, 3, 4, 5]:
 print(count)

for count in range(0, 100, 2):
 print(count)

"""
"""
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"The total is {total}")   ## 'f' is formatted string used to display dynamic values in output. print is defined outside of loop to avoid printing for each iterations.

"""

# nested for loop
"""
for x in range(4):
 for y in range(3):
  print(f'({x},{y})')
  
"""
"""
numbers = [5, 2, 5, 2, 2]
for num in numbers:
    if num == 5:
        print('*****')
    elif num == 2:
        print('**')
"""
"""
billing = str(input('>')).upper().lower()
condition = 0
total = 0

while billing == 'true' and condition < 5:
    list = [input('Enter your purchase amount >')]
    condition += 1

    for items in list:
        total += int(items)
print(total)
"""
