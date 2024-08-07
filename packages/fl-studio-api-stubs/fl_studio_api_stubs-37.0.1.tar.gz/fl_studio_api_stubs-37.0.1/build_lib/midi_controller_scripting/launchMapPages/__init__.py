"""
# Launchmappages

Launchmaps are custom files that provide different behavior for a controller
depending on what page it is currently set to display. See the MIDI Controller
reference post on
[Custom controller layouts](https://forum.image-line.com/viewtopic.php?f=1914&t=92193).
for more information.

Each page should be placed in a `Page[number].scr` file in the top directory of
the script. For example, if a script has 2 pages, it would have two files:

* `Page1.scr`
* `Page2.scr`
"""
from fl_classes import FlMidiMsg


def init(deviceName: str, width: int, height: int) -> None:
    """
    Initialise launchmap pages.

    ## Args

    * `deviceName` (`str`): ???

    * `width` (`int`): ???

    * `height` (`int`): ???

    Included since API version 1.
    """


def createOverlayMap(
    offColor: int,
    onColor: int,
    width: int,
    height: int,
) -> None:
    """
    Creates an overlay map.

    ## Args

    * `offColor` (`int`): ?

    * `onColor` (`int`): ?

    * `width` (`int`): ?

    * `height` (`int`): ?

    Included since API version 1.
    """


def length() -> int:
    """
    Returns launchmap pages length.

    ## Returns

    * `int`: length.

    Included since API version 1.
    """
    return 0


def updateMap(index: int) -> None:
    """
    Updates launchmap page at `index`.

    ## Args

    * `index` (`int`): index of page to update.

    Included since API version 1.
    """


def getMapItemColor(index: int, itemIndex: int) -> int:
    """
    Returns item color of `itemIndex` in map `index`.

    ## Args

    * `index` (`int`): map index.

    * `itemIndex` (`int`): item index.

    ## Returns

    * `int`: color.

    Included since API version 1.
    """
    return 0


def getMapCount(index: int) -> int:
    """
    Returns the number of items in page at `index`.

    ## Args

    * `index` (`int`): page index.

    ## Returns

    * `int`: number of items.

    Included since API version 1.
    """
    return 0


def getMapItemChannel(index: int, itemIndex: int) -> int:
    """
    Returns the channel for item at `itemIndex` on page at `index`.

    ## Args

    * `index` (`int`): page index.

    * `itemIndex` (`int`): item index.

    ## Returns

    * `int`: channel number.

    Included since API version 1.
    """
    return 0


def getMapItemAftertouch(index: int, itemIndex: int) -> int:
    """
    Returns the aftertouch for item at `itemIndex` on page at `index`.

    ## Args

    * `index` (`int`): page index.

    * `itemIndex` (`int`): item index.

    ## Returns

    * `int`: aftertouch value.

    Included since API version 1.
    """
    return 0


def processMapItem(
    eventData: FlMidiMsg,
    index: int,
    itemIndex: int,
    velocity: int,
) -> None:
    """
    Process map item at `itemIndex` of page at `index`

    ## Args

    * eventData (`eventData`): event data.

    * index (`int`): page index.

    * itemIndex (`int`): item index.

    * velocity (`int`): velocity.

    Included since API version 1.
    """


def releaseMapItem(eventData: FlMidiMsg, index: int) -> None:
    """
    Release map item at `itemIndex` of page at `index`.

    ## HELP WANTED
    This doesn't seem quite right, there is no `itemIndex` argument.

    ## Args

    * `eventData` (`eventData`): event data.

    * `index` (`int`): page index.

    Included since API version 1.
    """


def checkMapForHiddenItem() -> None:
    """
    Checks for launchpad hidden item???

    ## HELP WANTED
    What does this do?

    Included since API version 1.
    """


def setMapItemTarget(index: int, itemIndex: int, target: int) -> int:
    """
    Set target for item at `itemIndex` of page at `index`.

    ## Args

    * `index` (`int`): page index.

    * `itemIndex` (`int`): item index.

    * `target` (`int`): ????

    ## Returns

    * `int`: ????

    Included since API version 1.
    """
    return 0


# Clean up imports
del FlMidiMsg
