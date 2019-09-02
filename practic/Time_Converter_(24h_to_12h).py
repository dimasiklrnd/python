"""- выходной формат должен быть 'чч:мм a.m.' (для часов до полудня) или 'чч:мм p.m.' (для часов после полудня)
- если часы меньше 10 - не пишите '0' перед ними. Например: '9:05 a.m.'
Входные данные: Время в 24-часовом формате (как строка).
Выходные данные: Время в 12-часовом формате (как строка)."""


def time_converter(time):
    t = time.split(':')
    if int(t[0]) == 12:
        s = "".join(t[0]+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 13:
        s = "".join('1'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 14:
        s = "".join('2'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 15:
        s = "".join('3'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 16:
        s = "".join('4'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 17:
        s = "".join('5'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 18:
        s = "".join('6'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 19:
        s = "".join('7'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 20:
        s = "".join('8'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 21:
        s = "".join('9'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 22:
        s = "".join('10'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 23:
        s = "".join('11'+':'+t[1]+' ' + 'p.m.')
        return s
    elif int(t[0]) == 10:
        s = "".join('10'+':'+t[1]+' ' + 'a.m.')
        return s
    elif int(t[0]) == 11:
        s = "".join('11'+':'+t[1]+' ' + 'a.m.')
        return s
    elif str(t[0]) == '00':
        s = "".join('12'+':'+t[1]+' ' + 'a.m.')
        return s
    else:
        t2 = []
        for i in str(t[0]):
            if int(i) != 0 and int(t[0]) < 10:
                t2.append(i)
                s2 = "".join(t2[0]+':'+t[1]+' ' + 'a.m.')
                return s2


if __name__ == '__main__':
    print("Example:")
    print(time_converter('23:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
