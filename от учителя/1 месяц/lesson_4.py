word = input('word: ')

new = word.split()

print(new)

# ratings = []
#
# c = 0
#
# while c != 3:
#     name = input('Enter name: ')
#     rate = int(input(f'Rate {name}'))
#     ratings.append(dict(name=name, rate=rate))
#     c += 1
#     for i in ratings:
#         print(i)
#
# for i in ratings:
#     print(i)

# numbers = [20, 50, 100, 200]
# people = ['Т. Молдо', "К. Датка", "Т. Сатылганов", "А. Осмонов"]
#
# new_dict = dict(zip(numbers, people))
# print(new_dict)

# dict_som = {}
#
# c = 0
#
# while c != len(numbers):
#     dict_som[numbers[c]] = people[c]
#     c += 1
#
# for n, p in new_dict.items():
#     print(f'{n}: {p}')

# data = [
#     {'name': 'Adilet', 'hws': 51, 'StandUp': 5, 'test': 65},
#     {'name': 'Zarina', 'hws': 58, 'StandUp': 7, 'test': 75},
#     {'name': 'Bektur', 'hws': 75, 'StandUp': 6, 'test': 80},
#     {'name': 'Madina', 'hws': 75, 'StandUp': 8, 'test': 90},
#     {'name': 'Elina', 'hws': 80, 'StandUp': 8, 'test': 100},
# ]
#
#
# for i in data:
#     if i['hws'] >= 50 and i['hws'] <= 60 and i['StandUp'] < 6 and i['test'] >= 60:
#         i['discount'] = 1000
#     elif i['hws'] >= 50 and i['hws'] <= 60 and i['StandUp'] >= 6 and i['test'] >= 60:
#         # i['discount'] = 2000
#         i.update(dict(discount=2000))
#
# for i in data:
#     print(i)


# numbers = [1, 2, 3, 2, 4, 1]
# set_numbers = {1, 2, 3, 2, 4, 1}
#
# print(numbers)
# print(set_numbers)

# lagman = {'лапша', "мясо", "перец"}
# beshbarmak = {'лапша', "мясо", "лук"}
#
# print(lagman.intersection(beshbarmak))
# print(lagman & beshbarmak)
#
# print(lagman.difference(beshbarmak))
# print(lagman - beshbarmak)
#
# print(lagman.symmetric_difference(beshbarmak))
# print(lagman ^ beshbarmak)
#
# print(lagman.union(beshbarmak))
# print(lagman | beshbarmak)


# # dict = {key: value}
# students = ['Alina', 'Askat', 'Begimay', 'Adilet']
#
# student = {
#     'name': 'Jack',
#     '1age': 21,
#     'hobby': ['english', 'chess', 'football'],
#     # (1, 2, 3): 'werwer'
#     'fail': False
# }
# # student3 = dict((['name', 'John'],['age', 19],['country', 'USA']))
# # print(student3)
# # print(type(student2))
#
# student2 = dict(name='Anna', age=20, country='RUS')
# print(student2.items())
# for a, b in student2.items():
#     print(f'{a}: {b}')





# print(student2.keys())
# print(student2.values())



#
# print(student['name'])
# print(student.get('name', 'неправильно указан ключ'))
#
#
# # del student['fail']
# print(student.pop('fail'))

# student.update(student2)
# print(student)

# student2['surname'] = 'Ahmatova'
# student2['surname'] = 'Berdieva'
#
#
# print(student2)


# print(student['name'])
# print(student['age'])

# print(student[(1, 2)])
