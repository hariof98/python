#CALCULATOR

choose = input('Press Enter to Continue > ')
condition = 0
result = 0

while choose == '':
 calc = [int(input('Enter the number: '))]
 operation = input('> ')
 if operation == '+':
      for ans in calc:
       result += ans
       print(result)

 elif operation == '-':
      for ans in calc:
         result -= ans
         print(result)

 elif operation == '*':
      for ans in calc:
         result *= ans
         print(result)

 elif operation == '/':
      for ans in calc:
         result /= ans
         print(result)

exit('Thank You!')