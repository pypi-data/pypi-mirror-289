"""
Mixer > Events

Functions for managing events on effects plugins
"""
import midi


def getTrackPluginId(index: int, plugIndex: int) -> int:
    """
    Returns the plugin ID of the plugin on track `index` in slot `plugIndex`.

    A plugin ID is used internally by FL Studio to represent effects present
    on the mixer. A plugin ID can be used with REC events in order to automate
    plugins, and is also the return value of
    [ui.getFocusedFormID()](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/ui/windows#ui.__windows.getFocusedFormID) if the focused window is an effect
    plugin.

    Plugin IDs are represented as `((track << 6) + index) << 16`, although
    the official documentation lists them as `(track << 6 + index) << 16`,
    which uses the order of operations incorrectly.

    ## Args

    * index (`int`): track index.

    * plugIndex (`int`): plugin index.

    ## Returns

    * `int`: plugin ID.

    Included since API version 1.
    """
    return ((index << 6) + plugIndex) << 16


def isTrackPluginValid(index: int, plugIndex: int) -> bool:
    """
    Returns whether a plugin on track `index` in slot `plugIndex` is valid
    (has been loaded, so the slot isn't empty).

    ## Args

    * `index` (`int`): track index.

    * `plugIndex` (`int`): plugin index.

    ## Returns

    * `bool`: whether a plugin is loaded at this location.

    Included since API version 1.
    """
    return False


def getEventValue(
    index: int,
    value: int = midi.MaxInt,
    smoothTarget: int = 1,
) -> int:
    """
    Returns event value from MIDI.

    ## HELP WANTED

    * What does this do?

    ## Args

     * `index` (`int`): ???

     * `value` (`int`, optional): ???. Defaults to 'MaxInt'.

     * `smoothTarget` (`int`, optional): ???. Defaults to 1.

    ## Returns

     * `int`: ???

    Included since API version 1.
    """
    return 0


def remoteFindEventValue(index: int, flags: int = 0, /) -> float:
    """
    Returns event value.

    ## HELP WANTED

    * What does this do?

    ## Args

     * `index` (`int`): ???

     * `flags` (`int`, optional): ???. Defaults to 0.

    ## Returns

     * `float`: ???

    Included since API version 1.
    """
    return 0.0


def getEventIDName(index: int, shortname: int = 0) -> str:
    """
    Returns event name for event at `index`.

    ## HELP WANTED

    * What does this do?

    ## Args

    * `index` (`int`): ???

    * `shortname` (`int`, optional): ???. Defaults to 0.

    ## Returns

    * `str`: name of event?

    Included since API version 1.
    """
    return ""


def getEventIDValueString(index: int, value: int) -> str:
    """
    Returns event value as a string.

    ## HELP WANTED

    * What does this do?

    ## Args:
    * `index` (`int`): ???

    * `value` (`int`): ???

    ## Returns

    * `str`: ???

    Included since API version 1.
    """
    return ""


def getAutoSmoothEventValue(index: int, locked: int = 1) -> int:
    """
    Returns auto smooth event value.

    ## HELP WANTED

    * What does this do?

    ## Args

    * `index` (`int`): ???

    * `locked` (`int`, optional): ???. Defaults to 1.

    ## Returns

    * `int`: ???

    Included since API version 1.
    """
    return 0


def automateEvent(
    index: int,
    value: int,
    flags: int,
    speed: int = 0,
    isIncrement: int = 0,
    res: float = midi.EKRes,
) -> int:
    """
    Automate event.

    ## HELP WANTED

    * What does this do?

    ## Args

    * `index` (`int`): ???

    * `value` (`int`): ???

    * `flags` (`int`): refer to the [FL Studio manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#RecEventFlags).

    * `speed` (`int`, optional): ???. Defaults to 0.

    * `isIncrement` (`int`, optional): ???. Defaults to 0.

    * `res` (`float`, optional): ???. Defaults to `midi.EKRes`.

    ## Returns

    * `long`: ???

    Included since API version 1.
    """
    return 0
