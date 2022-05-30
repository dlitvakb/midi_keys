import subprocess
from osascript import osascript


def get_current_brightness():
    output = subprocess.run(
        ["brightness", "-l"], check=True, text=True, stdout=subprocess.PIPE
    )

    for line in output.stdout.split("\n"):
        if "brightness" in line:
            return float(line.split(" ")[-1])
    return None


def brightness_down():
    current_brightness = get_current_brightness()
    if current_brightness is not None:
        next_brightness_level = (
            current_brightness - 0.1 if current_brightness - 0.1 > 0 else 0
        )
        subprocess.run(
            ["brightness", f"{next_brightness_level}"],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        )


def brightness_up():
    current_brightness = get_current_brightness()
    if current_brightness is not None:
        next_brightness_level = (
            current_brightness + 0.1 if current_brightness + 0.1 < 1.0 else 1
        )
        subprocess.run(
            ["brightness", f"{next_brightness_level}"],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        )


def lock_screen(_name, _attributes, _quiet):
    osascript('tell application "Finder" to sleep')
