with open('eng.txt', encoding='Windows-1251') as file:
     lines = file.readlines()
print(lines)


with open('translate.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        file.write(line)
