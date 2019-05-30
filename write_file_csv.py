import csv

user_for_csv = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('export.csv', 'w', encoding='utf-8', newline='') as file:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(file, fields, delimiter=';')
    writer.writeheader()
    for user in user_for_csv:
        writer.writerow(user)