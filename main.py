import subprocess
import sys
import os

APP_PATHS = {
    "chrome": {
        "win32": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "darwin": "open -a 'Google Chrome'",
        "linux": "google-chrome"
    },
    "spotify": {
        "win32": r"C:\Users\tebai\AppData\Roaming\Spotify\Spotify.exe",
        "darwin": "open -a Spotify",
        "linux": "spotify"
    },
    "vsc": {
        "win32": r"C:\Users\tebai\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "darwin": "open -a 'Visual Studio Code'",
        "linux": "code"
    }
}

def open_app(app_name):
    app = app_name.lower().strip()
    platform = sys.platform

    if app not in APP_PATHS:
        return f"Unknown app: '{app}'. Available: {', '.join(APP_PATHS.keys())}"

    path = APP_PATHS[app].get(platform)

    if not path:
        return f"Platform '{platform}' not supported for {app}."

    # Expand environment variables for Windows paths
    if platform == "win32":
        path = os.path.expandvars(path)

    try:
        if platform == "win32":
            subprocess.Popen([path], shell=True)
        else:
            subprocess.Popen(path, shell=True)
        return f"{app.capitalize()} launched successfully."
    except FileNotFoundError:
        return f"Executable not found for {app} at {path}"
    except Exception as e:
        return f"Failed to open {app}: {e}"
