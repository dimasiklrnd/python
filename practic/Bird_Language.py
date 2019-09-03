'''
Птичка меняет слова по следующим правилам:
- после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
- после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);
Гласные буквы == "aeiouy".

Вам дана птичья фраза как несколько слов, разделёных пробелами (каждая пара слов разделена одним пробелом). Птичка не знает ничего о знаках пунктуации и использует только буквы. Все слова даны в нижнем регистре. Необходимо перевести эту птичью песню в понятную простым роботам фразу.

Входные данные: Птичья фраза как строка (string).
Выходные данные: Перевод как строка (string).

Примеры:
translate("hieeelalaooo") == "hello"
translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
translate("aaa bo cy da eee fe") == "a b c d e f"
translate("sooooso aaaaaaaaa") == "sos aaa"

Связь с реальной жизнью: Этот простой «шифр» похож на тот, который используют дети для своего «птичьего» языка. Но теперь-то вы легко взломаете их хитрости.
'''

glas = "aeiouy"
sogl = 'bcdfghjklmnpqrstvwxz'


def translate(phrase):
    stroka = [i for i in phrase]
    copy_str = []
    n = [i for i in range(len(stroka)-1)]

    for i in n:
        if stroka[i] in sogl:
            if i < len(stroka) and stroka[i+1] in glas:
                copy_str.append(stroka[i])

        if stroka[i] in glas:
            if i < (len(stroka)-2):
                if stroka[i+2] == stroka[i] and stroka[i+1] == stroka[i]:
                    copy_str.append(stroka[i])
                    stroka.pop(i)
                    stroka.pop(i)
                    n.pop()
                    n.pop()

        if stroka[i] == ' ':
            copy_str.append(stroka[i])

    cop = ''.join(i for i in copy_str)

    return cop


if __name__ == '__main__':
    print("Example:")
    print(translate("hoooowe yyyooouuu duoooiiine"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
