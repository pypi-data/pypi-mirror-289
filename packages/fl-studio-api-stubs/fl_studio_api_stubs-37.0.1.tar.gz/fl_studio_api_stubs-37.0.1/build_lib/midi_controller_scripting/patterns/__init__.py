"""
# Patterns

Allows you to control and interact with FL Studio Patterns.

## Contents

* [Properties](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/patterns/properties):
  functions for accessing properties of patterns.

* [Groups](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/patterns/groups):
  functions for controlling pattern groups.

* [Performance](https://il-group.github.io/FL-Studio-API-Stubs/midi_controller_scripting/patterns/performance):
  functions for interacting with performance mode patterns.

## Note

* Patterns are 1-indexed, with a range from `1` - `999`, meaning that the
  1000th pattern cannot be created.

* Multiple patterns can be selected, but only one pattern is considered to be
  the active pattern (indicated by an arrow to the left of its entry in the
  pattern picker).
"""
from .__properties import (
    patternNumber,
    patternCount,
    patternMax,
    getPatternName,
    setPatternName,
    getPatternColor,
    setPatternColor,
    getPatternLength,
    jumpToPattern,
    findFirstNextEmptyPat,
    isPatternSelected,
    selectPattern,
    selectAll,
    deselectAll,
    burnLoop,
    isPatternDefault,
    clonePattern,
    getChannelLoopStyle,
    setChannelLoop,
)
from .__performance import (
    getBlockSetStatus,
    ensureValidNoteRecord,
)
from .__groups import (
    getActivePatternGroup,
    getPatternGroupCount,
    getPatternGroupName,
    getPatternsInGroup,
)


__all__ = (
    'patternNumber',
    'patternCount',
    'patternMax',
    'getPatternName',
    'setPatternName',
    'getPatternColor',
    'setPatternColor',
    'getPatternLength',
    'jumpToPattern',
    'findFirstNextEmptyPat',
    'isPatternSelected',
    'selectPattern',
    'selectAll',
    'deselectAll',
    'burnLoop',
    'isPatternDefault',
    'getBlockSetStatus',
    'ensureValidNoteRecord',
    'clonePattern',
    'getChannelLoopStyle',
    'setChannelLoop',
    'getActivePatternGroup',
    'getPatternGroupCount',
    'getPatternGroupName',
    'getPatternsInGroup',
)
