name = input("Как ваше имя?: ")

file_write = 'lessons/files_and_exceptions/guest.txt'

with open(file_write, 'w') as file_object:
    file_object.write(name)