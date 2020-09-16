alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'blue', 'points': '15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# Make a list of empty Aliens:
aliens = []

# Make 30 aliens:
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 10}
    aliens.append(new_alien)
print(len(aliens))