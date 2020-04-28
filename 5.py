a = [9, 6, 2, 1, ]
i = int(input("Введите число: "))
g = [i, ]
x = 0

if i in a:
    a.insert((a.index(i)+1), i)
else:
    for u in a:
        if g[x] < u > i:
            g.insert(x, u)
            x += 1
        elif g[x] >= u <= i:
            g.insert(x+1, u)
            x += 1

    a = g
print(a)

# через sort

a.append(i)
a.sort()
a.reverse()
print(a)
