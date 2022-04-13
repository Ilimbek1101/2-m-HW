# print(type(None))
#
# a = 'abc'
#
# def whatis(obj):
#     if obj is None:
#         return None
#     elif obj is True:
#         return True
#     else:
#         return False
#
# print(whatis(a))



data = [
    {'name': 'Adilet', 'hws': 51, 'StandUp': 5, 'test': 65},
    {'name': 'Zarina', 'hws': 58, 'StandUp': 7, 'test': 75},
    {'name': 'Bektur', 'hws': 75, 'StandUp': 6, 'test': 80},
    {'name': 'Madina', 'hws': 75, 'StandUp': 8, 'test': 90},
    {'name': 'Elina', 'hws': 80, 'StandUp': 8, 'test': 100},
]

def search(name):
    for i in data:
        if name == i['name']:
            return i
    print('не найден')
    return False



def add_student(name):
    data.append({'name': name, 'hws': None, 'StandUp': None, 'test': None})


def edit_student(name):
    if search(name):
        # data[data.index(search(name))]['name']
        new_name = input(f'New name ').title()
        data[data.index(search(name))]['name'] = new_name
    else:
        print('не найден!')


def delete(name):
    del data[data.index(search(name))]

def show_all():
    for i in data:
        print(i)

while 1:
    show_all()
    command = input(f'Выберите команду: \n'
                    '1) Add \n'
                    '2) Edit\n'
                    '3) Delete\n'
                    )
    name = input('name: ').title()
    if command == '1':
        add_student(name)
    elif command == '2':
        edit_student(name)
    elif command == '3':
        delete(name)
    else:
        print("только от 1 до 3")



# def menu(breakfast, lunch, dinner):
#     return {'breakfast': breakfast, 'lunch': lunch, 'dinner': dinner}
#
# print(menu('eggs', 'chicken rice', 'steak'))
# print(menu(dinner='steak', lunch='chicken rice', breakfast='eggs'))

# def menu(**kwargs):
#     return kwargs
#
# print(menu(breakfast='каша', lunch="суп", dinner="котлеты"))
# print(menu(drink='cola', lunch="суп", dessert="cake"))



# def plus(a, b=4, *args):
#     print('a-', a, 'b-',  b, 'args-', args)
#     return a + b + sum(args)
#
#
# print(plus(2, 5, 1, 2))


# def greetings(name):
#     print('func started')
#     return f'Hello, {name.title()}'
#
#
# # greetings(input('enter name: '))
# print(greetings('vasya'))


# a = 5
# b = 4
# c = a + b
# print(c)
# def plus(a, b):
#     print(a + b)
#
# plus(3, 2)
# plus(23, 7)

# lenoleum_price = 250
#
#
# def get_square(length, width):
#     print(length * width)
#     # return length * width
#
# print(type(get_square(5, 2)))

# hall = get_square(6, 4)
# kitchen = get_square(5, 3)
#
# all_sum = hall + kitchen
# print(all_sum * lenoleum_price)
