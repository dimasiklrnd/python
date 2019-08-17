from restaurant import Restaurant

my_res_0 = Restaurant('paris', 'eat', 10)
my_res_0.describe_restaurant()
my_res_0.open_restaurant()


my_res1 = Restaurant('palladium', 'pizza', 5)
my_res1.describe_restaurant()
my_res1.open_restaurant()

my_res2 = Restaurant('petrovskyi prichal', 'ice cream', 50)
my_res2.describe_restaurant()
my_res2.closed_restaurant()
my_res2.set_number_served(8)
my_res2.open_restaurant()
my_res2.increment_number_served(32)
my_res2.closed_restaurant()