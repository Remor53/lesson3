from datetime import datetime, timedelta

if __name__ == '__main__':
    # Вывод в консоль даты: вчера, сегодня, месяц назад
    today = datetime.now()
    delta1 = timedelta(days=1)
    if int(today.strftime('%m')) in [5, 7, 10, 12]:
        delta2 = timedelta(days=30)
    elif int(today.strftime('%m')) == 3:
        if int(today.strftime('%Y')) % 4 == 0:
            delta2 = timedelta(days=29)
        else:
            delta2 = timedelta(days=28)
    else:
        delta2 = timedelta(days=31)
    print('Сегодня -', today.strftime('%d/%m/%Y'))
    print('Вчера -', (today - delta1).strftime('%d/%m/%Y'))
    print('Месяц назад -', (today - delta2).strftime('%d/%m/%Y'))
    # Превращение строки "01/01/17 12:10:03.234567" в объект datetime
    string = '01/01/17 12:10:03.234567'
    print('\nДанная строка -', string)
    print('Ееё тип -', type(string))
    obj = datetime.strptime(string, '%d/%m/%y %H:%M:%S.%f')
    print('Объект -', obj)
    print('Тип объекта -', type(obj))
