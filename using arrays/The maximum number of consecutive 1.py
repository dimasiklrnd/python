'''Вводится последовательность, состоящая только из 0 и 1. Необходимо найти максимальное количество 1,
идущих подряд (без 0 между ними).

Формат входных данных
В первой строке задается натуральное N<=10000 , длина массива, далее идут N чисел 0 или 1 -- элементы массива. Каждое число вводится с новой строки.

Формат выходных данных
Одно число — результат.'''

N = [0]*int(input())
n = len(N)

# N=[] # можно схитрить
if n <= 10000:
    for i in range(len(N)):
        N[i] = int(input())

    """ и не с помощью фор, а вот так пересоздать массив, следуя условиям задачи
    while n > 0:
        N.append(int(input()))
        n -= 1"""
print(N)  # для наглядности

p = 0
m = 0
for i in range(len(N)):
    # пропускаем первый элемент, т.к. его не с чем сравнивать (первый элемент в массиве = 0)
    if i != 0:

        if N[i] == N[i-1] == 1 and p == 0:
            p += 2  # если счетчик пустой, то присваеваем ему 2, т.к. мы сравнили первые две единички
            if p > m:  # если счетчик превышает предыдущее макс значение, то
                m = p  # переписываем макс значение

        elif N[i] == N[i-1] == 1 and p != 0:
            p += 1
            if p > m:  # если счетчик превышает предыдущее макс значение, то
                m = p  # переписываем макс значение

        if N[i] == 0:
            p = 0

print(m)