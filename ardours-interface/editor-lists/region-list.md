# The Regions List
The Regions list shows all the regions in the session, with infos about
them in a tabular form. Any column caption can be clicked to sort the
list according to the clicked value:

|        |                                                               |
|--------|---------------------------------------------------------------|
| Name   | The name of the region, can be modified by double-clicking it |
| \# Ch  | Number of channels for an audio region (0 for MIDI)           |
| Tags   | User-added tag text, can be modified by double clicking it    |
| Start  | position of the start of the region on the global timeline    |
| Length | duration of the region                                        |

The time format used for *Start* and *Length* follows the [Primary
Clock](@@editing-clocks) one.

At the right of the list are three columns of flags that can be altered:

|  |  |
|----|----|
| □ L | whether the region position is locked, so that it cannot be moved. |
| □ M | whether the region is muted, so that it will not be heard. |
| □ O | whether the region is opaque; opaque regions 'block' regions below them from being heard, whereas 'transparent' regions have their contents mixed with whatever is underneath. |

Hovering the mouse pointer over a column heading shows a tool-tip which
can be handy to remember what the columns are for.

A handy feature of the region list is that its regions can be dragged
and dropped into a suitable track in the session.
