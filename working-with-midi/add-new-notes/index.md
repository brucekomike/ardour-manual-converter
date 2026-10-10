# Adding New Notes
MIDI notes can be added a few different ways in Ardour:

## Using the mouse
{#add-new-notes-using-the-mouse}

Drawing notes with the mouse requires that a MIDI track
[exists](@@create-midi-tracks), and a blank MIDI region has been
[created](@@create-midi-regions) in this track.

In the *Draw* [Mode](@@toolbox) new notes can be added with a click or a
click-and-drag: a mouse *click* creates a note at the pointer location
(or the nearest grid anchor if grid is enabled), and its duration is one
[Grid unit](@@grid-controls). A mouse *drag* creates the note like a
click does, but allows continuously setting the duration of the note
until the mouse button is released.

It\'s also possible to *brush notes* by pressing [Shift]{.kbd},
clicking, and dragging to the right. New notes will be painted at an
interval defined by global quantization ([Edit \> Snap & Grid \> Global
Quantization]{.kbd .menu}), with the length defined in the editor
toolbar (see below).

The toolbar available in the [Draw]{.dfn} mode helps drawing notes of
exact length, in a certain MIDI channel, with predefined velocity:

![MIDI draw toolbar](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/midi-draw-toolbar.png){style="width:75%"}

While the [Velocity]{.dfn} drop-down list only displays presets, you can
hover it and use mouse wheel scrolling to increment the current value
by 1. Scrolling above the other two drop-down lists will cycle through
the presets.

The [Auto]{.dfn} option in three drop-down lists works differently in
all three cases:

|          |                                                                                                                                                                              |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Length   | The length will be defined by the grid snapping setting                                                                                                                      |
| Channel  | This value will be inherited from the closest note                                                                                                                           |
| Velocity | The value will be an interpolation between two closest notes, the position of the newly added note relative to either of the two notes will also be taken into consideration |

## Using Step Entry
{#add-new-notes-using-step-entry}

The [Step Entry editor](@@step-entry) allows to enter a melody in
sequence along time, using a virtual keyboard and specific controls. It
can be a very handy and fast way to create MIDI lines, in a kind of
typewriter way, all the more when using its different keyboard
shortcuts.

The Step Entry window is shown by [right]{.kbd .mouse} clicking the
record button in the [MIDI track header](@@midi-track-controls) and
selecting [Step Entry]{.kbd .menu}. This will automatically create a
MIDI region to type into at the playhead position, which will
automatically expand at each step.

## Using the Virtual Keyboard
{#add-new-notes-using-the-virtual-keyboard}

The [Virtual MIDI Keyboard](@@virtual-keyboard) --- or a real MIDI
keyboard plugged in as the tracks input --- can be used to record MIDI,
as a microphone would record audio.

It can be started by choosing the [Window \> Virtual Keyboard]{.kbd
.menu} menu. Exactly like for audio recording, the track(s) must be
armed for recording, the main record engaged, then the transport
started. As for the Step Entry, a MIDI region will be auto-generated at
the playhead position, and expanded as long as the recording lasts.

```{toctree}
/working-with-midi/handle-overlapping-notes
/editing-and-arranging/edit-midi/note-selection
/working-with-midi/note-cut-copy-and-paste
/working-with-midi/note-splitting-joining
/working-with-midi/chords
/editing-and-arranging/editing-midi/changing-note-properties
/editing-and-arranging/editing-midi/editing-velocity
/working-with-midi/patch-change
/working-with-midi/copy-midi-region
/working-with-midi/quantize-midi
/working-with-midi/transpose-midi
/working-with-midi/key-scale-tuning-system
/midi-list-editor
/working-with-midi/transformation-midi
```
