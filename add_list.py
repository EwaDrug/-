username = input('Введите имя пользователя: ')
title = input('Заголовок заметки: ')
while True:
    user_input = input('Ваша заметка о книге? (Да/Нет): ')
    if user_input.lower() == 'да':
        theme = input('Введите основную тему книги: ')
        characters = input('Кто основные персонажи? ')
        recommendations = input('Вы порекомендавали бы данную книгу для чтения? ')
        title2 = ["Тема книги:", theme, "Основные персонажи:", characters, "Рекомендации для чтения:", recommendations]
        break
    elif user_input.lower() == 'нет':
        break
    else:
        print('Неверный тип ответа')
content = input('Текст заметки: ')
status = input('Статус заметки: ')
created_date = input('Дата создания заметки в формате ДД-ММ-ГГГГ: ')
issue_date = input('Дата истечения заметки в формате ДД-ММ-ГГГГ: ')
print('Имя пользователя:', username)
print('Заголовок заметки:', title)
if user_input.lower() == 'да':
    print(title2)
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', created_date[0:5])
print('Дата истечения заметки:', issue_date[0:5])