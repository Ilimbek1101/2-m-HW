import random
from random import sample, choice, randint, randrange
import datetime
import time

secret = randint(1, 50)
print(secret)

guess = int(input('number? '))
if guess > secret:
    print('<')
elif guess == secret:
    print('')



# player = (randint(1, 6), randint(1, 6))
# comp = (randint(1, 6), randint(1, 6))
#
# cash = 500
# bet = int(input(f'Доступно {cash} '
#                 f'Введите ставку!'))
#
# print(f'comp: {comp} \n'
#       f'player: {player}')
#
# if sum(player) > sum(comp):
#     print('You won!')
#     cash += bet
# elif sum(player) < sum(comp):
#     print('You lost!')
#     cash -= bet
# else:
#     print('Draw')
# print(cash)


# data = []
# students = [1, 3, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17]
# print(students)
# start = datetime.datetime.now()
# while len(students) != 0:
#     chosen_student = choice(students)
#     name = input(f'укажите имя: {chosen_student}')
#     question_student = choice(students)
#     rate = int(input(f'Задаёт вопрос: {question_student} '
#                      f'Оценка для: {name}'))
#     data.append({'name': name, 'rate': rate})
#     del students[students.index(chosen_student)]
#     for i in data:
#         print(i)
#     print(students)
#
# print(f'Время опроса: {datetime.datetime.now() - start}')


# c = 0
#
# while c != 5:
#     print(c)
#     time.sleep(1)
#     c += 1

# def timer(number):
#     while number != -1:
#         time.sleep(1)
#         print(number)
#         number -= 1
# timer(5)

# start = datetime.datetime.now()
# print(start)
# time.sleep(5)
# print(datetime.datetime.now())
# print(datetime.datetime.now() - start)





# print(sample(students, 2))
#
# print(randrange(1, 10, 2))
#
# print(randint(1, 5), randint(1, 5))
# print(randint(1, 6), randint(1, 6))



# from lesson_6 import greetings as privet
# greetings('azat')
# privet('samat')
