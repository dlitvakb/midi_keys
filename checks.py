import mido
from inputs import get_input
from volume import get_current_volume, is_muted


if __name__ == "__main__":
    print(f"Volume: {get_current_volume()} - Muted: {is_muted()}")
    with mido.open_input(get_input()) as inport:
        for message in inport:
            print(message)
