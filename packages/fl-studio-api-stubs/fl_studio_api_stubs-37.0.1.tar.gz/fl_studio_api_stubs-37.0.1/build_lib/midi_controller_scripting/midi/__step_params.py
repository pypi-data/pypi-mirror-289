"""
Step parameters are parameters for events within the step sequencer.

They can be controlled using [channels.getCurrentStepParam()](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/channels/sequencer#channels.__sequencer.getCurrentStepParam),
[channels.setStepParameterByIndex()](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/channels/sequencer#channels.__sequencer.setStepParameterByIndex), and other similar functions
in the [channels](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/channels) module.

```py
import channels, midi

channels.setStepParameterByIndex(
    2,  # third channel
    patterns.patternNumber(),  # current pattern
    0,  # first step
    midi.pPan,  # set panning
    128,  # 100% right
)
```
"""

pPitch = 0
"""
Step note pitch.

This is represented as a MIDI note, with the default value being middle C
(`60`, [midi.MiddleNote_Default](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/midi/miscellaneous#midi.__miscellaneous.MiddleNote_Default)).
"""

pVelocity = 1
"""
Step velocity.

This is represented as a MIDI velocity (`event.data2` in note-on `FlMidiMsg`
objects), with the default value being `100`.
"""

pRelease = 2
"""
Step release.

This is represented as a MIDI release value (`event.data2` in note-off
`FlMidiMsg` objects), with the default value being `64`.
"""

pFinePitch = 3
"""
Step fine pitch.

This value uses a range of `0` (-1200 cents) to `240` (+1200 cents). The
default value is `120` (0 cents).
"""

pPan = 4
"""
Step panning.

This value uses a range of `0` (100% left) to `128` (100% right). The default
value being `64` (centred).
"""

pModX = 5
"""
Mod-x value.
"""

pModY = 6
"""
Mod-y value.
"""

pShift = 7
"""
Note shift value.

This represents the amount to shift the note from the standard timing. The
value is measured in ticks, meaning that the number of available values depends
on the project's PPQ setting, which can be calculated using
[general.getRecPPQ()](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/general/fl_state#general.__fl_state.getRecPPQ) divided by 4 (the number of steps per beat).
"""
