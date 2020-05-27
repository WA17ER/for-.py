target = int(input('Укажите цель : '))
start = int(input('первый результат : '))
day = 1

while start < target:
    start += start/10
    day += 1
print(f'Цель будет достигнута на {day} день')