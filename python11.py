class MyClass:
    def largest_num(self):
        numbers = [2, 3, 100, 4, 500, 1]
        max = 0

        for num in numbers:
            if num > max:
                max = num
        print(max)


num = MyClass()
num.largest_num()