'''Но сейчас мы не будем играть в эту игру. Вы будете судить игру, и оценивать результат. Вам дан результат игры, и вы должны решить, кто победил или что это ничья. Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок. В случае ничьи, результат должен быть "D".

Результаты игры представлены, как список (list) строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.

Вх. данные: Результат игры, как список (list) строк (str, unicode).
Вых. данные: "X", "O" или "D", как строка (str).

Примеры:
checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"

Как это используется: Эта задача поможет вам лучше понять, как работать с матрицами и вложеными массивами. Ну и конечно, это будет полезно при разработке игр, так как надо уметь оценивать результаты.

Предусловия:
В играх может быть только один победитель или ничья.
len(game_result) == 3
all(len(row) == 3 for row in game_result)'''

from typing import List


def checkio(g: List[str]) -> str:

    if g[0][0] == g[0][1] == g[0][2] and g[0][0] != '.':
        return g[0][0]
    elif g[0][0] == g[1][1] == g[2][2] and g[0][0] != '.':
        return g[0][0]
    elif g[0][0] == g[1][0] == g[2][0] and g[0][0] != '.':
        return g[0][0]
    elif g[0][1] == g[1][1] == g[2][1] and g[0][1] != '.':
        return g[0][1]
    elif g[0][2] == g[1][2] == g[2][2] and g[0][2] != '.':
        return g[0][2]
    elif g[0][2] == g[1][1] == g[2][0] and g[0][2] != '.':
        return g[0][2]
    elif g[1][0] == g[1][1] == g[1][2] and g[1][0] != '.':
        return g[1][0]
    elif g[2][0] == g[2][1] == g[2][2] and g[2][0] != '.':
        return g[2][0]
    else:
        return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "...",
        "XXX",
        "OO."]) == "X", "Xs wins"
    assert checkio([
        "OXO",
        "XOX",
        "OXO"]) == "O", "Os wins"
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
