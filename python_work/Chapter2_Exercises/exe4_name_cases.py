#Use a variable to represent a person’s name,#
#and then print that person’s name in lowercase, uppercase, and title case.#

persons_name = "leia organa"
message_upper = persons_name.upper()
message_lower = persons_name.lower()
message_title = persons_name.title()

final_message = f'{message_upper}\n{message_lower}\n{message_title}'
print(final_message)
