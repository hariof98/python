print('Hello ! Good Day')
employee = int(input('Enter your Employee Id > '))

condition = 0
total = 0
emp_list = [1, 2]


while condition < 5:
    condition += 1

    if employee not in emp_list:
        print('Employee Id does not exist..Please try again')
        employee = int(input('Enter your Employee Id > '))

    elif employee in emp_list:
      print(f'Hello {employee}')
      proceed = input('Press enter to continue (or) ` to exit >')


      while proceed != '`':
         item = [int(input('Enter the purchase amount > '))]

         for items in item:
             total += items
             print(total)

             if items == 0:
                print(f'Your total amount is: Rs.{total}')
                exit('Thanks for shopping with us!')
                # Objects that when printed, print a message like “Use quit() or Ctrl-D (i.e. EOF) to exit”, and when called, raise SystemExit with the specified exit code.

      print('We look forward to improve your shopping experience...Thank You!')
      exit()

exit('Please try again after some time...')






