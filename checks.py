import mido
from inputs import get_input
from volume import get_current_volume, is_muted
from brightness import get_current_brightness


if __name__ == "__main__":
    print(
        f"Volume: {get_current_volume()} - Muted: {is_muted()} - Brightness: {get_current_brightness()}"
    )
    with mido.open_input(get_input()) as inport:
        for message in inport:
            print(message)
