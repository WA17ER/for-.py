a = []
l = int(input('Введите число '))
i = 0

while len(a) < l:
    b = input('введите значение')
    a.append(b)
if l // 2 == 0:
    while i < len(a):
        a[i], a[i + 1] = a[i + 1], a[i]
        i += 2
else:
    while i < len(a) - 1:
        a[i], a[i + 1] = a[i + 1], a[i]
        i += 2
print(a)
