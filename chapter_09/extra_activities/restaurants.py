class Restaurant:
    def __init__(self,restaurant_name,cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cusine Type: {self.cusine_type}")

    def number_customers(self):
        print(f"We have served {self.number_served} Customers!")

    def increment_number_served(self,served):
        if served >= self.number_served:
            self.number_served = served
        else:
                print("Can't Count Back!")
        
    def open_restaurant(self):
        print(f"We Are Open!")

my_restaurant = Restaurant('Ocean Cusine','Sea Foods')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# my_restaurant.number_customers()
# my_restaurant.number_served = 10
# my_restaurant.number_customers()

my_restaurant.increment_number_served(52)
my_restaurant.number_customers()

# #Three Restaurants
# restaurant_one = Restaurant('La Colombe','French-inspired')
# restaurant_two = Restaurant('FYN','Japanese')
# restaurant_three = Restaurant('Qunu Restaurant','South African fusion')

# restaurant_one.describe_restaurant()
# restaurant_two.describe_restaurant()
# restaurant_three.describe_restaurant()

