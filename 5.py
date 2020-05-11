def new_func(some_str):
    if some_str == '$':
        return '$'
    else:
        my_list = some_str.split()
        var_1 = 0
        for var in my_list:
            if var == "$":
                break
            else:
                var_1 += int(var)
    return var_1



Total = 0
while True:
    tolta1 = new_func(input('Введите чмсла через пробел  \n или $ чтобы прервать'))
    if tolta1 == "$":
        break
    else :
        Total += tolta1
    print(Total)
