def describe_pet(pet_name, animal_type='dog'):
    """Display a type of an animal and its name"""
    print(f'I have a {animal_type}')
    print(f'My {animal_type}"name is {pet_name.title()}')


describe_pet('serena')


# # A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')


#  # A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
