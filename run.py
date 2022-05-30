import mido
import sys
from inputs import get_input
from controls import process_message
from threading import Thread


if __name__ == "__main__":
    try:
        auto_input = None
        quiet = False
        if "--auto" in sys.argv or "-a" in sys.argv:
            auto_input = "Arturia MiniLab mkII"
        if "--quiet" in sys.argv or "-q" in sys.argv:
            quiet = True

        with mido.open_input(get_input(auto_input)) as inport:
            for message in inport:
                Thread(target=process_message, args=(message, quiet)).start()
    except KeyboardInterrupt:
        exit(0)
