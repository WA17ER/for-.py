pribyl = int(input('введите прибыль фирмы '))
izderjki = int(input('Укажите издержки'))
workers = int(input('укажите число сотрудников'))
profit = pribyl - izderjki
profit_at_workers = profit / workers

if profit > 0 :
    print(f'Фирма отработала с выгодой {profit}.Рентабильность сотавила {profit/pribyl} . Доход на каждого работника {profit_at_workers}')
elif profit < 0 :
    print(f"фирма понесла убытки {profit}")
else :
    print('фирма не получила дохода ,но и не понесла убытков')
