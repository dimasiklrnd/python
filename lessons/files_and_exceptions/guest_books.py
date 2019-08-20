flag = True
print('Как закончите введите "енд')
file_write = 'lessons/files_and_exceptions/guest_books.txt'

while flag:
    nam = input('Ваше имя?: ')
    if nam == 'енд':
        flag = False
        continue
    write_book = 'Привет, человек по имени ' + nam.title() + '!'

    print(write_book)

    file_wr = 'lessons/files_and_exceptions/' + nam + '.txt'
    with open(file_wr, 'x') as f_o:  # открытие на запись если файла не существует, иначе исключение
        f_o.write(write_book + '\n')

    question = input('Почему вам нравится программировать?: ')
    if question == 'енд':
        flag = False
        continue
    with open(file_wr, 'a') as f_o:
        f_o.write('Ответ ' + nam.title() +
                  ' на вопрос о программировании: '+question + '\n')
