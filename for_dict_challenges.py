# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
names = {}
for student in students:
    names[student['first_name']] = names.get(student['first_name'], 0) + 1

for k,v in sorted(names.items()):
    print('{}: {}'.format(k, v))


# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
names = {}
for student in students:
    names[student['first_name']] = names.get(student['first_name'], 0) + 1

max_count = max(names.values())
name = [k for k, v in names.items() if v == max_count]
print('Самое частое имя среди учеников: {}'.format(*name))


# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
i = 1
for c in school_students:
    students_name = {}
    print(f"Самое частое имя в классе {i}: ", end="")
    i += 1
    answer=None
    for x in c:
        students_name[x['first_name']] = c.count(x)
    for y, num in students_name.items():
        if answer is None:
            answer = y
        if students_name[answer] < num:
            answer = y
    print(answer)
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for x in school:
    male = 0
    female = 0
    for y in x['students']:
        if is_male.get(y['first_name']) is False:
            female += 1
        else:
            male += 1
    print(f"В классе {x['class']}: {female} девочки и {male} мальчика")

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for x in school:
    male = 0
    female = 0
    for y in x['students']:
        if is_male.get(y['first_name']) is False:
            female += 1
        else:
            male += 1
    
    print(f"В классе {x['class']}: {female} девочки и {male} мальчика")

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a