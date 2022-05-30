import mido
import sys
from inputs import get_input
from controls import process_message


if __name__ == "__main__":
    auto_input = None
    if "--auto" in sys.argv:
        auto_input = "Arturia MiniLab mkII"

    with mido.open_input(get_input(auto_input)) as inport:
        for message in inport:
            process_message(message)
