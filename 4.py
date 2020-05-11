# через **
def result1(var_1, stepen):
    return var_1 ** stepen


# через цикл
def result2(var_2, stepen_2):
    if stepen_2 == 0:
        return 1
    elif stepen_2 > 0:
        x = var_2
        for a in range(1,stepen_2) :
            x *= var_2
        return x
    else:
        y = abs(stepen_2)
        x = var_2
        for a in range(1, y):
            x *= var_2
        return 1/x


frst = result1(int(input('введите число :')), int(input("Укажите степень ")))
scnd = result2(int(input('введите число :')), int(input("Укажите степень ")))
print(f'Результат первого действия {frst}. Результат второго {scnd}')
