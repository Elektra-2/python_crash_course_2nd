# Creating a dictionary

alien_0 = {'color': 'green', 'points': '5'}
print(alien_0['color'])
print(alien_0['points'])

print('\n')


# To get the value associated with a key, give the name of the dictionary and then place
# the key inside a set of square brackets

new_points = alien_0['points']
print(f'Congrats! you just won {new_points}!')

print('\n')

#  Adding more key values to a dictionary

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('\n')


# Defining and / or creating an empty dictionary

alien_a = {}
alien_a['color'] = 'green'
alien_a['points'] = 15

print('\n')

# Modifying a value in a dictionary
# To modify a value in a dictionary, give the name of the dictionary with the key in square brackets alien_c['color']
# and then the new value you want associated with that key. 'yellow'


alien_c = {'color': 'green'}
print(f"the alien is {alien_c['color']}")

alien_c['color'] = 'yellow'
print(f"the alien is {alien_c['color']}")




