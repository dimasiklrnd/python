'''
Вам необходимо найти длину самой длинной подстроки, которая состоит из одинаковых букв. Например, строка "aaabbcaaaa" состоит из четырех подстрок с одинаковыми буквами "aaa", "bb","c" и "aaaa". Последняя подстрока является самой длинной, что и делает ее ответом.

Входные данные: Строка.

Выходные данные: Целое число.

Пример:
long_repeat('sdsffffse') == 4
long_repeat('ddvvrwwwrggg') == 3
'''
from itertools import groupby


def iterlen(it):
    return sum(1 for _ in it)


def long_repeat(s):
    """
        length the longest substring that consists of the same char
    """
    result = {}
    for letter, group in groupby(s):
        l = iterlen(group)
        if result.get(letter, 0) < l:
            result[letter] = l
    p = sorted([i for i in result.values()], reverse=True)
    if len(s) > 0:
        return p[0]
    else:
        return 0




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
