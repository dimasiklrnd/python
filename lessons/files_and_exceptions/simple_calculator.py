print("Дайте мне два числа, и я разделю их.")
print("Введите 'q', чтобы выйти.")
while True:
    first_number = input("\nПервое число: ")
    if first_number == 'q':
        break
    second_number = input("Второе число: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('Нельзя делить на ноль!')
    except ValueError:
        print('Небходимо ввести числа!')
    else:
        print(answer)
