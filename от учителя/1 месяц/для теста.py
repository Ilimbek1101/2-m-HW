# name = 4 / 2
# name2 = 4 // 2
#
# print(type(name), type(name2))
#
# sdf = ("", 1 > 2, {}, 0, not True)
# sad = ([False], -0.1, 'None', 1 != 2 and 3 >= 2)
# print(type(sdf))
# print(type(sad))
#
# _home2 = "Victory 4 floor"
#
# print(_home2)
# 2home@ = 'Ибраимова 103'

# re = {'name': 'fds', 'sur': 'sdsd'}
# dsd = {'name': 'ewe', 'sur': 'op'}
#
# re.update(dsd)
#
# print(re)

# if 10 > 0:
#     pass
# else:
#     pass
# elif 10 > 9:
# print(1)

# letter = 'word'[2]
# 
# print(letter)

# user = {"пользователь", "Шерлок", "пароль", "BakerStreet221"}
# print(user['пароль'])

# list_1 = ['baha', 'nurik', 'adi', 'kesha', 'aiba']
# list_1.sort()
# rev_list = list_1[::-1]
# list_1.reverse()
#
# print(list_1 == rev_list, list_1 is rev_list)

# numbers = (1, 2, 3)
# numbers += (4, 5, 6)
# numbers[5] = 5.9
# numbers.append(6)
# print(numbers)

# def dfg(name, age=20):
#     return f"я {name}, мне {age} лет, я родился в {2022 - age} году"
#
# print(dfg("Искендер", 26))

# def f(a, *args, **kwargs):
#     print('{} | {} | {}'.format(a, args, kwargs))
#
# f(1, 2, 3, x=4, y=5)

from datetime import datetime as dt
print(dt.now())

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