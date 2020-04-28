a = input('Ведите несколько слов ')
p = 0
for i in a.split():
    print(f'{p}) {i[:10]}')
    p += 1



