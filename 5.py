with open('5.txt', 'w') as file:
    value = input('Введите целые числа через пробел: ')
    file.write('Введенные числа: ' + value + '\n')
    value = map(int, value.split())
    sum_val = sum(value)
    file.write('Сумма чисел: ' + str(sum_val))
print('Сумма введенных чисел:', sum_val)
