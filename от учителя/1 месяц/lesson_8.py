from random import choice, randint, sample
import datetime
    
data = []
themes = list(range(1, 8+1))
while True:
    # print(themes)
    print(sample(themes, 2))

    student = input('name: ').title()
    if student == 'Q':
        print('exit')
        break
    rate = int(input(f'rate for {student}: '))
    data.append({'name': student, 'rate': rate})
    print(data)
    with open('rate.txt', 'a') as file:
        file.write(f"name: {student}, rate: {rate}\n")

a = 0
for i in data:
    a += i['rate']


with open('rate.txt', 'a') as file:
    file.write(f"\n Average rate {round(a / len(data), 2)}")

with open('rate.txt', 'r') as file:
    print(file.read())



# c = 0
# while True:
#     f_number = randint(1, 100)
#     s_number = randint(100, 200)
#     answer = int(input(f'сколько будет {s_number} - {f_number}'))
#     if answer == 'q':
#         break
#     c += 1
#     print(f'попытки {c}')
#     res = s_number - f_number
#     if answer == res:
#         print('ok')
#     else:
#         print(f'неправильно! Правильный ответ {res}')
#
#
# with open('results.txt', 'a') as file:
#     file.write(f'\nПопыток было {c}')



# secret_number = 27
# left = 1
# right = 100


# while True:
#     mid = int((left + right) / 2)
#     answer = input(f'{mid} < or >')
#     with open('results.txt', 'a') as file:
#         file.write(f'\n{mid} {answer}')
#     if answer == '<':
#         right = mid
#     elif answer == '>':
#         left = mid
#     elif answer == 'ok':
#         print('we found it')
#         break

    # if secret_number < mid:
    #     right = mid
    #     print(mid)
    # elif secret_number > mid:
    #     left = mid
    #     print(mid)
    # elif secret_number == mid:
    #     print('we found it')
    #     break



# new_file = open('file.txt', 'w')
# new_file.write('other words')
# new_file.close()



# open('file.txt', 'w') as file:
#     file.write(f'{datetime.datetime.today()}')

#
# with open('file.txt', 'r') as file:
#     for i in file.read():
#         time.sleep(0.2)
#         print(i, end='')

