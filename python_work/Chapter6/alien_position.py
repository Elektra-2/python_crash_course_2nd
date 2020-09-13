# Alien current speed
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original Alien x-position {alien_0['x_position']}")


#  Moving alien to the right
#  Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New Alien x-position is {alien_0['x_position']}")


# Removing key values - use the del statement

alien_1 = {'color': 'blue', 'points': 10}
print(alien_1)

# deleting a key value
del alien_1['points']
print(alien_1)
