import mido


def get_inputs():
    return mido.get_input_names()


def get_input(default=None):
    available_inputs = get_inputs()
    if not available_inputs:
        print("No available inputs. Exiting.")
        exit(-1)

    if default is not None:
        return default

    print("Available Inputs:")
    for index, input_name in enumerate(available_inputs):
        print(f"\t{index}. {input_name}")

    return available_inputs[int(input("Select an Input (number): "))]
