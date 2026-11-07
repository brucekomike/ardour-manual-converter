# The Sources List
The Sources list shows all the original audio and MIDI files in the
session, either recorded in takes or imported from existing files. Any
column caption can be clicked to sort the list according to the clicked
value:

Name

The name of the region, can be modified by double-clicking it.

\# Ch

The number of channels, only displayed for audio files (it is 0 for MIDI
files).

Captured for

The name of the track the source was originally captured in.

\# Xruns

How many dropouts occured while capturing the source.

Tags

All the [tags](@searching-for-files-using-tags) assigned to the source.

Take ID

The unique ID of the source. Uses the timestamp for when the capturing
of source was started. E.g. `2023-10-16 14.08.58` means the capturing
started on October 16, 2023, at 2.08pm. This is only used for audio and
MIDI sources that were captured, not imported.

Orig Pos

The original position at which the capturing of the source was started.
The time format is whatever the user chose for the primary clock when
the source was captured. Switching between time formats when capturing
sources means the time format will not be the same for all captured
sources.

Path

File name of the captured or imported source.

Hovering the mouse pointer over a column heading shows a tool-tip which
can be handy to remember what the columns are for.

[right]{.kbd .mouse}-clicking on a source in the list brings up a
context menu with just one item: [Remove the selected Sources]{.kbd
.menu}. Choosing it gives several options to the user:

- Canceling the requested action and doing nothing.
- Removing just the regions that use the selected source, but not the
  sources themselves.
- Removing both the regions that use selected sources and deleting the
  selected sources. The latter action cannot be undone and requires
  using the [Session \> Cleanup \> Flush Wastebasket]{.kbd .menu}
  command to physically delete the sources.
