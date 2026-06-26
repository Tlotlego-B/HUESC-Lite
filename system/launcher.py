import json
import subprocess
import sys
import os
import logging

with open("config/apps.json", "r") as file:
    APP_PATHS = json.load(file)

def open_app(app_name):
    app = app_name.lower().strip()
    platform = sys.platform

    if app not in APP_PATHS:
        return f"Unknown app: '{app}'. Available: {', '.join(APP_PATHS.keys())}"

    path = APP_PATHS[app].get(platform)

    if not path:
        return f"Platform '{platform}' not supported for {app}."

    if platform == "win32":
        path = os.path.expandvars(path)

    try:
        if platform == "win32":
            subprocess.Popen([path], shell=True)
        else:
            subprocess.Popen(path, shell=True)

        return f"{app.capitalize()} launched successfully."

    except FileNotFoundError:
        logging.error(f"Executable not found: {path}")
        return f"Executable not found: {path}"
    except Exception as e:
        logging.exception("Failed to open app")
        return f"Failed to open {app}: {e}"
