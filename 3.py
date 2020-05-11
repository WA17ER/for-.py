def my_func(var_1, var_2, var_3):
    list_var = [var_1, var_2, var_3]
    max1 = max(list_var)
    list_var.remove(max1)
    return max(list_var) + max1


a = my_func(int(input('Первое число :')), int(input('Второе число :')), int(input('Третье число')))
print(f'сумма двух наибольших чиссел равна {a}')
