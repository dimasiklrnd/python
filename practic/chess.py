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
    c = [i for j in pawns for i in j]
    print(c)
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
