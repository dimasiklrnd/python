file_write = 'lessons/files_and_exceptions/programming.txt'

with open(file_write, 'w') as file_object:
    file_object.write('Мне нравится программировать\n')
    file_object.write('Мне нравится программировать!!!\n')

with open(file_write, 'a') as file_object:# атрибут 'a' добавляет в файл не перезаписывая его, 'r+' как чтение так и запись
    file_object.write('Мне нравится программировать!\n')
