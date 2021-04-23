"""
abc = input("Enter the company name >")
print(f"Your company name is: {abc}")
"""

# lists ***
"""
names = ['hari', 'hrishi', 'rahul', 'usha', 'balaji', 'sri']
names[0] = 'HARI'
print(names)
print(names[1])
print(names[1:])
print(names[1:5])

"""
#SIMPLE WAY TO FIND LARGEST AND SMALLEST NUMBER IN A LIST
"""
num = [3, 4, 7, 10, 19, 5]
print(max(num))
print(min(num))

numbers = [3, 6, 1, 7, 12, 15, 8]
max = 0

for number in numbers:
    if number > max:
       max = number

print(max)

"""
#2D LISTS

matrix = [
           1, 2, 3,
           4, 5, 6,
           7, 8, 9,
         ]

for row in matrix:
    #print(row)
    qwe = int(input('>'))
    print(matrix.index(qwe))

