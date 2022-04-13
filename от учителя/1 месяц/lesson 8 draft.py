# new_file = open('file.txt', 'w')
# new_file.write('other words')
# new_file.close()

with open('file.txt', 'a') as file:
    file.write('cool')