from system.launcher import open_app
from ai.chat import chat
from plugins.plugins import load_plugins


def process_command(command):
    command = command.strip()
    lower = command.lower()

    # Static commands
    static = {
        "help": "Available commands: help, exit, status | open <app> | chat <message> | plugins",
        "status": "System is running.",
        "exit": "Exiting HUESC."
    }

    if lower in static:
        return static[lower]
    
    # Open apps

    if lower.startswith("start "):
        app_name = command[6:].strip()
        return open_app(app_name)

    if lower.startswith("open "):
        app_name = command[5:].strip()
        return open_app(app_name)

    # AI Chat
    if lower.startswith("chat "):
        message = command[5:].strip()
        return chat(message)

    # Plugin system
    if lower.startswith("plugin "):
        plugin_name = command[7:].strip()
        return load_plugins(plugin_name)

    return "Unknown command. Type 'help' for a list of available commands."
