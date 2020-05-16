from itertools import count
from itertools import cycle

for step in count(0, 60):
    if step > 1000:
        break
    else:
        print(step)

gen = 0

for data in cycle("Рандоиная строка"):
    if gen > 60:
        break
    print(data)
    gen += 1
