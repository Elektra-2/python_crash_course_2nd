prompt = input("Hello, tell me something and I will repeat: ")
prompt += "Enter 'quit' to end the program"

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
