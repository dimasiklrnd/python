file_write = 'lessons/files_and_exceptions/programming.txt'

with open(file_write, 'w') as file_object:
    file_object.write('Мне нравится программировать')

with open(file_write, 'a') as file_object:# атрибут 'a' добавляет в файл не перезаписывая его
    file_object.write('\nМне нравится программировать!')
