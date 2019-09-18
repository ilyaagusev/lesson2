# задание 1 - вывести список чисел увеличив каждое на единицу


integer_list = [3, 5, 8, 2, 8, 13, 37, 90, 12, 14]
for integer in integer_list:
    integer += 1
    print(integer)


# задание 2 - дать пользователю ввести предложение и вывести каждое слово
# отдельной строкой

sentence = input('Введите предложение из нескольких слов: ')
for word in sentence.split(" "):
    print(word)


# Создать список из словарей с оценками учеников разных классов школы
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

school = [
    {'school_class': '5a', 'scores': [5, 4, 4, 2, 5]},
    {'school_class': '5b', 'scores': [4, 3, 2, 3, 3]},
    {'school_class': '5c', 'scores': [4, 4, 5, 5, 5]},
]


averege_class_scores = []


for school_classes in school:
    averege_score = sum(school_classes['scores']) / len(
        school_classes['scores'])
    averege_class_scores.append(averege_score)
    print('Средний балл по классу {0} - {1}.'.format(
        school_classes['school_class'], averege_score))


averege_school_score = sum(averege_class_scores) / len(averege_class_scores)
print('Средний балл по школе - {}.'.format(round(averege_school_score, 1)))
