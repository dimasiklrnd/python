flag = True
print('Как закончите введите "енд')
file_write = 'lessons/files_and_exceptions/guest_books.txt'

while flag:
    name = input('Ваше имя?: ')
    if name == 'енд':
        flag = False
        continue
    write_book= 'Привет, человек по имени ' + name.title() + '!'
    print(write_book)
    with open(file_write, 'a') as f_o:
        f_o.write(write_book + '\n')

    question = input('Почему вам нравится программировать?: ')
    with open(file_write, 'a') as f_o:
        f_o.write('Ответ ' + name.title() + ' на вопрос о программировании: '+question + '\n')
