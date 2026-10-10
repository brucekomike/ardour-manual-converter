# MIDI Track Controls
A MIDI track has the same basic controls as an [audio
track](@@audio-track-controls), with a number of differences.

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/typical-midi-track-controls.png" class="mini"
style="width:200px;" alt="A MIDI track header" />
<figcaption>MIDI track header</figcaption>
</figure>

1.  The level meters for the track\'s outputs show MIDI output in
    [red]{style="color:red;"}, on the left; Audio output in
    [green]{style="color:green;"}, on the right
2.  The [Scroomer]{.dfn}, a combined scroll and zoom widget for
    controlling MIDI notes display range, is unique to MIDI tracks
3.  An External MIDI Device combobox can appear, for selecting
    [MIDNAMs](@@patch-change#midnam)
4.  An External Device Mode combobox can appear, for selecting an
    external device\'s mode, in case no relevant External MIDI Device
    has been selected

To show the full set of MIDI track controls, the [track
height](@@track-height) must be increased beyond the default height.
MIDI tracks will show only a few of the control elements when there is
insufficient vertical space. As for [Audio
tracks](@@audio-track-controls), this can be done by either toggling the
track\'s full screen mode ([Track \> Height \> Fit selection
(Vertical)]{.kbd .menu}, default : [F]{.kbd}, or by simply
double-clicking an empty space in the track header, to increase the
track\'s height.\
Further, the External MIDI Device and External Device Mode comboboxes
will **not** appear if there is a synth plugin on the track that comes
with an associated [MIDNAM](@@patch-change#midnam).

## The Scroomer

The Scroomer performs the following functions:

-   The scrollbar controls the range of pitches that are visible on the
    track, as visualized by the piano keyboard. Dragging the body of the
    scrollbar up and down displays higher or lower pitches.
-   Dragging the scrollbar handles zooms in and out and increases or
    decreases the range of visible pitches.
-   Double clicking the scrollbar auto-adjusts the zooms to make the
    range of visible pitches fit the actual content of the track.
-   Clicking on the piano plays the corresponding MIDI note for
    reference.
-   [left]{.kbd .mouse .mod3} clicking on a note adds the note to the
    selection (for all regions on the track). See [Note
    Selection](@@note-selection).
-   [middle]{.kbd .mouse} clicking a note clears the selection, selects
    only the note.

Scroomer\'s user interface looks lightly differently depending on the
currently selected tool. For most tools, the UI is the same as on the
screenshot above. However, when either the Draw or the Edit tool is
selected, the scroomer will additionally display notes (e.g. 048 C, 049
C#):

![Notes in the scroomer](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/scroomer-notes.png){width="50%"}

If a virtual instrument loaded into the MIDI track provides MIDNAM data,
Ardour will read and display note names rather than notes:

![Note names in the
scroomer](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/scroomer-note-names.png){width="50%"}

You can configure Ardour to always show note names when they are
available or never show them. The setting is on the [Appearance \>
Editor]{.kbd .menu} page of the Preferences dialog.

The extent to which scroomer can zoom into the pianoroll depends on the
maximum size of a note cell. This setting is available on the
[MIDI]{.kbd .menu} page of the Preferences dialog.

## Channel and Patch Selection

### The Channel Selector

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/midi-chan-sel-dlg.png" width="300"
alt="The MIDI channel control window" />
<figcaption>The MIDI channel control window.</figcaption>
</figure>

A MIDI track\'s data may utilize any number of the 16 available [MIDI
channels]{.dfn}, and it is useful to be able to filter out a subset of
those or force the input or output to utilize only certain channels. The
Channel Selector dialog allows for filtering or modification of both the
input and output of any given MIDI track.

The Channel Selector dialog is activated by [right]{.kbd
.mouse}-clicking on a MIDI track\'s header and selecting [Channel
Selector\...]{.kbd .menu} from the menu that appears. Filtering or
modification of Inbound MIDI events for the given MIDI track is done by
selecting among:

-   [Record only selected channels]{.kbd .menu}
-   [Force all channels to 1 channel]{.kbd .menu}

Selecting [Record all channels]{.kbd .menu} does no filtering of inbound
MIDI events.

If simple filtering of incoming MIDI events is desired, [Record only
selected channels]{.kbd .menu} should be selected. A 1-by-16 grid of
squares with numbers in them will become sensitive to mouse clicks, and
the desired channels to be allowed through the filter can then be
selected by clicking on them. Channels that are allowed to pass through
will be highlighted in green.

[Force all channels to 1 channel]{.kbd .menu} will rewrite the channel
number of all incoming events of the selected MIDI track to whichever
channel is highlighted in the 1-by-16 grid of squares. When this option
is chosen, one and only one channel can be selected.

Filtering or modification of outbound MIDI events is done by selecting
among:

-   [Play only selected channels]{.kbd .menu}
-   [Use a single fixed channel for all playback]{.kbd .menu}

Selecting [Playback all channels]{.kbd .menu} does no filtering of
outbound MIDI events.

Simple filtering of outgoing MIDI events is done similarly to simple
filtering of incoming MIDI events, and is done by selecting [Play only
selected channels]{.kbd .menu}. Also similarly to the incoming case,
[Use a single fixed channel for all playback]{.kbd .menu} will rewrite
the channel number of all outgoing events of the selected MIDI track to
whichever channel is selected.

When either [Record only selected channels]{.kbd .menu} or [Playback
only selected channels]{.kbd .menu} is selected, a group of three
buttons, each appearing below their respective 1-by-16 grids, will
become sensitive to mouse clicks. They perform the following functions:

|        |                                                                                                               |
|--------|---------------------------------------------------------------------------------------------------------------|
| All    | Selects all the channels in the 1-by-16 grid above it; all the squares become lit with green                  |
| None   | Deselects all the channels in the 1-by-16 grid above it; all the squares become unlit                         |
| Invert | Any channel in the 1-by-16 grid that is lit green becomes unlit, and any unlit channel becomes lit with green |

### The Patch Selector
{#the-patch-selector .clear}

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/midi-patch-selector.png" class="mini"
alt="The Patch Selector window" />
<figcaption>The Patch Selector window.</figcaption>
</figure>

[](@@patch-change)

The Patch Selector window is an easy way to set which instrument will be
used on any of the MIDI channels. Although patches can be changed at any
time using a [patch change](@@patch-change), this dialog provides an
easy and convenient way to preview patches in software and hardware
instruments. It integrates fully with Ardour\'s support for MIDNAM
(patch definition files), so Ardour can display named programs/patches
for both General MIDI synths and those with MIDNAM files.

The window itself makes it easy to choose a channel, a bank number,
optionally choosing a bank number through its [MSB]{.dfn
title="Most Significant Byte"} and [LSB]{.dfn
title="Least Significant Byte"} numbers (CC#00 and CC#32) for large
banks, then choosing an instrument.

The keyboard at the bottom of the window allows for a quick preview of
the selected instrument, either automatically (using the buttons on top
of the keyboard) or manually by either clicking a note or using the
computer keyboard as a piano keyboard.
