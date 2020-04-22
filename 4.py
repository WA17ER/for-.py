a = int(input('Ведите число '))
b = 0

while a // 10 > 0:
    if b > a % 10 and b > (a // 10) % 10:
        b = b
    elif b < a % 10 and (a % 10) > (a // 10) % 10:
        b = a % 10
    elif (a % 10) // 10 > (a // 10):
        b = (a // 10) % 10
    a //= 10
print(b)
