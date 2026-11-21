# Punch Range
The [punch range]{.dfn} is a special range used to define where
recording will start and/or stop during a [punch]{.dfn}. Punch range
markers show up on the Region Markers ruler.

## Creating a Punch Range

A punch range can be created in multiple ways.

- By [right]{.kbd .mouse}-clicking on the Range Markers ruler at the top
  of the timeline, then selecting [Add \> Punch Range]{.kbd .menu}.
- By selecting a range on the timeline, [right]{.kbd .mouse}-clicking,
  then selecting [Set Punch from Selection]{.kbd .menu}. This will
  create punch range\'s start and end markers that match the beginning
  and the end of the range selection respectively.

## Editing a Punch Range

The punch range can be edited in multiple ways as well.

- Individual markers can be dragged on the ruler by [left]{.kbd
  .mouse}-clicking and dragging. It is also possible to drag both the
  start and the end markers togother. [Left]{.kbd .mod3 .mouse}-click
  and select both markers, then drag them.
- Positions of the start and the end markers can be edited numerically
  in the [Ranges & Marks](@@the-ranges-and-marks-lists) sidebar.
- Positions of the start and the end markers can also be reset from
  another range selection by making that selection, then [right]{.kbd
  .mod1 .mouse}-clicking and selecting the [Set Range from
  Selection]{.kbd .menu} menu item.

## Removing a Punch Range

There are two ways to delete a punch range:

1.  [Right]{.kbd .mouse}-click on one of the punch range markers and
    select the [Remove Range]{.kbd .menu} menu item.
2.  Click the [X]{.kbd} button in the list of ranges in the [Ranges &
    Marks](@@the-ranges-and-marks-lists) sidebar.

## More Options

The right-click menu mostly copies that of a regular pair of range
markers. The following options are available in addition to the ones
mentioned above.

|  |  |
|----|----|
| Play Range | Starts playback at the left marker in the pair and stops at the right marker. |
| Locate to Marker | Moves the playhead to the selected marker. |
| Play from Marker | Moves the playhead to the selected marker and starts playback. |
| Loop Range | Creates a loop range off the selected range markers pair and starts playback. |
| Set Marker from Playhead | Changes the position of the selected marker to that of the playhead. |
| Zoom to Range | Changes the zoom so that the area defined by the range markers would be maximized yet visible entirely within Ardour\'s window. |
| Loudness Assistant... | Launches the Loudness Assistant to analyze the selection defined by the selected pair of range markers. |
| Export Range... | Exports the selection defined by the selected pair of range markers. |
| Promote to Time Origin | This makes the position of the chosen range marker the origin time. This is mostly useful when the *Display delta to origin marker* clock mode is enabled to display the difference between current playhead position and the origin time. Absolute time stays unaffected. |
| Separate Regions in Range | Cuts all regions crossing the positions of the range markers. |
| Select All in Range | Select entire regions that cross the borders of the range markers. |
| Select Range | Create a selection from the range markers in all selected tracks and busses. |
