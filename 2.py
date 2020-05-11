def user_data(name, last_name, year_birth, city, email, phone):
    print(f'Имя-{name}, Фамилия-{last_name}, дата рождения-{year_birth}, Город-{city}, '
          f'электронная почта{email}, номер телефона{phone}')


user_data(input('Укажите имя '), input('Укажите Фамилию '), int(input('год рождения ')), input('Город проживания '),
          input('адрес электронной почты '), int(input('Номер телефона ')))
