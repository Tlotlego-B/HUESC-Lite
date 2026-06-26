def load_plugins(plugin_name):
    try:
        module = __import__(f"plugins.{plugin_name}", fromlist=["run"])
        if hasattr(module, "run"):
            return module.run()
        return f"Plugin '{plugin_name}' does not have a run() function."
    except ModuleNotFoundError:
        return f"Plugin '{plugin_name}' not found."
    except Exception as e:
        return f"Error loading plugin '{plugin_name}': {e}"
