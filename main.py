from commands.router import process_command
import logging

logging.basicConfig(filename="huesc.log", level=logging.INFO)

print("HUESC Advanced Initializing...")

while True:
    try:
        command = input("HUESC> ")
        response = process_command(command)
        print(response)
        logging.info(f"Command: {command} | Response: {response}")

        if command.lower() == "exit":
            break
    except KeyboardInterrupt:
        print("\nExiting HUESC.")
        break
