'''Посчитать количество четных элементов в массиве целых чисел, заканчивающихся нулём. Сам ноль учитывать не надо.

Формат входных данных
Массив чисел, заканчивающийся нулём (каждое число с новой строки, ноль не входит в массив)

Формат выходных данных
Одно число — результат.'''

n = int(input())
x = 0
while n != 0:
    if n % 2 == 0:
        x += 1
    n = int(input())


print(x)
