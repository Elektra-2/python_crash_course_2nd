#  requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#  for requested_topping in requested_toppings:
#   if requested_topping == 'green peppers':
#      print("Sorry, we're out of green peppers")
#   else:
#      print(f'Adding requested toppings {requested_topping}')

# print('\nYou finished making your pizza!')


# Checking the list is not empty

requested_toppings = ['cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'adding your topping {requested_topping}')
    print("\nYou finished your pizza")
else:
    print("Are you sure you want a plain pizza?")
