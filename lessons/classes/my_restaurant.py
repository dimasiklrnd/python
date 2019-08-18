from restaurant import Restaurant, IseCreamStand

my_res_0 = Restaurant('paris', 'ресторан', 10)
my_res_0.describe_restaurant()
my_res_0.open_restaurant()


my_res1 = Restaurant('палладиум', 'пицца', 5)
my_res1.describe_restaurant()
my_res1.open_restaurant()

my_res2 = Restaurant('петровский причал', 'ресторан')
my_res2.describe_restaurant()
my_res2.closed_restaurant()
my_res2.set_number_served(8)
my_res2.open_restaurant()
my_res2.increment_number_served(32)
my_res2.closed_restaurant()

my_iceCream = IseCreamStand(
    'ларек "Холодок"', 'мороженое', 5)
my_iceCream.describe_restaurant()
my_iceCream.increment_number_served(18)
my_iceCream.open_restaurant()
my_iceCream.flavors = ['бодрая корова', 'пломбир']
my_iceCream.flavors.append('большой папа')
my_iceCream.flavors.append('кубанская буренка')
my_iceCream.ice_creams_assortiment()
