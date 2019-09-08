'''
Вам предоставляется набор координат, в которых расставлены белые пешки. Вы должны подсчитать количество защищенных пешек.

Входные данные: Координаты расставленных пешек в виде набора строк.
Выходные данные: Количество защищенных пешек в виде целого числа.

Пример:
safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
'''
pole_a = 'abcdefgh'
pole_b = '12345678'


def safe_pawns(pawns: set) -> int:
    c = [''.join(i+str(j)) for i in pole_a for j in pole_b]
    l = c[::8]
    n = 0
    for i in pawns:
        if i not in l:
            a = i[0]
            z = int(i[1])
            b = pole_a.index(a)

            pr_sleva = ''
            if b-1 >= 0:
                pr_sleva = ''.join(pole_a[b-1]+str(z-1))

            pr_sprava = ''
            if b+1 < 8:
                pr_sprava = ''.join(pole_a[b+1]+str(z-1))

            if pr_sleva in pawns or pr_sprava in pawns:
                n += 1

    return n


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"}) == 7
    assert safe_pawns({"a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"}) == 0
    assert safe_pawns({"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"})
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
