'''
Отсортируйте заданную итерацию так, чтобы ее элементы оказались в порядке убывания частоты, то есть, сколько раз они появляются в элементах. Если два элемента имеют одинаковую частоту, они должны заканчиваться в том же порядке, что и первое появление в итерируемом.

frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']

Вход: повторяемый
Выход: итерируемый
Условие: элементы могут быть целочисленными или строковыми
'''
from collections import Counter


def frequency_sort(items):
    a = items[:]
    b = Counter(a).most_common()
    print(b)
    c = [k[0] for k in b for i in items if i == k[0]]
    print(c)
    return c


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [
        4, 4, 4, 4, 2, 2, 2, 6, 6]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
        'bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
