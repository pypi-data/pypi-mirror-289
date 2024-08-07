"""
The overlay functions in the `ui` module can be used to produce overlays on
parts of FL Studio's interface in order to indicate the state of a MIDI
controller. For example, if a user selected a track on the mixer, a script
could use [ui.miDisplayRect()](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/ui/overlays#ui.__overlays.miDisplayRect) to highlight nearby tracks and show
which tracks can be controlled using the MIDI controller. This is especially
useful if your script changes its links dynamically based on the user's
selection.
"""


def crDisplayRect(
    left: int,
    top: int,
    right: int,
    bottom: int,
    duration: int,
    flags: int = 0,
) -> None:
    """
    Displays a selection rectangle on the channel rack.

    This rectangle is anchored using the top left corner, and a width and
    height.

    Subsequent calls to this function will remove previously displaying
    rectangles.

    ## Args

    * `left` (`int`): left position.

    * `top` (`int`): top position.

    * `width` (`int`): horizontal width.

    * `height` (`int`): vertical height.

    * `duration` (`int`): duration to display for (in ms). Or,
          * use `midi.MaxInt` to show indefinitely.

          * use `0` to hide.

    * `flags` (`int`, optional): a bitwise combination of:
          * `CR_HighlightChannels`: Display on channel list rather than on
            grid.

          * `CR_ScrollToView`: Scroll channel rack to specified position.

    Included since API version 1.
    """


def miDisplayRect(
    start: int,
    end: int,
    duration: int,
    flags: int = 0,
) -> None:
    """
    Displays a selection rectangle on the mixer.

    Subsequent calls to this function will remove previously displaying
    rectangles.

    ## Args

    * `start` (`int`): start track index.

    * `end` (`int`): end track index.

    * `duration` (`int`): duration to display for (in ms). Or,
          * use `midi.MaxInt` to show indefinitely.

          * use `0` to hide.

    * `flags` (`int`, optional): unknown.

    Included since API version 13.
    """


def miDisplayDockRect(
    start: int,
    length: int,
    dock_side: int,
    time: int,
) -> None:
    """
    Display a red guide rectangle on the mixer, but contained to one side of
    the dock.

    Compare to: `miDisplayRect()`.

    ## Args

    * `start` (`int`): the index of the starting point, with `1` being the 1st
      track to be docked to that side, and `5` being the 5th track docked to
      that side.

    * `length` (`int`): the length of the rectangle to display, for example `1`
      means the rectangle will be `1` track wide.

    * `dock_side` (`int`): the dock side to show the rectangle on:
          * `0`: left.

          * `1`: middle.

          * `2`: right.

    * `time` (`int`): the amount of time to display the rectangle for, or
      `midi.MAXINT` to display indefinitely and `0` to turn off.

    Included since API Version 20.
    """
