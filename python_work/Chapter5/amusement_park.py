# Testing if statements and elif conditions

age = 12
#
# if age < 4:
#     print("Your entrance is free")
# elif age < 18:
#     print("Your entrance cost $25")
# else:
#     print("Your entrance costs $40")

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f'your entrance costs $ {price}')
