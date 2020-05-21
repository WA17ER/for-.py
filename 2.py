with open('new.txt') as file:
    lines = file.readlines()
    print('Количество строк:', len(lines))
    for num_line, line in enumerate(lines, start=1):
        print(f'{num_line} строка содержит - {len(line.split())} слов')
