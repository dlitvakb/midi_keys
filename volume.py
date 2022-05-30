from osascript import osascript


def get_current_volume():
    raw = osascript("get volume settings")
    try:
        output_volume = int(raw[1].split(", ")[0].split(":")[1])
        return output_volume
    except ValueError:
        return None


def is_muted():
    raw = osascript("get volume settings")
    return raw[1].split(", ")[-1].split(":")[1] == "true"


def volume_up():
    current_volume = get_current_volume()
    if current_volume is None:
        print("Volume could not be set")
        return
    next_volume = current_volume + 10 if current_volume + 5 < 100 else 100
    osascript(f"set volume output volume {next_volume}")
    return next_volume


def volume_down():
    current_volume = get_current_volume()
    if current_volume is None:
        print("Volume could not be set")
        return
    next_volume = current_volume - 10 if current_volume + 5 > 0 else 0
    osascript(f"set volume output volume {next_volume}")
    return next_volume


def mute_toggle(_name, _attributes, _quiet):
    if is_muted():
        osascript("set volume without output muted")
    else:
        osascript("set volume with output muted")
