with open(file_wr, 'x') as f_o:  # открытие на запись если файла не существует, иначе исключение
        f_o.write(write_book + '\n')