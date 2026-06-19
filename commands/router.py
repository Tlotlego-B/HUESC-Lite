def process_command(command):
    command = command.lower().strip()

    commands = {
        "help": "Available commands: help, exit, status",
        "status": "System is running.",
        "exit": "Exiting the program."
    }

    return commands.get(command, "Unknown command. Type 'help' for a list of available commands.")