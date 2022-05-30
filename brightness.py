from osascript import osascript


def brightness_down():
    osascript("tell application \"System Events\" to key code 107")


def brightness_up():
    osascript("tell application \"System Events\" to key code 113")


def lock_screen():
    osascript("tell application \"Finder\" to sleep")
