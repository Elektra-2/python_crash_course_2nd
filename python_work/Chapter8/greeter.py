def get_formatted_name(first_name, last_name):
    """Return a full name formatted"""
    full_name = f'{first_name} {last_name}'
    return full_name.title()


while True:
    print("Tell me your name")
    print("Press 'q' to quit any time")

    f_name = input("Tell me your name: ")
    if f_name == 'q':
        break

    l_name = input("Tell me your last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f' Hello ! {formatted_name.title()}')

