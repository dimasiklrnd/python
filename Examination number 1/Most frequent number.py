'''На вход программе подается массив чисел.Необходимо найти число, которое чаще всего встречается в массиве. Гарантируется, что такое число одно.

Формат входных данных
В первой строке задается число N , длина массива, далее идут N чисел -- элементы массива. Все числа больше 0 и меньше 100. Каждое число вводится с новой строки.

Формат выходных данных
Одно число, которое встречается наибольшее количество раз.'''
from collections import Counter

n = int(input())

N = []

while n > 0:
    x = int(input())
    N.append(x)
    n -= 1

# превращает в словатрь {} и подсчитывает количество вхождений всех элементов
c = Counter(N)

"""M = {}

for i in N:
    if i in M:
        M[i] += 1
    else:
        M[i] = 1
print(M)"""

D = sorted(c.values())  # сортируем по количеству вхождений
mx = D[len(D)-1]  # максимально значение получилось в конце списка

val = 0

for i, j in c.items():
    if j == mx:
        val = i  # присваеваем переменной ключ, который и есть значение которое больше всех встречается в массиве


print(val)
