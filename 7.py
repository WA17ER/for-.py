from math import factorial


def fibo_gen(num):
    yield num + 1


count = 0
while count < 15:
    for el in fibo_gen(count):
        print(factorial(el))
        count += 1
