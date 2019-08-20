try:
    x = 5/0
    print(x)
except ZeroDivisionError:
    print("Вы не можете делить на ноль!")
