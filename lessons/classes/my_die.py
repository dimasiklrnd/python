from die import Die

die1 = Die()
for i in range(11):
    print(die1.sides, end=', ')
    die1.roll_die()
