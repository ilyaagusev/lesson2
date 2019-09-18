# задание 1 - функция ask_user() которая отвечает пользователю, пока он не
# напишет слово "пока".


dialog_dictionary = {
    'привет': 'Рад встрече!',
    'как дела?': 'Потихоньку.',
    'что делаешь?': 'Учусь.',
    'есть новости?': 'Все по старому',
    'как настроение?': 'Боевое!',
    'как погода?': 'Осень.',
}


def ask_user():
    while True:
        user_answer = input('Пользователь: ')
        if user_answer in dialog_dictionary:
            print('Программа: {}'.format(dialog_dictionary[user_answer]))
        elif user_answer == 'пока':
            print('Пока!')
            break
        else:
            print('Программа: Не понял.')


ask_user()
