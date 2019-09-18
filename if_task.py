# задание 1 - определить возрастную группу по числу полных лет.


def age_group(users_age):
    if 0 <= users_age <= 6:
        return 'детский сад'
    elif 7 <= users_age <= 17:
        return 'школа'
    elif 18 <= users_age <= 23:
        return 'институт'
    elif 24 <= users_age <= 100:
        return 'работа'
    elif 0 > users_age or users_age > 100:
        return 'Что-то не так с вашим возрастом'


users_age = int(input('Введите ваш возраст (полных лет): '))
print(age_group(users_age))

# задание 2 - сравнить строки на основании их типов и значения


def string_checker(string_one, string_two):
    if type(string_one) != str or type(string_two) != str:
        return 0
    elif string_one == string_two:
        return 1
    elif len(string_one) > len(string_two) and string_two != 'learn':
        return 2
    elif string_one != string_two and string_two == 'learn':
        return 3
    else:
        pass


print(string_checker(1, 'asdf'))
print(string_checker('qwerty', 'qwerty'))
print(string_checker('qwerty', 'asdf'))
print(string_checker('asdf', 'learn'))
