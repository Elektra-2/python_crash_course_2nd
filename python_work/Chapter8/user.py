def new_user(name, email):
    """Adds a new user to the website"""
    user = {
        'name': name,
        'email': email,
    }
    return user


added_user = new_user('caro', 'carol@hotmail.com')
print(added_user)
