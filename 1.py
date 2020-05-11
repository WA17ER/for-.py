def delenie(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        print('Деление на 0')


chasnoe = delenie(int(input("Введите делимое")), int(input('Введите дилитель')))
print(chasnoe)
