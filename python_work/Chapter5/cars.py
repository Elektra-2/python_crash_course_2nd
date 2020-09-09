#  Simple example using ifs

cars = ['volks', 'ford', 'audi', 'bmw', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# Comparing Values
#
# requested_toppings = 'mushrooms'
# if requested_toppings != 'anchovies':
#     print('Hold the Anchovies')
#
#
# #  Checking a value not in a list
#
# banned_users = ['andrew', 'claudia', 'jorge']
# user = 'marie'
#
# if user not in banned_users:
#     print(f'{user.title()}, you can post a message here')

age = 18
if age >= 18:
    print('OK to vote')
