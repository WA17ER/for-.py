spisok_tovarov = {
    'Фирма':('LG', 'Panasonic', 'Apple'),
    'тип товара': ('Ноутбук', 'Телефон', 'Смартфон'),
    'цена': (45000, 10000, 145000,),
    'кол-во': (7, 2, 6),
}
i=1
j=0
while i < 4:
     x = input("Назовите фирму ")
     y = input('Укажите тип товара ')
     z = int(input('Цена товара '))
     w = int(input('кол-во товара '))
     j = (i,{'Фирма':(spisok_tovarov['Фирма'][spisok_tovarov['Фирма'].index(x)]),
             'тип товара':(spisok_tovarov['тип товара'][spisok_tovarov['тип товара'].index(y)]),
             'цена':(spisok_tovarov['цена'][spisok_tovarov['цена'].index(z)]),
             'кол-во':(spisok_tovarov['кол-во'][spisok_tovarov['кол-во'].index(w)])
             })
     print(j)
     i += 1
