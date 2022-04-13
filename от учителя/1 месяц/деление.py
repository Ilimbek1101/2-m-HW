# Выполнение домашнего задания № .
# Программа “Деление”.

from random import randint
import datetime, time

attempts = int(input('Сколько попыток? '))
person = input('Укажите имя? ').title()
start = datetime.datetime.now()

s = 0

while s != attempts:
    number1 = randint(1, 100)
    number2 = randint(1, 10)
    if number1 % number2 == 0 and number1 / number2 <= 10:
        answer = int(input(f'{number1} : {number2} = ? '))
        print(int(number1 / number2))
        with open('results3.txt', 'a') as file:
            if answer == number1 / number2:
                file.write(f"{number1} : {number2} = {int(number1 / number2)} ({answer}) правильно\n")
            else:
                file.write(f"{number1} : {number2} = {int(number1 / number2)} ({answer}) неправильно\n")
        s += 1

with open('results3.txt', 'a') as file:
    file.write(f"было {attempts} попыток, потраченное время: {datetime.datetime.now() - start}, "
               f"имя: {person}\n")

with open('results3.txt', 'r') as file:
    for i in file.read():
        time.sleep(0.1)
        print(i, end='')