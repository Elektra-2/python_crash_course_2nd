
users = ['antonio', 'claudia', 'admin', 'carol']

for user in users:
    if user == 'admin':
        print("Hello Admin Would you like to see the report?")
    else:
        print(f'Hello!, {user.title()}, thanks for logging in')
