from volume import volume_up, volume_down, mute_toggle
from brightness import brightness_up, brightness_down, lock_screen
from gpt import summarise_gpt
from launch import launch
from zoom import toggle_zoom_mute, toggle_zoom_video
import pyperclip


INFINITE = "infinite"
TOGGLE = "toggle"
SLIDER = "slider"
LAUNCH = "launch"


CONTROLS = {
    # OS Controls (knobs)
    "VOLUME": {
        "id": 112,
        "type": INFINITE,
        "threshold": 64,
        "up_fn": volume_up,
        "down_fn": volume_down,
    },
    "BRIGHTNESS": {
        "id": 114,
        "type": INFINITE,
        "threshold": 64,
        "up_fn": brightness_up,
        "down_fn": brightness_down,
    },
    "MUTE": {"id": 113, "type": TOGGLE, "press_fn": mute_toggle},  # top knob
    "LOCK": {"id": 115, "type": TOGGLE, "press_fn": lock_screen},  # bottom knob
    # app launchers (pads 1 - 4)
    "OBSIDIAN": {"id": 36, "channel": 9, "type": LAUNCH, "app": "Obsidian"},
    "ARC": {"id": 37, "channel": 9, "type": LAUNCH, "app": "Arc"},
    "SLACK": {"id": 38, "channel": 9, "type": LAUNCH, "app": "Slack"},
    "ITERM": {"id": 39, "channel": 9, "type": LAUNCH, "app": "iTerm"},
    # zoom controls (last 2 pads - 7 and 8)
    "ZOOM_VIDEO": {
        "id": 42,
        "channel": 9,
        "type": TOGGLE,
        "press_fn": toggle_zoom_video,
    },
    "ZOOM_AUDIO": {
        "id": 43,
        "channel": 9,
        "type": TOGGLE,
        "press_fn": toggle_zoom_mute,
    },
    # macros
    "GPT_SUMMARISE_CLIPBOARD": {
        "id": 48,  # lower C
        "channel": 0,
        "type": TOGGLE,
        "press_fn": summarise_gpt,
    },
}


def find_control(message):
    for name, attributes in CONTROLS.items():
        if message.is_cc():
            if attributes["id"] == message.control:
                return name, attributes
        elif message.type == "note_on":
            if (
                attributes["id"] == message.note
                and attributes["channel"] == message.channel
            ):
                return name, attributes
    return None, None


def process_infinite(name, attributes, message, quiet):
    if message.value > attributes["threshold"]:
        attributes["up_fn"]()
        if not quiet:
            print(name, "UP")
    if message.value < attributes["threshold"]:
        attributes["down_fn"]()
        if not quiet:
            print(name, "DOWN")


def process_toggle(name, attributes, message, quiet):
    value = message.value if message.is_cc() else message.velocity
    if value > 0:
        if "press_fn" in attributes:
            attributes["press_fn"](name, attributes, quiet)
            if not quiet:
                print(name, "PRESS")
    if value == 0:
        if "unpress_fn" in attributes:
            attributes["unpress_fn"](name, attributes, quiet)
            if not quiet:
                print(name, "UNPRESS")


def process_launch(name, attributes, _message, quiet):
    launch(attributes["app"])
    if not quiet:
        print(name, "LAUNCH")


def process_slider(_name, _attributes, _message, _quiet):
    # noop
    return None


CONTROL_TYPES = {
    INFINITE: process_infinite,
    TOGGLE: process_toggle,
    SLIDER: process_slider,
    LAUNCH: process_launch,
}


def process_message(message, quiet):
    name, attributes = find_control(message)
    if name:
        try:
            CONTROL_TYPES[attributes["type"]](name, attributes, message, quiet)
        except Exception as e:
            print(f"Error on {name}:\n{e}")
