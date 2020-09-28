# Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
# a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    """Creating Restaurants"""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describing Restaurant name and its cuisine type"""
        print(f"Restaurant {self.name} & Cuisine type {self.cuisine}")

    def open_restaurant(self):
        """Informing that the restaurant is open"""
        print(f'The Restaurant {self.name} is now open!')


my_restaurant = Restaurant('queen', 'italian')

"""Print the two attributes individually"""
print(my_restaurant.name)
print(my_restaurant.cuisine)

"""calling both methods"""
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

