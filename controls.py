from volume import volume_up, volume_down, mute_toggle
from brightness import brightness_up, brightness_down, lock_screen
from launch import launch


INFINITE = "infinite"
TOGGLE = "toggle"
SLIDER = "slider"
LAUNCH = "launch"


CONTROL_TYPES = [
    INFINITE,
    TOGGLE,
    SLIDER,
    LAUNCH
]


CONTROLS = {
    "VOLUME": {
        "id": 112,
        "type": INFINITE,
        "threshold": 64,
        "up_fn": volume_up,
        "down_fn": volume_down
    },
    "MUTE": {
        "id": 113,
        "type": TOGGLE,
        "press_fn": mute_toggle
    },
    "BRIGHTNESS": {
        "id": 114,
        "type": INFINITE,
        "threshold": 64,
        "up_fn": brightness_up,
        "down_fn": brightness_down
    },
    "LOCK": {
        "id": 115,
        "type": TOGGLE,
        "press_fn": lock_screen
    },
    "OBSIDIAN": {
        "id": 36,
        "channel": 9,
        "type": LAUNCH,
        "app": "Obsidian"
    },
    "BRAVE": {
        "id": 37,
        "channel": 9,
        "type": LAUNCH,
        "app": "Brave"
    },
    "SLACK": {
        "id": 38,
        "channel": 9,
        "type": LAUNCH,
        "app": "Slack"
    },
    "ITERM": {
        "id": 39,
        "channel": 9,
        "type": LAUNCH,
        "app": "iTerm"
    },
}


def find_control(message):
    for name, attributes in CONTROLS.items():
        if message.is_cc():
            if attributes["id"] == message.control:
                return name, attributes
        elif message.type == "note_on":
            if (attributes["id"] == message.note
                    and attributes["channel"] == attributes["channel"]):
                return name, attributes
    return None, None


def process_infinite(name, attributes, message):
    if message.value > attributes["threshold"]:
        attributes["up_fn"]()
    if message.value < attributes["threshold"]:
        attributes["down_fn"]()


def process_toggle(name, attributes, message):
    if message.value == 127:
        if "press_fn" in attributes:
            attributes["press_fn"]()
    if message.value == 0:
        if "unpress_fn" in attributes:
            attributes["unpress_fn"]()


def process_launch(_name, attributes, _message):
    launch(attributes["app"])


def process_message(message):
    name, attributes = find_control(message)
    if name:
        if attributes["type"] == INFINITE:
            process_infinite(name, attributes, message)
        elif attributes["type"] == TOGGLE:
            process_toggle(name, attributes, message)
        elif attributes["type"] == LAUNCH:
            process_launch(name, attributes, message)
