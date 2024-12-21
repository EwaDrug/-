import datetime
created_date = datetime.datetime.today()
print('Дата создания заметки: ', created_date.strftime('%d-%m'))

issue_date = input('Введите дату истечения заметки в формате ДД-ММ-ГГГГ: ')
print('Дата истечения заметки:', issue_date[0:5])