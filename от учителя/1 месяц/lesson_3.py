# Списки - методы списков, отрезки, Кортежи.
# names = ['asan', 'leon', 'temir']
# names = [i.title() for i in names]
# print(names)

# data_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, True, 'float']
#
# strings = []
# numbers = []
#
# for i in data_types:
#     if type(i) == str:
#         strings.append(i)
#     # elif type(i) == int or type(i) == float:
#     #     numbers.append(i)
#     elif 3 <= i <= 7:
#         numbers.append(i)
#
# print(strings)
# print(numbers)


# data = []
#
# while 1: # 1991
#     nominals = int(input('Введите номинал: '))
#     if nominals == 0:
#         print('exit...')
#         break
#     data.append(nominals)
#     print(data)
# data = tuple(data)
# print(data)
#
#
# data = list(data)
# while 1: # 2014
#     nominals = int(input('Введите номинал: '))
#     if nominals == 0:
#         print('exit...')
#         break
#     data.append(nominals)
#     print(data)
#
# data = tuple(data)
# print(data)



# tpl = (1, 2, 3, 4, 5)
# strs = ('tuple', 'list', 'python')
# name = ('fedor',)
# tpl += strs
#
# new = tpl + strs
#
# print(new)
#
# print(type(name))
# print(type(tpl))
# print(type(strs))



# names = ['sam', 'jack', 'anna', 'jack', 'azamat', 'sergey']
# new_names = names.copy()
# new_names1 = names[0::]

# numbers = [2, 3, 5, 10]


# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))



# names.clear()
# print(names.count('jack'))
# print(names)

# new_names[-1] = False


# names.sort()
# names.reverse()

# new_names = sorted(names)
#
# print(id(names))
# print(id(new_names))
#
# print(names is new_names)
# print(names == new_names)
# print(2 is 5-3)


# c = 0
# while c != len(names):
#     print(names[c].capitalize())
#     c += 1

# for i in names:
#     print(i.upper())



# names.remove('azamat')
# del names[-1]
# print(names.index('jack'))
# new = names.pop(names.index('sam'))
# print(new)
# new_names.append(names.pop(0))

# print(names)
# print(new_names)




# list1 = ['string', 5, 2.5, True]

# names[0], names[1], names[2],  = names[0].title(), names[1].title(), names[2].title()
# names[0] = 'samat'

# [start:end:step]
# new_obj = [i.title() for i in names]

# print(new_obj)

# list1.append(False)
# list1.insert(2, '3sdfs')

# list1.extend(names)
# list1 += names



# print(list1)


# word = 'python'
# new_lest = list(word)
# print(new_lest)
# print(type(lst))
