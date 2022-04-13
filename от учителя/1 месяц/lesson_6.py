def greetings(name:str):
    print(f'Hello, {name.title()}')

greetings('aman')


# numbers = [1, 2, 3, 4, 5, 6]
# words = ['zero', "one", 'two', 'three']
#
# # our_dict = dict(enumerate(words))
# # print(our_dict)
# #
# print(numbers)
# numberx2 = list(map(lambda x: x ** 2, numbers))
# print(numberx2)
#
# numbers2 = [i**2 for i in numbers]
# print(numbers2)

#
# less3 = list(filter(lambda x: x < 4, numbers))
# print(less3)


# letters = 'qwertyuiopasdfghjklzxcvbnm'
# up_letters = letters.upper()
# numbers = '123456789'
# symbols = '!@#$%&()'
#
# best_password = letters + up_letters + numbers + symbols
#
# print(best_password)
#
# user_password = input('enter password')
# for i in user_password:
#     if i in best_password:
#         print("пароль надежен")
#         break
#     else:
#         print('не пойдет!')



# numbers = [5, 6, 7, 8, 9]
# other = ['a', 'b',' c', 'd', 'e', 'f']
#
# while True:
#     indx = input('Введите индекс! ')
#     try:
#         print(numbers[int(indx)])
#     except:
#         print(f" Only numbers! or index 0 to {len(numbers) - 1}")
    # except ValueError:
    #     print("Only numbers!")



# otrher_words = ['modules', 'import', 'from']
# lambda a: a * 2

# def name(a):
#     print(a)
#     return a + a
#
# print(name(5))
#
# a = lambda x, y: x + x * y
# print(a(5, 2))
#
# e, r = lambda x: x + x, lambda x: x + x,
# print(e(3), r(5))

# new_words = lambda x: x.title(), words

# words = ['python', 'lambda', 'exception', 'conditions', 'egg']
# limit = 3
#
# new = list(filter(lambda x: len(x) <= limit, words))
# other = list(map(lambda x: x.upper(), words))
#
# print(new)
# print(other)


# def upword(lst):
#     return lst.title()
#
# def edit_word(lst, func):
#     for i in lst:
#         print(func(i))
#
# edit_word(words, lambda word: word.upper())
# edit_word(words, upword)