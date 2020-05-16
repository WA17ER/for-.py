from functools import reduce


def func1(num1, num2):
    return num1 * num2


result = [el for el in range(10, 101, 10)]
print(reduce(func1, result))

#Указанные в дз числа

result = [el for el in range(100, 1001, 2)]
print(reduce(func1, result))