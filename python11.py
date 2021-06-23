# class MyClass:
#     def largest_num(self):
#         numbers = [2, 3, 100, 4, 500, 1]
#         max = 0
#
#         for nums in numbers:
#             if nums > max:
#                 max = nums
#         print(max)
#
#
# num = MyClass()
# num.largest_num()
#


def find_me(numbers):
    max = 0

    for items in numbers:
        if items > max:
            max = items
    print(max)