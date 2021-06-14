# #FUNCTIONS
# def hello_python():
#     print('Hello world')
#     print('How are you?')
#
#
# print('Good Morning')  # after function definition leave 2 blank lines and continue (PEP 8: E305 expected 2 blank lines after class or function definition)
# hello_python()
# print('Thank You!')


# # Functions with parameters
# def hello_world(name):   # name is the parameter
#     print(f'Hello {name} ')
#     print('Welcome aboard')
#     print('Stay safe')
#
#
# print('Greetings')
# hello_world("Hari")    ## if you have a parameter you should pass a value to the parameter
# hello_world("Rahul")   ## Hari and Rahul are arguments.... Arguments and parameters are not the same.
# print('Thank You!')


# def hello_world(first_name, last_name):
#     print(f'Hello, {first_name} {last_name} ')
#     print(f'Hello, {last_name} {first_name} ')
#     print('Welcome aboard')
#     print('Stay safe')
#
#
# print('Greetings')
# hello_world("Hari", "Sridhar")  # these 2 arguments are called positional arguments
# hello_world(last_name="Sridhar", first_name="Hari")  # this is called keyword argument (It is used to improve the readability of the code,especially if we want to declare multiple numeric values.
#         ##"Always use positional arguments first and then keyword argument
# print('Thank You')

# #FUNCTION USING RETURN STATEMENTS
#      #By Default all functions in Python return None
#        #If we have a function that calculates something we can use return statement
#
# def calc_number(number):
#     return number * number
#
#
# #print(calc_number(3))
# answer = calc_number(int(input('Please enter a number to calculate: ')))
# print(answer)


#CALCULATOR

# def my_calc(num1, num2):
#     return num1 + num2
#
#
# print(my_calc(int(input('Enter a number to calculate: ')), int(input('Enter a number to calculate: '))))




