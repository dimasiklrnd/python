from die import Die

die1 = Die()  # шестигранный кубик
for i in range(11):
    die1.roll_die(1, 6)
    print(die1.sides, end=', ')


print('')
die2 = Die()  # десятигранный
for i in range(11):
    die1.roll_die(1, 10)
    print(die1.sides, end=', ')

print('')
die3 = Die()  # двадцатигранный
for i in range(11):
    die1.roll_die(1, 20)
    print(die1.sides, end=', ')
