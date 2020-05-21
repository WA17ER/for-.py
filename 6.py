lesson ={}
with open('6.txt') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split()
        subject = data[0]
        sum_lessons = sum([int(x[:x.find('(')]) for x in data[1:] if '(' in x])
        lesson[subject] = sum_lessons
print(lesson)