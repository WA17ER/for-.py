from sys import argv

hour, rate, bonus = argv[1:]
result = int(hour) * int(rate) + float(bonus)
print(result)