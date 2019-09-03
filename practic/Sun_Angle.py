'''
Ваша задача - определить угол солнца над горизонтом, зная время суток. Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов. В 12:00 солнце в зените, а значит угол = 90 градусов. В 18:00 солнце садится за горизонт и угол равен 180 градусов. В случае, если указано ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу "I don't see the sun!".

Входные данные: Время.
Выходные данные: Угол солнца над горизонтом, округленный до 2 знаков после запятой.

Пример:
sun_angle("07:00") == 15
sun_angle("12:15"] == 93.75
sun_angle("01:23") == "I don't see the sun!"
'''


def sun_angle(time):
    h, m = time.split(":")
    time = (int(h)-6)*60+int(m)

    # check night time or return proportion of 180 deg
    if (time < 0 or time > (18-6)*60):
        angle = "I don't see the sun!"
    else:
        angle = 180*time/(12*60)
    return angle


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("18:00"))
    print(sun_angle("07:00"))
    print(sun_angle("12:15"))
    print(sun_angle("12:30"))
    print(sun_angle("01:23"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("12:30") == 97.5
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
