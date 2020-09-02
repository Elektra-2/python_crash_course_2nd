# # Modifying Elements on a list
# motos = ['triumph', 'yamaha', 'ducati', 'honda']
# print(motos)
#
# motos[1] = 'suzuki'
# print(motos)
#
# # Append or Adding new elements on a list
# # The append() method adds 'ducati' to THE END OF THE LIST
# # without affecting any of the other elements in the list:
# motos.append('yamaha')
# print(motos)

# Using the insert() method to add new elements to the list but AT A SPECIFIC POSITION
# cars = ['gol', 'fox', 'fusca']
# cars.insert(2, 'logan')
# print(cars)
#
# # Using del statement to remove an item from a list
# del cars[0]
# print(cars)

# Using the pop() method
# The pop() method removes the last item in a list,
# but it lets you work with that item after removing it.

# cars2 = ['citroen', 'touro', 'argos', 'fiesta']
# cars2_pop = cars2.pop()
# # cars2_pop = cars2.pop(1) or use pop() to pop an specific position
# print(cars2)
# print(cars2_pop)

# Removing an item by value using remove() method
colors = ['green', 'blue', 'yellow', 'pink']
print(colors)
colors.remove('yellow')
print(colors)

# You can also use the remove() method to work with a value that’s being removed from a list.
# Let’s remove the value 'pink' and print a reason for removing it from the list:
dontlike = 'pink'
colors.remove(dontlike)
print(colors)
print(dontlike)
