"""
Window indexes are used by many [window-related functions](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/ui/windows)
within the FL Studio API to refer to FL Studio's primary windows.

These constants all begin with the `wid` prefix.

```py
import ui
import midi

if ui.getFocused(midi.widMixer):
    print("Mixer window is open")
else:
    ui.setFocused(midi.channelRack)
    print("Opened the channel rack window")
```
"""


widMixer = 0
"""
Mixer window.
"""

widChannelRack = 1
"""
Channel rack window.
"""

widPlaylist = 2
"""
Playlist window.
"""

widPianoRoll = 3
"""
Piano roll window.
"""

widBrowser = 4
"""
Content browser window.
"""

widPluginEffect = 6
"""
Effect plugin window. This index is returned by [ui.getFocused()](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/ui/windows#ui.__windows.getFocused)
if any effect plugin is focused.

Note that this cannot be used for activating windows. To activate an effect
plugin window, use [mixer.focusEditor()](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/mixer/properties#mixer.__properties.focusEditor).
"""

widPluginGenerator = 7
"""
Generator (instrument) plugin window. This index is returned by
[ui.getFocused()](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/ui/windows#ui.__windows.getFocused) if any generator plugin is focused.

Note that this cannot be used for activating windows. To activate a generator
plugin window, use [channels.focusEditor()](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/channels/ui#channels.__ui.focusEditor).
"""
