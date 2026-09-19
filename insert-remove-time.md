# Insert/Remove Time
## Insert Time

The [Insert Time]{.dfn} window allows to insert blank space in the
timeline, on the selected track(s). It is accessed through the [Track \>
Insert Time]{.kbd .menu} menu.

![The Insert Time window](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/insert-time.png){width="50%"}

The Insert Time window not only allows to set the time inserted, but
also some fine-tuning options:

|                                     |                                                                                                                                                                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Insert Time starting at:            | Sets the point in the session where the time will be added. By default, it is the playhead\'s position                                                                                                                                             |
| Time to insert:                     | Duration of the blank space inserted                                                                                                                                                                                                               |
| Intersected regions should:         | A choice as to what happens to regions that exists at the Insert Time set above. See below.                                                                                                                                                        |
| Apply to all the track\'s playlists | As a track can have multiple [playlists](@@understanding-playlists), the insertion can happen either only on the active playlist or on all the playlists of this track.                                                                            |
| Move markers                        | As a [marker](@@working-with-markers) can be [locked]{.kbd .option}, this option and the two subjacent ones allow to shift the time position of those markers.                                                                                     |
| Move tempo and meter changes        | The [tempo and meter](@@tempo-and-meter) markers, that can be used to change the tempo along the session, can also be shifted in the process. Though, moving the tempo markers while e.g. keeping the MIDI regions unaffected can create oddities. |

Both the two time fields have a useful context menu, that allows to
copy/paste the time and change the display among one of the [clock
modes](@@editing-clocks). The Insert Time field also has two options to
[Set from Playhead]{.kbd .menu} (to get the insertion time from the
playhead, which is what happens by default) and [Locate to This
Time]{.kbd .menu} which moves the playhead to the time field value,
useful if the field has been manually edited to better visualize the
insertion point.

The \"Intersected regions should\" dropdown allows to select what
happens to regions that cross the insertion position:

|                                      |                                                                                                               |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [stay in position]{.dfn} *(default)* | The crossed regions are not affected by the time insertion. Only regions after the insertion point are moved. |
| [move]{.dfn}                         | The crossed regions are shifted in time.                                                                      |
| [be split]{.dfn}                     | The crossed regions are split, and the section after the time insertion point is shifted in time.             |

This last mode allows a *brute force* insertion, creating a blank space
in all the selected tracks, and replacing multiple operations.

Note: One interesting option is, if a range selection (created with in
[Range Mode](@@toolbox)) exists, it is used as the default parameters in
the window, instead of the playhead, for both the start time and
duration.

## Remove Time

The [Remove Time]{.dfn} window, accessed through the [Track \> Remove
Time]{.kbd .menu} menu, is very similar to the previous, and its options
are very similar. Only the *\"Intersected regions should\"* option is
not present.

The range selection note above can be especially useful in this context.
