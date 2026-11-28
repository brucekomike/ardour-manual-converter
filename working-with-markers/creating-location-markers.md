# Location Markers
[Location Markers]{.dfn} appear in the [Locations Markers](@@ruler)
ruler at the top of the timeline. They have multiple uses, most
commonly --- for navigation in a session, e.g. where this or that
instrument should start/stop playing. Custom markers can be created at
any position in a session.

The [start]{.dfn style="background-color:limegreen;"} and [end]{.dfn
style="background-color:limegreen;"} markers, that define the length of
the session, appear automatically once any content has been added to the
session (either recorded or imported). The end marker automatically
shifts to the right once more material gets added.

## Creating Location Markers

There are multiple ways to create custom markers at the current playhead
position:

- using the keyboard shortcut (default is [Tab]{.kbd})
- using the [Transport \> Markers \> Add Mark from Playhead]{.kbd .menu}
  menu.

Adding a marker at an arbitrary location on the timeline (i.e. not at
the playhead position) can also be done either by:

- [right]{.kbd .mouse} clicking in the Location Marker ruler, and
  selecting [Add \> Location Marker]{.kbd .menu}
- using the [Ranges & Marks List](@@the-ranges-and-marks-lists),
  clicking [New Marker]{.kbd .menu} and using the [clock
  widget](@@editing-clocks) to set its position.

## Moving Location Markers

[Left]{.kbd .mouse}-clicking and dragging moves a single marker to a new
location on the timeline.

It is possible to move multiple markers by the same distance.
[Left]{.kbd .mouse .mod1}-clicking each marker creates a selection of
markers that can be dragged left or right together.

## Renaming Location Markers

There are three ways to rename a location marker:

1.  Double-click on a marker opens a dialog where a new name can be
    submitted.
2.  Right-clicking on a marker and selecting [Rename....]{.kbd .menu}
    opens a dialog where a new name can be submitted.
3.  Editing and confirming the name by pressing [Enter]{.kbd .button} in
    an entry box in the *Ranges & Marks* sidebar.

## Removing Location Markers

There are three ways to remove a location marker:

1.  Hovering the marker and pressing [Enter]{.kbd .button}.
2.  Right-clicking on a marker and selecting [Remove]{.kbd .menu}.
3.  Clicking the [x]{.kbd .button} for a marker of choice in the
    *Ranges & Marks* sidebar.

## More Options

The context (right-click) menu for location markers has more options
than the ones mentioned above:

|  |  |
|----|----|
| Locate to Here | Moves the playhead to the selected marker. |
| Play from Here | Moves the playhead to the selected marker and starts playback. |
| Move Mark to Playhead | This changes the position of the selected marker to that of the playhead. |
| Create Range to next Marker | This creates a pair of range markers between the selected marker and the next one to the right on the timeline. |
| Promote to Time Origin | This makes the position of the chosen range marker the origin time. This is mostly useful when the *Display delta to origin marker* clock mode is enabled to display the difference between current playhead position and the origin time. Absolute time stays unaffected. |
| Hide | This hides the selected marker from the ruler until the user chooses to unhide it. |
| Rename... | This opens a dialog to rename the marker. |
| Lock | This prevents a marker from being accidentally moved elsewhere. |
