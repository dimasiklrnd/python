"""Любимое число: напишите программу, которая запрашивает у пользователя его любимое число . Воспользуйтесь функцией json.dump() для сохранения этого числа в файле .
Напишите другую программу, которая читает это значение и выводит сообщение: «Я знаю ваше любимое число! Это _____» ."""

import json


def favorite_num():
    name = input("Ваше имя? " )
    filename = 'lessons/files_and_exceptions/fav_num'+'_'+str(name)+'.json'
    try:
        with open(filename) as f_obj:
            fn = json.load(f_obj)
        num = fn[1]
        print('Я знаю ваше любимое число! Это: ' + num)

    except FileNotFoundError:
        print('\tЯ не знаю вас')
        fav_num = input('Введите ваше любимое число: ')
        list_fn=[]
        list_fn.append(name)
        list_fn.append(fav_num)
        with open(filename, 'w') as f_obj:
            json.dump(list_fn,f_obj)
        print('\tприходите в следующий раз и я угадаю твое число')


favorite_num()
