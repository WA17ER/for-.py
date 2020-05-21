with open('new.txt', 'w') as file:
    while True:
        line = input('ВВедите строку: ')
        if line == '':
            break
        file.write(line + '\n')
