# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
# a) Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# b) Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# c) Print a second set of invitation messages, one for each person who is still in your list.

# Creating a list to invite people to dinner
guest_list = ['pai', 'mae', 'jeff', 'carla', 'vera', 'augusto']

# Sending a msg to the guests
guest_one = f' Hello, {guest_list[0].title()} you are invite to my dinner party'
guest_two = f'Hello, {guest_list[1].title()} you are invite to my dinner party'
guest_three = f'Hello, {guest_list[2].title()} you are invite to my dinner party'
print(guest_one, '\n', guest_two, '\n', guest_three, '\n')

# Guest rejected the invite and Im creating a msg to all the guests
rejected_invite = f'Unfortunately, {guest_list[0].title()}, cannot attend'
print(rejected_invite)

# Deleting the guest from the list and adding the new one
del guest_list[0]
guest_list.insert(0, 'val')

# print new msg to the new guest and all others.
new_guest = f' Hello, {guest_list[0].title()} you are invite to my dinner party'
print(new_guest, '\n', guest_two, '\n', guest_three, '\n')
