from osascript import osascript


def toggle_zoom_mute(_name, _attributes, _quiet):
    osascript(
        """
        tell application "System Events"
            tell application "zoom.us" to activate
            key code 0 using {command down, shift down}
        end tell
    """
    )


def toggle_zoom_video(_name, _attributes, _quiet):
    osascript(
        """
        tell application "System Events"
            tell application "zoom.us" to activate
            key code 9 using {command down, shift down}
        end tell
    """
    )
