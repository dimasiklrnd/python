n = int(input('num? '))
p = int(input('pow? '))
r = 1
while (p > 0):
    r *= n
    p -= 1
print('result:', r)
