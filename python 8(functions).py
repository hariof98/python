# FUNCTIONS
# def hello_python():
#     print('Hello world')
#     print('How are you?')
#
#
# print('Good Morning')  # after function definition leave 2 blank lines and continue (PEP 8: E305 expected 2 blank lines after class or function definition)
# hello_python()
# print('Thank You!')


# Functions with parameters
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


def hello_world(first_name, last_name):
    print(f'Hello, {first_name} {last_name} ')
    print('Welcome aboard')
    print('Stay safe')


print('Greetings')
hello_world("Hari", "Sridhar")  # these 2 arguments are called positional arguments
print('Thank You!')