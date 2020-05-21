with open('zp.txt') as file:
    total = []
    lines = file.readlines()
    for line in lines:
        name, zp = line.split(' - ')
        total.append(int(zp))
        if int(zp) < 20000:
            print(line, end='')
    print('\nСредняя зп:', sum(total) / len(total))