import os  # Чтобы получить содержимое этого каталога в виде списка

flag = True
print('Как закончите, введите "енд')
file_write = 'lessons/files_and_exceptions/guest_books.txt'

while flag:
    name = input('Ваше имя?: ')
    if name == 'енд':
        flag = False
        continue
    write_book = 'Привет, человек по имени ' + name.title() + '!'

    print(write_book)

    file_wr = 'lessons/files_and_exceptions/' + name + '.txt'

    # Каталог из которого будем брать файлы
    directory = 'lessons/files_and_exceptions/'
    # Получаем список файлов в переменную files
    files = os.listdir(directory)
    # Фильтруем список и получаем в виде списка в переменную
    txt = list(filter(lambda x: x.endswith('.txt'), files))

    comparison = name + '.txt'

    if comparison in txt:  # если в директории есть такой же файл, то прибавляем к имени единицу
        n = 1
        while comparison in txt:
            comparison = name+'_'+str(n)+'.txt'
            n += 1

    file_wr = 'lessons/files_and_exceptions/' + comparison  # переименовываем файл

    with open(file_wr, 'x') as f_o:  # открытие на запись если файла не существует, иначе исключение
        f_o.write(write_book + '\n')

    question = input('Почему вам нравится программировать?: ')
    if question == 'енд':
        flag = False
        continue
    with open(file_wr, 'a') as f_o:
        f_o.write('Ответ ' + name.title() +
                  ' на вопрос о программировании: '+question + '\n')
