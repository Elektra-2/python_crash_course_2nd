def new_user(name, email):
    user = {
        'name': name,
        'email': email,
    }
    return user


added_user = new_user('caro', 'carol@hotmail.com')
print(added_user)
