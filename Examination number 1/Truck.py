"""Вы - водитель грузовика с открытым кузовом. В кузове два груза: пианино и холодильник.
Пианино необходимо доставить в институт, холодильник в общежитие.
В каждое из этих мест ведет отдельная дорога, начинающаяся от перекрестка, на котором
Вы стоите, других дорог в мире нет.
Известно, что по дороге в институт есть мост, на котором действует ограничение максимальной
допустимой массы автомобиля с грузом, а по дороге в общежитие есть туннель с ограничением высоты.
Требуется определить, возможно ли доставить грузы или нет (разумеется, сгружать их, где попало,
Вам запрещено).

Формат входных данных
На вход подается 8 чисел натуральных чисел (каждое < 100), каждое в новой строке,
в следующем порядке: вес грузовика без груза, высота платформы кузова (на которой стоят грузы),
вес пианино, высота пианино, вес холодильника, высота холодильника,
максимальный допустимый вес на мосту, максимальная допустимая высота в туннеле

Примечание: пианино и холодильник заведомо возвышаются над кабиной грузовика,
т.е. высоту кабины можно в расчет не принимать.

Формат выходных данных
Вывести YES если доставка возможна и NO в противном случае."""

wT = int(input())
hT = int(input())
wP = int(input())
hP = int(input())
wF = int(input())
hF = int(input())
maxW = int(input())
maxH = int(input())

wAll = wF+wP+wT
if hF >= hP:
    hAll = hT+hF
else:
    hAll = hT+hP


if maxW >= wAll and maxH >= hAll:  # когда все вместе меньше максимально допустимого
    print('YES')

elif maxH < (hT+hF):
    print('NO')


elif maxW < (wT+wP):
    print('NO')

elif maxH >= hAll and maxW >= (wT+wP):
    print('YES')

# когда пианино выше допуска, но вес обоих не превышает максимум
elif maxW >= wAll and maxH >= (hT+hF):
    print('YES')

else:
    print('NO')
