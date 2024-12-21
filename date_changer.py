while True:
    user_input = input('Дата создания заметки сегодня? (Да/Нет): ')
    if user_input.lower() == 'да':
        import datetime
        created_date = datetime.datetime.today()
        break
    elif user_input.lower() == 'нет':
        created_date = input('Введите дату создания в формате ДД-ММ-ГГГГ: ')
        break
    else:
        print('Неверный тип ответа')
issue_date = input('Введите дату истечения заметки в формате ДД-ММ-ГГГГ: ')
if user_input.lower() == 'да':
    print('Дата создания заметки: ', created_date.strftime('%d-%m'))
elif user_input.lower() == 'нет':
    print('Дата создания заметки:', created_date[0:5])
print('Дата истечения заметки:', issue_date[0:5])