from commands.router import process_command

print("HUESC Initializing...")

while True:
    user_input = input("HUESC> ")
    response = process_command(user_input)
    print(response)

    if user_input.lower().strip() == "exit":
        break