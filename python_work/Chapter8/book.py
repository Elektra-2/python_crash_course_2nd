#  8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title.
#  The function should print a message, such as One of my favorite books is Alice in Wonderland.
#  Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    """Display a msg about a favorite book"""
    print(f" One of my favorite books is {title.upper()}")


favorite_book('cem anos de solidao')
