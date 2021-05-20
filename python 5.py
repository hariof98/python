# DICTIONARIES
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
"""
customer = {
    'name': 'Hari',
    'age': 22,
    'is_verified': True  #boolean value
}
#customer['name'] = 'Hrishi'
print(customer.get('name'))
#print(customer['dob'])  # simply printing the variable throws keypair error in dictionaries if the variable is not available,
#so we are using .get() function to print the output
print(customer.get('dob'))
print(customer.get('dob', '12-11-1998'))

print(customer)

"""
#abc = '45'
#print(type(abc))

"""
phone = input('Phone > ')

dictionary = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}
output = ''
for num in phone:
    if num > '4':
        print('That may be beyond my abilities!')
    else:
     output += dictionary.get(num)
print(output)
"""