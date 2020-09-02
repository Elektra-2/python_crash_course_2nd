# # Organizing a list
#
# # Sorting a List Permanently with the sort() Method in Alphabetic order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#
# # Sorting a List Permanently with the sort() Method in Alphabetic order
# # but using an argument reverse=True
#
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
#
# # Sorting a List Temporarily with the sorted() Function
colors = ['green', 'blue', 'yellow', 'pink']
print(colors)  # printa a lista original
print((sorted(colors))) # printa a lista sorted
print(colors)  # printa a lista de volta a original sem estar sorted.
#
# # Printing a List in Reverse Order using the reverse() method
# # Notice that reverse() doesn’t sort backward alphabetically;
# # it simply reverses the order of the list:
colors = ['green', 'blue', 'yellow', 'pink']
colors.reverse()
print(colors)

# # The reverse() method changes the order of a list permanently,
# # but you can revert to the original order anytime by applying reverse() to the same list a second time.
colors = ['green', 'blue', 'yellow', 'pink']
colors.reverse()
print(colors)
colors.reverse()  # applying reverse() again takes the list to its original positions
print(colors)

# Finding the Length of a List
colors = ['green', 'blue', 'yellow', 'pink']
print(len(colors))

# Python counts the items in a list starting with one and not zero

# If an index error occurs and you can’t figure out how to resolve it,
# try printing your list or just printing the length of your list.
# Your list might look much different than you thought it did,
# especially if it has been managed dynamically by your program.
# Seeing the actual list, or the exact number of items in your list, can help you sort out such logical errors.

