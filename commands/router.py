from main import open_app          # import the launcher
from commands.ai_chat import ai_chat

def process_command(command):
    command = command.strip()
    lower = command.lower()

    # Static commands
    static = {
        "help": "Available commands: help, exit, status | open <app> | chat <message>",
        "status": "System is running.",
        "exit": "Exiting HUESC."
    }

    if lower in static:
        return static[lower]
    
    # Open apps: "open chrome", "open spotify", "open code"
    if lower.startswith("open "):
        app_name = command[5:].strip()
        return open_app(app_name)   # <-- actually launch app

    # AI Chat: "chat Hello, how are you?"
    if lower.startswith("chat "):
        message = command[5:].strip()
        return ai_chat(message)
    
    return "Unknown command. Type 'help' for a list of available commands."
