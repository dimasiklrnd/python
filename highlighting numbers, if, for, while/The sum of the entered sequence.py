'''Определите сумму всех элементов последовательности, завершающейся числом 0.

Числа, следующие за нулем, считывать не нужно.

Формат входных данных
Вводятся элементы последовательности по одному целому числу на строку. Числа вводятся, пока не будет введен 0.

Формат выходных данных
Вывести одно целое число - сумму последовательности.'''
n = int(input())
x = 0
while n > 0:
    x = x + n
    n = int(input())


print(x)
