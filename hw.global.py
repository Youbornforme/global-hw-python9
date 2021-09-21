#1. Создать словарь оценок по приведенной таблице, для вас и ваших одногрупников.
#Ключ - ФИ, значение - вложенный словарь тема -> значение.
#2. Вывести среднюю оценку каждого студента.
#3. Вывести название самой проблемной темы.
#4. Вывести самого неуспевающего студента.


from random import randint

stud = {
    'Godunov Nikita': {'shema' : 4, 'fb' : 5, 'fb+' : 6, 'practice' : 10, 'string' : 0, 'dict' : 0, 'git1' : 6,
                    'practice 2': 10, 'module' : 10, 'psql' : 0, 'psql module' : 0},
    'Hoptarev Denys': {'shema' : 6, 'fb' : 10, 'fb+' : 0, 'practice' : 10, 'string' : 0, 'dict' : 0, 'git1' : 0,
    'practice 2' : 10, 'module' : 10, 'psql' : 0, 'psql module' : 10},
    'Kalchenko Vladyslav': {'shema' : 7, 'fb' : 6, 'fb+' : 8, 'practice' : 10, 'string' : 0, 'dict' : 0, 'git1' : 8,
    'practice 2' : 10, 'module' : 10, 'psql' : 0, 'psql module' : 10},
    'Dzyadsuh Yurui': {'shema' : 7, 'fb' : 8, 'fb+' : 8, 'practice' : 10, 'string' : 0, 'dict' : 0, 'git1' : 8,
    'practice 2' : 10, 'module' : 10, 'psql' : 0, 'psql module' : 10},
    'Lisickiy Vladymir': {'shema' : 7, 'fb' : 10, 'fb+' : 8, 'practice' : 10, 'string' : 8, 'dict' : 8, 'git1' : 8,
    'practice 2' : 10, 'module' : 10, 'psql' : 0, 'psql module' : 10},
    'Savchenko Vladymir': {'shema' : 8, 'fb' : 10, 'fb+' : 9, 'practice' : 10, 'string' : 8, 'dict' : 8, 'git1' : 8,
    'practice 2' : 10, 'module' : 10, 'psql' : 0, 'psql module' : 10},
    'Trofimchuk Vladymir': {'shema' : 8, 'fb' : 10, 'fb+' : 10, 'practice' : 10, 'string' : 9, 'dict' : 10, 'git1' : 8,
    'practice 2' : 10, 'module' : 10, 'psql' : 10, 'psql module' : 10},
    'Korshunov Dmytiy': {'shema' : 7, 'fb' : 10, 'fb+' : 10, 'practice' : 10, 'string' : 10, 'dict' : 10, 'git1' : 10,
    'practice 2' : 10, 'module' : 10, 'psql' : 10, 'psql module' : 10},
}
for student in stud:
    s = 0
    for dist in stud[student]:
        s += stud[student][dist]
    s = s / len(stud[student])
    print(f"Student: {student}. Average rating: {s}")
    if s < 6:
        print(f"Not a successful student: {student} Grade: {int(s)}")
    print(f"Student: {student}. Avarage rating: {int(s)}")
    for dist, values in stud[student].items():
        if values < 5:
            print(f"Student: {student} Problematic topic:{dist}")
