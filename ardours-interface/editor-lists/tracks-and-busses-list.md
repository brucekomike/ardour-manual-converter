# The Tracks and Busses List
This lists the tracks and busses that are present in the session. The
list order reflects the order in the editor, and track or bus names can
be dragged-and-dropped in the editor list to re-order them in the
editor. The columns in the list represent the following:

|  |  |
|----|----|
| V | Whether the track or bus is visible; they can be hidden, in which case they will still play, but just not be visible in the editor; this can be useful for keeping the display uncluttered. |
| C | Whether the track is visiable on the Cue page, in which case it can be used for non-linear sequencing in the Cue window, but any content in the track visible in the Editor window will not be played. |
| A | Whether the track or bus is active; inactive tracks will not play, and will not consume any CPU. |
| I | For MIDI tracks, whether the MIDI input is enabled; this dictates whether MIDI data from the track\'s input ports will be passed through the track. |
| R | Whether the track is record-enabled. |
| RS | Whether the track is record safe; a record safe track cannot be armed for recording, to protect against a mistake. |
| M | Whether the track is muted. |
| S | Track solo state. |
| SI | Track solo-isolated state. |
| SS | Solo safe state. |

Each icon in these columns can be clicked to toggle the track/bus state,
which is a very fast way to set multiple tracks/busses state at once.

As with the region list, hovering the mouse pointer over a column
heading shows a tool-tip which can be handy to remember what the columns
are for.
