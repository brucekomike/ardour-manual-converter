# Range Markers
[Range markers]{.dfn} are essentially two [location
markers](@@creating-location-markers) that appear in the [Range
Markers](@@ruler) ruler, and are grouped together to mark the beginning
and end of a section on the timeline.

Ardour combines regular range markers, loop ranges, and punch ranges in
the same Range Markers ruler.

## Creating a Range on the Timeline
{#creating-range-on-timeline}

There are multiple ways to create range markers:

-   [Right]{.kbd .mouse}-clicking on the Range Markers ruler at the top
    of the timeline, then selecting [Add \> Range]{.kbd .menu}. For loop
    ranges and punch ranges, please select [Add \> Loop Range]{.kbd
    .menu} and [Add \> Punch Range]{.kbd .menu} respectively.
-   Selecting a range in the Editor window, then [right]{.kbd
    .mouse}-clicking and selecting [Add Range Markers]{.kbd .menu}, [Set
    Loop from Selection]{.kbd .menu} or [Set Punch from Selection]{.kbd
    .menu}.
-   Clicking [New Range]{.kbd .button} button at the bottom of the
    [Ranges & Marks]{.kbd .window} sidebar. The markers will be created
    around the playhead position, unless the playhead in at the time
    origin (in which case the markers will be placed at the time origin
    position).
-   [Right]{.kbd .mouse}-clicking a location or a CD marker and
    selecting [Create Range to Next Marker]{.kbd .menu}. This will
    create a pair of range markers that start at the selected marked and
    end at the position of the next location or CD marker (both rulers
    are taken into account).

## Editing a Range
{#editing-range}

Both markers of a range can be independently moved along the timeline by
clicking and dragging them to the desired location. They can also be
moved together by []{.kbd .mod2n}-dragging one of the markers.

Any pair or range markers, including session start/end markers, can be
repositioned to the extents of an existing range selection on the
timeline by [right]{.kbd .mouse}-clicking on either of the markers and
selecting [Set Range from Selection]{.kbd .menu} in the menu.

### Renaming Range Markers

Ardour provides several ways to rename an existing pair of range
markers:

-   Double-clicking either of the two range markers will show a dialog
    for setting a new caption for the markers.
-   The same can be achieved by right-clicking on either of the markers
    and selecting the [Rename Range...]{.kbd .menu} menu item.
-   Additionally, the name can be edited in the [Ranges & Marks]{.kbd
    .window} sidebar.

## Removing Range Markers

Range markers can be deleted in several ways:

-   By clicking on one of the markers and pressing the [Del]{.kbd} key.
-   By right-clicking on one of the markers and selecting [Remove
    Range]{.kbd .menu}.
-   By clicking the markers\' [x]{.kbd .button} button in the *Ranges &
    Marks* sidebar.

Additionally, all ranges can be removed at once by [right]{.kbd
.mouse}-clicking on an empty part of the Range Markers ruler and
selecting the [Clear All Ranges]{.kbd .menu} menu item.

## More Options

The context (right-click) menu for range markers has more options than
the ones mentioned above:

|                           |                                                                                                                                                                                                                                                                            |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Play Range                | Starts playback at the left marker in the pair and stops at the right marker.                                                                                                                                                                                              |
| Locate to Marker          | Moves the playhead to the selected marker.                                                                                                                                                                                                                                 |
| Play from Marker          | Moves the playhead to the selected marker and starts playback.                                                                                                                                                                                                             |
| Loop Range                | Creates a loop range off the selected range markers pair and starts playback.                                                                                                                                                                                              |
| Set Marker from Playhead  | Changes the position of the selected marker to that of the playhead.                                                                                                                                                                                                       |
| Zoom to Range             | Changes the zoom so that the area defined by the range markers would be maximized yet visible entirely within Ardour\'s window.                                                                                                                                            |
| Loudness Assistant...     | Launches the Loudness Assistant to analyze the selection defined by the selected pair of range markers.                                                                                                                                                                    |
| Export Range...           | Exports the selection defined by the selected pair of range markers.                                                                                                                                                                                                       |
| Promote to Time Origin    | This makes the position of the chosen range marker the origin time. This is mostly useful when the *Display delta to origin marker* clock mode is enabled to display the difference between current playhead position and the origin time. Absolute time stays unaffected. |
| Hide Range                | This hides the range from the Range Markers ruler. Marker\'s visibility can be restored in the *Ranges & Marks* sidebar.                                                                                                                                                   |
| Separate Regions in Range | Cuts all regions crossing the positions of the range markers.                                                                                                                                                                                                              |
| Select All in Range       | Select entire regions that cross the borders of the range markers.                                                                                                                                                                                                         |
| Select Range              | Create a selection from the range markers in all selected tracks and busses.                                                                                                                                                                                               |
