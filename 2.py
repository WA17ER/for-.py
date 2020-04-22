time = int(input("Ведите время в секундах"))
sec = time % 60
min = time // 60
hour = time // 360
full_time = f'{hour}:{min}:{sec}'
print(full_time)
