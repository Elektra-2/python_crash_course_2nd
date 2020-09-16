#  A dictionary of similar object

favorite_programming_languages = {
    'Caro': 'Python',
    'Claudia': 'Golang',
    'Ruiz': 'C++',
    'Antonio': ' Java'
    }

for name, language in favorite_programming_languages.items():
    print(f"{name.title()}' Favorite Language is {language.title()}")

for name in favorite_programming_languages.keys():
    print(name)

# Using get() to access dictionary values
# If you try accessing a key value that does not exits on the dictionary, you'll get a traceback keyerror
#  For dictionaries, specifically, you can use the get() method to set a default value that will be returned
#  if the requested key doesn’t exist.

alien_0 = {'color': 'green', 'speed': 'slow'}
points_value = alien_0.get('points', 'No points assigned')
print(points_value)
