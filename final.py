username = input('Введите имя пользователя: ')
title1 = input('Заголовок заметки: ')
while True:
    user_input = input('Ваша заметка о книге? (Да/Нет): ')
    if user_input.lower() == 'да':
        theme = input('Введите основную тему книги: ')
        characters = input('Кто основные персонажи? ')
        recommendations = input('Вы порекомендавали бы данную книгу для чтения? ')
        title2 = [theme, characters, recommendations]
        break
    elif user_input.lower() == 'нет':
        title2 = []
        break
    else:
        print('Неверный тип ответа')
content = input('Текст заметки: ')
status = input('Статус заметки: ')
created_date = input('Дата создания заметки в формате ДД.ММ.ГГГГ: ')
issue_date = input('Дата истечения заметки в формате ДД.ММ.ГГГГ: ')
note = [username, content, status, created_date[0:5], issue_date[0:5], [title1, title2]]
print (note)