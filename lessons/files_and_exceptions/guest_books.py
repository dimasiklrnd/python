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
    file_wr = 'lessons/files_and_exceptions/' + name + '.txt'
    while not file_wr:
        with open(file_wr, 'w') as f_o:
            f_o.write(write_book + '\n')


    n=1
    while file_wr:
        n+=1

        file_wr = 'lessons/files_and_exceptions/' + name + str(n)+'.txt'
        print(file_wr)
        if not file_wr:
            with open(file_wr, 'w') as f_o:
                f_o.write(write_book + '\n')
            break





    question = input('Почему вам нравится программировать?: ')
    if question == 'енд':
        flag = False
        continue
    with open(file_wr, 'a') as f_o:
        f_o.write('Ответ ' + name.title() + ' на вопрос о программировании: '+question + '\n')
