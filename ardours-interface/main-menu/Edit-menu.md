# The Edit Menu
The [Edit]{.dfn} menu groups together the actions related to the
edition, and so will be mostly used while in Editor mode.

```{eval-rst}
+----------------------------------+--------------------------------------------------------+
| Undo (*action*)                  | Reverts the last editing operation, namely *action*    |
+----------------------------------+--------------------------------------------------------+
| Redo                             | Does the last editing operation again, after an Undo   |
+----------------------------------+--------------------------------------------------------+
| Undo Selection Change            | Reverts the last selection operation                   |
+----------------------------------+--------------------------------------------------------+
| Redo Selection Change            | Does the last selection operation again after an Undo  |
|                                  | Selection Change                                       |
+----------------------------------+--------------------------------------------------------+
| Cut                              | Deletes the current selection, but puts it in memory   |
|                                  | ready to be pasted                                     |
+----------------------------------+--------------------------------------------------------+
| Copy                             | Copies the current selection to memory                 |
+----------------------------------+--------------------------------------------------------+
| Paste                            | Pastes the memory at the [edit                         |
|                                  | point](@@edit-point-control), after a Cut or Copy      |
|                                  | operation                                              |
+----------------------------------+--------------------------------------------------------+
| Select                                                                                    |
+----------------------------------+--------------------------------------------------------+
| Select All Objects               | Selects all the regions and automation points in the   |
|                                  | session                                                |
+----------------------------------+--------------------------------------------------------+
| Select All Tracks                | Selects all the tracks, busses and control masters in  |
|                                  | the session                                            |
+----------------------------------+--------------------------------------------------------+
| Select All Visible Lanes         | Selects all the visible tracks, busses and control     |
|                                  | masters, i.e. those marked [v]{.kbd .check} in the     |
|                                  | [Editor List](@@editor-lists)                          |
+----------------------------------+--------------------------------------------------------+
| Deselect All                     | Deselects all objects or tracks, nothing is selected   |
+----------------------------------+--------------------------------------------------------+
| Invert Note Selection            | Select the previously unselected regions, and deselect |
|                                  | the previously selected ones                           |
+----------------------------------+--------------------------------------------------------+
| Set Range to Loop Range          | Creates a range selection on the selected tracks,      |
|                                  | based on the selected loop markers, and switches to    |
|                                  | [Range Mode tool](@@toolbox)                           |
+----------------------------------+--------------------------------------------------------+
| Set Range to Punch Range         | Same as above, based on the selected punch markers     |
+----------------------------------+--------------------------------------------------------+
| Set Range to Selected Regions    | Same as above, based on the selected regions (i.e.     |
|                                  | from the start of the earliest region to the end of    |
|                                  | the latest one)                                        |
+----------------------------------+--------------------------------------------------------+
| Select All After Edit Point      | Select all the regions and automation points that      |
|                                  | exist after the Edit Point, even if the region starts  |
|                                  | before it. If some tracks are selected, only selects   |
|                                  | on these tracks.                                       |
+----------------------------------+--------------------------------------------------------+
| Select All Before Edit Point     | Same as above, but before the Edit point (i.e. to the  |
|                                  | left of it)                                            |
+----------------------------------+--------------------------------------------------------+
| Select All Overlapping Edit      | Select all the regions and automation points of which  |
| Range                            | at least a part is in the current selection range      |
+----------------------------------+--------------------------------------------------------+
| Select All Inside Edit Range     | Selects all the regions that are completely inside the |
|                                  | selection range, i.e. their start and end are inside   |
|                                  | the range. If some tracks are selected, only selects   |
|                                  | on these tracks.                                       |
+----------------------------------+--------------------------------------------------------+
| Select All in Punch Range        | Selects all the regions of which a part in in the      |
|                                  | punch range. If some tracks are selected, only selects |
|                                  | on these tracks.                                       |
+----------------------------------+--------------------------------------------------------+
| Select All in Loop Range         | Same as above, based on the loop range                 |
+----------------------------------+--------------------------------------------------------+
| Move Range Start to Previous     | Extends the left boundary of the range to the left to  |
| Region Boundary                  | the next region start or end. The region must be in    |
|                                  | the range.                                             |
+----------------------------------+--------------------------------------------------------+
| Move Range Start to Next Region  | Same as above, to the right (reduces the selection)    |
| Boundary                         |                                                        |
+----------------------------------+--------------------------------------------------------+
| Move Range End to Previous       | Same as above, with the right edge of the range, to    |
| Region Boundary                  | the left (reduces the selection)                       |
+----------------------------------+--------------------------------------------------------+
| Move Range End to Next Region    | Same as above, with the right edge, to the right       |
| Boundary                         | (extends the selection)                                |
+----------------------------------+--------------------------------------------------------+
| Start Range                      | Sets the left edge of the range to the Edit point      |
+----------------------------------+--------------------------------------------------------+
| Finish Range                     | Sets the right edge of the range to the Edit point     |
+----------------------------------+--------------------------------------------------------+
| Select Next Track or Bus         | Select the track or bus under the currently selected   |
|                                  | one. If multiple tracks are selected, only the first   |
|                                  | one is considered                                      |
+----------------------------------+--------------------------------------------------------+
| Select Previous Track or Bus     | Same as above, with the track/bus above the first one  |
|                                  | selected.                                              |
+----------------------------------+--------------------------------------------------------+
| Delete                           | Deletes all that is currently selected                 |
+----------------------------------+--------------------------------------------------------+
| Crop                             | Cuts the parts of the regions that are outside the     |
|                                  | range boundaries. Only applies on the regions that     |
|                                  | belong at least in part to the range.                  |
+----------------------------------+--------------------------------------------------------+
| Split/Separate                   | Cuts the selected regions at the Edit point,           |
|                                  | separating them in two regions                         |
+----------------------------------+--------------------------------------------------------+
| Separate                                                                                  |
+----------------------------------+--------------------------------------------------------+
| Separate Under                   | Removes all the parts of the regions that are under    |
|                                  | the selected one. Once done, the selected region is    |
|                                  | alone on its part of the track.                        |
+----------------------------------+--------------------------------------------------------+
| Separate Using Loop Range        | Cuts the selected regions or the regions on the        |
|                                  | selected tracks along the Loop range\'s start and end  |
|                                  | markers. If nothing is selected, acts on all tracks at |
|                                  | once.                                                  |
+----------------------------------+--------------------------------------------------------+
| Separate Using Punch Range       | Same as above, with the Punch range markers            |
+----------------------------------+--------------------------------------------------------+
| Consolidate                                                                               |
+----------------------------------+--------------------------------------------------------+
| Consolidate Range                | Group all parts of regions in the range and on the     |
|                                  | same track as one (Audio or MIDI but not both).        |
|                                  | Optionally, add it to the Cue Grid and/or to the Clip  |
|                                  | library.                                               |
+----------------------------------+--------------------------------------------------------+
| Consolidate Range (with          | Same as above, with processing (effects, plugins,      |
| processing)                      | gain&hellip) applied before grouping.                  |
+----------------------------------+--------------------------------------------------------+
| Combine                          | Group all the selected regions belonging to the same   |
|                                  | track as one (Audio or MIDI but not both).             |
+----------------------------------+--------------------------------------------------------+
| Uncombine                        | (Audio only) splits back a compound into its original  |
|                                  | regions.                                               |
+----------------------------------+--------------------------------------------------------+
| Align                                                                                     |
+----------------------------------+--------------------------------------------------------+
| Align Start                      | Moves the selected regions to align the beginning of   |
|                                  | the regions to the Edit point                          |
+----------------------------------+--------------------------------------------------------+
| Align Start Relative             | When multiple regions are selected, moves all the      |
|                                  | regions together as a block to align the beginning of  |
|                                  | the earliest one to the Edit point.                    |
+----------------------------------+--------------------------------------------------------+
| Align End                        | Moves the selected regions to align the end of the     |
|                                  | regions to the Edit point                              |
+----------------------------------+--------------------------------------------------------+
| Align End Relative               | When multiple regions are selected, moves all the      |
|                                  | regions together as a block to align the end of the    |
|                                  | latest one to the Edit point.                          |
+----------------------------------+--------------------------------------------------------+
| Align Sync                       | Moves the selected regions to align the Sync point of  |
|                                  | the regions to the Edit point                          |
+----------------------------------+--------------------------------------------------------+
| Align Sync Relative              | When multiple regions are selected, moves all the      |
|                                  | regions together as a block to align the earliest Sync |
|                                  | point to the Edit point.                               |
+----------------------------------+--------------------------------------------------------+
| Fade                                                                                      |
+----------------------------------+--------------------------------------------------------+
| Fade Range Selection             | For all the regions that either begin or end in the    |
|                                  | range, create a fade in or out on the regions length.  |
+----------------------------------+--------------------------------------------------------+
| Set Fade In Length               | If the edit point is within the region boundaries,     |
|                                  | adjusts selected audio regions\' fade in to end at the |
|                                  | edit point.                                            |
+----------------------------------+--------------------------------------------------------+
| □ Fade In                        | Toggles the fade in on the selected region on or off   |
+----------------------------------+--------------------------------------------------------+
| Set Fade Out Length              | Same as above, for the fade out                        |
+----------------------------------+--------------------------------------------------------+
| □ Fade Out                       | Toggles the fade out on the selected region on or off  |
+----------------------------------+--------------------------------------------------------+
| Analyze                                                                                   |
+----------------------------------+--------------------------------------------------------+
| Spectral Analysis                | For the selected range and tracks, shows the Spectral  |
|                                  | analysis, showing a frequency vs dBFS graph.           |
+----------------------------------+--------------------------------------------------------+
| Loudness Analysis                | For the selected range, one tab per track, shows the   |
|                                  | [Audio                                                 |
|                                  | Report/Analysis](@@export-dialog#export_analyze),      |
|                                  | showing in particular a time vs dBFS graph.            |
+----------------------------------+--------------------------------------------------------+
| Loudness Assistant               | For the selected range and tracks, shows the [Loudness |
|                                  | Analyzer and Normalizer](@@loudness-analyzer).         |
+----------------------------------+--------------------------------------------------------+
| Tag Last Capture                 | Prompts for a text to tag the last record, this tag is |
|                                  | visible in the [Region list](@@the-region-list)        |
+----------------------------------+--------------------------------------------------------+
| Remove Last Capture              | Destroy the last recording. A prompt reminds the user  |
|                                  | this *cannot* be undone.                               |
+----------------------------------+--------------------------------------------------------+
| Edit point                                                                                |
+----------------------------------+--------------------------------------------------------+
| Change Edit Point                | Toggles between the mouse and the playhead as the Edit |
|                                  | point                                                  |
+----------------------------------+--------------------------------------------------------+
| Change Edit Point Including      | Toggles between the mouse, the playhead and marker as  |
| Marker                           | the Edit point                                         |
+----------------------------------+--------------------------------------------------------+
| Toggle Snap                      | Activates/deactivates snapping, which aligns region    |
|                                  | boundaries to the closest selected time marker when    |
|                                  | moved                                                  |
+----------------------------------+--------------------------------------------------------+
| Snap & Grid                                                                               |
+----------------------------------+--------------------------------------------------------+
| Previous Quantize Grid Choice    | Changes the snap quantization to the previous one in   |
|                                  | the list below                                         |
+----------------------------------+--------------------------------------------------------+
| Next Quantize Grid Choice        | Changes the snap quantization to the next one in the   |
|                                  | list below                                             |
+----------------------------------+--------------------------------------------------------+
| ○ No Grid                        | Disables [snapping](@@grid-controls), i.e. allows free |
|                                  | movement of regions and boundaries                     |
+----------------------------------+--------------------------------------------------------+
| ○ Bar                            | Snaps to the closest musical bar, bars can be set and  |
|                                  | seen in the [Ruler](@@ruler)                           |
+----------------------------------+--------------------------------------------------------+
| ○ 1/4 Note → 1/28 (32nd          | Selects the division of musical time to snap to        |
| septuplet)                       |                                                        |
+----------------------------------+--------------------------------------------------------+
| ○ Timecode                       | Snaps to the closest frame, a timecode being           |
|                                  | Hrs:Min:Sec:Frame. The number of frames per second is  |
|                                  | defined in the [Session                                |
|                                  | Properties](@@session-properties#properties-timecode). |
+----------------------------------+--------------------------------------------------------+
| ○ MinSec                         | Snaps to the closest second in the timeline.           |
+----------------------------------+--------------------------------------------------------+
| ○ CD Frames                      | Snaps to the closest CD Frame, one CD frame being      |
|                                  | 1/75^th^ of a second.                                  |
+----------------------------------+--------------------------------------------------------+
| Tempo                                                                                     |
+----------------------------------+--------------------------------------------------------+
| Set Tempo from Region = Bar      | Computes the tempo so that the duration of the first   |
|                                  | selected region is 1 bar. Ardour prompts if the user   |
|                                  | wants it to be the global tempo, or a tempo marker at  |
|                                  | the beginning of the region used                       |
+----------------------------------+--------------------------------------------------------+
| Set Tempo from Edit Range = Bar  | Same thing, with the current Range instead of a region |
+----------------------------------+--------------------------------------------------------+
| □ Smart Mode                     | Toggles the Smart Mode, allowing the mouse to be in    |
|                                  | Range Mode in the upper half of a region, and in Grab  |
|                                  | Mode in the lower half                                 |
+----------------------------------+--------------------------------------------------------+
| □ Show Automation Lane on Touch  | When toggled on, clicking on a plugin parameter,       |
|                                  | hardware controller, etc... makes Ardour show the      |
|                                  | relevant [automation](@@automation) lane               |
+----------------------------------+--------------------------------------------------------+
| Lua Scripts                                                                               |
+----------------------------------+--------------------------------------------------------+
| □ Script Manager                 | Shows the [Script manager](@@lua-scripting), allowing  |
|                                  | to use and manage the Lua scripts in the session       |
+----------------------------------+--------------------------------------------------------+
| *Action script #n*               | Executes the *n*th script. The script list is defined  |
|                                  | in the Script Manager.                                 |
+----------------------------------+--------------------------------------------------------+
| Preferences                      | Displays the [Preferences](@@preferences) panels,      |
|                                  | allowing to change Ardour\'s behaviour                 |
+----------------------------------+--------------------------------------------------------+
```
