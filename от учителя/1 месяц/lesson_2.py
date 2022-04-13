# Условные конструкции и Операторы сравнения, Булеаны,  Циклы
# or, and, not

word = input('word? ')

# c = 10
# while c != 0:
#     print(c)
#     c -= 1


# secret_word = 'python'
# c = 0
# guessed = 0
# fails = 0
#
# while c != len(secret_word):
#     letter = input('Enter letter: ')
#     if len(letter) > 1 and letter == 0:
#         print('Только одна буква!')
#         continue
#     # for i in secret_word:
#     if letter in secret_word:
#         guessed += 1
#     else:
#         fails += 1
#     print(guessed)
#     print(fails)
#     c += 1







# while True:
#     day = int(input('Введите день: '))
#     if day == 0:
#         print('Программа завершена: ')
#         break
#     month = int(input('Введите месяц: '))

# day = 5
# month = 10

    # if 21 <= day <= 31 and month == 3 or day >= 1 and day <= 20 and month == 4:
    #     print('ОВЕН')



# words = ''
# c = 0
#
# while c != 3:
#     word = input('Enter word: ')
#     words += ''.join(word)
#     print(words)
#     c += 1



# name = 'sam'
# name = name.join('at')
# print(name)



# vowels = 'aeouyi'
#
# word = 'abstraction'
#
# v_count = 0
# consonants = 0
# numbers = 0
# for i in word:
#     if i in vowels:
#         v_count += 1
#     else:
#         consonants += 1
#
#
# print(f'vowels: {v_count} - {v_count / len(word) * 100} %')
# print(f'consonants: {consonants} - {consonants / len(word) * 100} %')
# print('numbers: ', numbers)




# c = 0
#
# while c != len(word):
#     print(word[c], end='')
#     c += 1



# for number in range(1, 6):
#     if number <= 3:
#         print('пока все норм')
#         print(number)
#     else:
#         print("здесь уже устаём")

# name = 'aleksandr'
#
# for i in name:
#     if i == 's':
#         print('we found that letter!')
#         continue
#     print(i)

# time = 'evening'
#
# print(time == 'evening')
#
# if time == 'morning':
#     print('Доброе утро!')
# elif time == 'afternoon':
#     print('Добрый день!')
# elif time == 'evening':
#     print('Добрый вечер!')
# else:
#     print('Здравстуйте!')


# print(3 > 5)
# print(3 < 5)
# print(3 <= 5)
# print(3 >= 5)
# print(3 == 5-2)
# print(3 != 5)



# print(bool(5))
# print(bool(0))
# print(bool('abc'))
# print(bool(''))
# print(bool(-0))
