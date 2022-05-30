from osascript import osascript


def launch(app_name):
    osascript(f"activate application \"{app_name}\"")
