# Note Selection
## Navigating/Selecting notes with the keyboard

[tab]{.kbd} selects the next note in a MIDI region, while [tab]{.kbd
.mod1} selects the previous note. Holding down the []{.kbd .mod3} key as
well prevents previously visited notes from being deselected.

## Selecting notes with the mouse

While in [Internal Edit Mode](@@toolbox), any note can be clicked on to
select it. Once a note has been selected, [left]{.kbd .mouse
.mod3}-clicking on another note selects all notes between the first note
selected and the second one. Adding or removing a note to or from the
selection is done by [left]{.kbd .mouse .mod1}-clicking it. Clicking and
dragging outside of a note will [rubberband select]{.dfn} any notes
enclosed by the selection rectangle; holding down the []{.kbd .mod3n}
key will prevent any previously selected notes from being deselected.

In any mode, [left]{.kbd .mod3 .mouse}-clicking on a note on the
Scroomer (the piano header of the track, see [MIDI Track
Controls](@@midi-track-controls)) will add all occurrences of that note
to the selection, while [middle]{.kbd .mouse}-clicking will only
select/deselect all occurrences of that note, clearing the previous
selection. Scroomer selections work on all MIDI regions of a track at
once.

## Listening to Selected Notes

If [Edit \> Preferences \> MIDI \> Sound MIDI notes as they are
selected]{.kbd .menu} is enabled, Ardour will send a pair of
NoteOn/NoteOff messages through the track as notes are selected.
Assuming there is an appropriate device or synthesizer attached to the
track, these should be audible.
