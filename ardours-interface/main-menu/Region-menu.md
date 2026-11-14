# The Region Menu
The [Region]{.kbd .menu} Menu is where the user can tweak its regions,
the parts of audio or MIDI that sit on the timeline.

```{eval-rst}
+----------------------------------+---------------------------------------------------------+
| Insert Region from Source List   | If a region is selected in the Editor List, add it at   |
|                                  | the Edit point                                          |
+----------------------------------+---------------------------------------------------------+
| Play Selected Regions            | Starts playback at the beginning of the selected        |
|                                  | region(s), and stops at its(their) end                  |
+----------------------------------+---------------------------------------------------------+
| Tag Selected Regions             | Prompts for a text to tag all the selected regions,     |
|                                  | this tag is visible in the [Region                      |
|                                  | list](@@the-region-list)                                |
+----------------------------------+---------------------------------------------------------+
| Loop                             | Creates a loop range on the selected region\'s          |
|                                  | boundaries, and starts the looped playback              |
+----------------------------------+---------------------------------------------------------+
| Rename...                        | Changes the name of the region, that appears in its top |
|                                  | left area                                               |
+----------------------------------+---------------------------------------------------------+
| Properties...                    | Shows the [Region properties]{.kbd .menu} window, that  |
|                                  | displays detailed information about the region and      |
|                                  | allow for some modifications                            |
+----------------------------------+---------------------------------------------------------+
| Loudness Analysis...             | Shows the [Audio Report/Analysis]{.kbd .menu} window,   |
|                                  | that displays detailed [dBFS                            |
|                                  | information](@@metering-in-ardour) as well as a         |
|                                  | spectrogram (dBFS of frequency against time)            |
+----------------------------------+---------------------------------------------------------+
| Spectral Analysis...             | Shows the [Audio Report/Analysis]{.kbd .menu} window,   |
|                                  | that displays a integrated spectral view of the region  |
|                                  | (dBFS against frequency)                                |
+----------------------------------+---------------------------------------------------------+
| Edit                                                                                       |
+----------------------------------+---------------------------------------------------------+
| Combine                          | Creates a new region by joining the selected audio      |
|                                  | regions in the same track, and replaces those region    |
|                                  | with the newly created compound. The same rules are     |
|                                  | applied to create the compound as for playback          |
|                                  | regarding e.g. layering                                 |
+----------------------------------+---------------------------------------------------------+
| Uncombine                        | Splits back the compound created by *combining* into    |
|                                  | its original audio regions                              |
+----------------------------------+---------------------------------------------------------+
| Pitch Shift...                   | Changes the tune of the audio region, by octave,        |
|                                  | semitones or percentage, based on spectral analysis.    |
|                                  | Optionally, and if they have been set for the region,   |
|                                  | preserves the formants                                  |
+----------------------------------+---------------------------------------------------------+
| Split at Percussion Onset        | Allows splitting the selected regions on its Percussion |
|                                  | Onsets marker as set by the Rhythm Ferret (Not usable   |
|                                  | as of 5.5)                                              |
+----------------------------------+---------------------------------------------------------+
| Make Mono Regions                | Creates mono regions out of a stereo or multichannel    |
|                                  | region by splitting it into its discrete channels. The  |
|                                  | created regions are added to the Editor List            |
+----------------------------------+---------------------------------------------------------+
| Close Gaps                       | Extends (or reduces) the selected regions to be         |
|                                  | perfectly aligned. Optionally, sets up a crossfade      |
|                                  | duration, or a pull-back (spacing between regions)      |
+----------------------------------+---------------------------------------------------------+
| Place Transient                  | Places a transient at the Edit Point. Used e.g. for the |
|                                  | [Pitch Shift...]{.kbd .menu} action                     |
+----------------------------------+---------------------------------------------------------+
| Rhythm Ferret...                 | Opens the [Rhythm Ferret]{.kbd .menu} which is a        |
|                                  | powerful tool to sequence audio files                   |
+----------------------------------+---------------------------------------------------------+
| Strip Silence...                 | Opens the [Strip Silence]{.kbd .menu} window which is a |
|                                  | very handy tool to remove all audio under a user-chosen |
|                                  | threshold (with a preview)                              |
+----------------------------------+---------------------------------------------------------+
| Reverse                          | Mirrors the audio horizontally                          |
+----------------------------------+---------------------------------------------------------+
| Layering                                                                                   |
+----------------------------------+---------------------------------------------------------+
| Raise to Top                     | On overlapping regions, puts the selected one(s) on top |
+----------------------------------+---------------------------------------------------------+
| Raise                            | On overlapping region, makes the selected one(s) one    |
|                                  | layer higher                                            |
+----------------------------------+---------------------------------------------------------+
| Lower                            | Makes the selected region(s) one layer lower            |
+----------------------------------+---------------------------------------------------------+
| Lower to Bottom                  | Sends the selected region to the background             |
+----------------------------------+---------------------------------------------------------+
| MIDI                                                                                       |
+----------------------------------+---------------------------------------------------------+
| Transpose...                     | On a MIDI region, shows the [[Transpose MIDI]{.kbd      |
|                                  | .menu} window](@@transposing-midi), allowing to shift   |
|                                  | the pitch of the whole MIDI region by ± *n* semitones   |
|                                  | or octaves                                              |
+----------------------------------+---------------------------------------------------------+
| Insert Patch Change...           | Inserts a patch change at the Edit Point, allowing a    |
|                                  | change of patch, channel, program and/or bank           |
+----------------------------------+---------------------------------------------------------+
| Quantize...                      | Shows the [[Quantize]{.kbd .menu}                       |
|                                  | window](@@quantize-midi), allowing to perfectly align   |
|                                  | the MIDI notes to the musical grid                      |
+----------------------------------+---------------------------------------------------------+
| Legatize                         | Shortens or elongates the MIDI notes to make them       |
|                                  | perfectly sequential, i.e. the end of a note is the     |
|                                  | start of the following one                              |
+----------------------------------+---------------------------------------------------------+
| Remove Overlap                   | Shortens or elongates the MIDI notes to make them       |
|                                  | perfectly sequential, i.e. the end of a note is the     |
|                                  | start of the following one                              |
+----------------------------------+---------------------------------------------------------+
| Transform...                     | [[Transform]{.kbd .menu}                                |
|                                  | window](@@transforming-midi---mathematical-operations), |
|                                  | that allows for mathematical operations on the midi     |
|                                  | notes                                                   |
+----------------------------------+---------------------------------------------------------+
| Unlink all selected regions      | Makes the selected MIDI regions independent, e.g.       |
|                                  | editing this region won\'t affect any other one.        |
+----------------------------------+---------------------------------------------------------+
| Unlink from unselected           | Makes the selected MIDI regions independent from        |
|                                  | regions outside the selection, but keep the link        |
|                                  | between the selected ones.                              |
+----------------------------------+---------------------------------------------------------+
| Deinterlace Into Layers          | Splits the selected region(s) to create in-place copies |
|                                  | each containing only one channel. A region containing   |
|                                  | e.g. 3 channels will generate 3 stacked regions         |
|                                  | containing 1 channel each.                              |
+----------------------------------+---------------------------------------------------------+
| List Editor...                   | Shows the [[List Editor]{.kbd                           |
|                                  | .menu}](@@midi-list-editor) which sequentially lists    |
|                                  | all the MIDI events in the region, and allows for       |
|                                  | precise modifications                                   |
+----------------------------------+---------------------------------------------------------+
| Gain                                                                                       |
+----------------------------------+---------------------------------------------------------+
| □ Opaque                         | When checked, makes the region opaque audio-wise, i.e., |
|                                  | the underlying regions won\'t be audible                |
+----------------------------------+---------------------------------------------------------+
| □ Mute                           | When checked, mutes *only* the selected region on the   |
|                                  | track, without muting the track. The muted regions will |
|                                  | have *!!* prepended to their name and will be           |
|                                  | semi-transparent                                        |
+----------------------------------+---------------------------------------------------------+
| Normalize...                     | Shows the [Normalize region]{.kbd .menu} dialog, which  |
|                                  | allows to scale the region level by setting its maximum |
|                                  | level, optionally constraining the RMS                  |
+----------------------------------+---------------------------------------------------------+
| Boost Gain                       | Increases the gain on the selected region by boosting   |
|                                  | the audio, without touching the envelope or automation  |
+----------------------------------+---------------------------------------------------------+
| Cut Gain                         | Reduces the gain without touching the envelope or       |
|                                  | automation                                              |
+----------------------------------+---------------------------------------------------------+
| Reset Gain                       | If the gain has been edited, revert to its initial      |
|                                  | value                                                   |
+----------------------------------+---------------------------------------------------------+
| Reset Envelope                   | If the gain envelope has been edited, resets it to its  |
|                                  | initial value (constant at 0 dB)                        |
+----------------------------------+---------------------------------------------------------+
| □ Invert Polarity                | When checked, inverts the signal\'s phase in the        |
|                                  | selected regions and renders the symbol (a diagonal     |
|                                  | line across zero) next to the names of affected regions |
+----------------------------------+---------------------------------------------------------+
| □ Envelope Active                | When unchecked, disables any envelope editing that has  |
|                                  | been made. The envelope will be displayed in yellow     |
|                                  | instead of green.                                       |
+----------------------------------+---------------------------------------------------------+
| Position                                                                                   |
+----------------------------------+---------------------------------------------------------+
| Move to Original Position        | Moves the region where it was initially recorded or     |
|                                  | inserted in the session                                 |
+----------------------------------+---------------------------------------------------------+
| Snap Position to Grid            | If the Grid Mode is set to *Grid*, snaps the region to  |
|                                  | the nearest grid line                                   |
+----------------------------------+---------------------------------------------------------+
| □ Lock                           | Locks the selected regions at their current positions   |
|                                  | in time and tracks, avoiding any movement on the        |
|                                  | timeline. The region name will be surrounded by *\>*    |
|                                  | and *\<* brackets                                       |
+----------------------------------+---------------------------------------------------------+
| □ Lock to Video                  | Same as above, relative to the position in the video    |
+----------------------------------+---------------------------------------------------------+
| Set Sync Position                | Creates or move the Sync position, i.e. the point of    |
|                                  | the region that will be aligned or snapped to the grid, |
|                                  | and that is (by default) the beginning of the region.   |
+----------------------------------+---------------------------------------------------------+
| Remove Sync                      | Removes any user defined Sync point, and resets the     |
|                                  | sync position to the beginning of the region            |
+----------------------------------+---------------------------------------------------------+
| Nudge Later                      | Moves the region to the right by the amount shown in    |
|                                  | the [nudge timer](@@nudge-controls)                     |
+----------------------------------+---------------------------------------------------------+
| Nudge Earlier                    | Same as above, to the left                              |
+----------------------------------+---------------------------------------------------------+
| Nudge Later by Capture Offset    | Moves the region to the right by the capture latency    |
|                                  | computed by Ardour based on the user\'s settings        |
|                                  | regarding latency                                       |
+----------------------------------+---------------------------------------------------------+
| Nudge Earlier by Capture Offset  | Same as above, to the left                              |
+----------------------------------+---------------------------------------------------------+
| Sequence Regions                 | Puts the selected regions one after the other, so that  |
|                                  | the end of one region is the beginning of the next one, |
|                                  | removing any overlap or silence. The reference point is |
|                                  | the earliest region.                                    |
+----------------------------------+---------------------------------------------------------+
| Markers                                                                                    |
+----------------------------------+---------------------------------------------------------+
| Add Region Cue Marker            | Opens a dialog to enter a region-level marker at the    |
|                                  | mouse pointer position                                  |
+----------------------------------+---------------------------------------------------------+
| Clear Region Cue Markers         | Removes all markers from the selected regions           |
+----------------------------------+---------------------------------------------------------+
| Convert Region Cue Markers to CD | Converts all markers from selected regions to CD        |
| Markers                          | markers, bit doesn\'t delete original region-level      |
|                                  | markers                                                 |
+----------------------------------+---------------------------------------------------------+
| Convert Region Cue Markers to    | Converts all markers from selected regions to location  |
| Location Markers                 | markers, bit doesn\'t delete original region-level      |
|                                  | markers                                                 |
+----------------------------------+---------------------------------------------------------+
| Trim                                                                                       |
+----------------------------------+---------------------------------------------------------+
| Trim Start at Edit Point         | If the Edit Point is within the region boundaries,      |
|                                  | shortens the region to align its start with the Edit    |
|                                  | Point                                                   |
+----------------------------------+---------------------------------------------------------+
| Trim End at Edit Point           | Same as above, for the end of the region                |
+----------------------------------+---------------------------------------------------------+
| Trim to Loop                     | Uses both the start and end Loop markers to shorten the |
|                                  | region                                                  |
+----------------------------------+---------------------------------------------------------+
| Trim to Punch                    | Same as above with the Punch markers                    |
+----------------------------------+---------------------------------------------------------+
| Trim to Previous                 | On overlapping regions, shortens the selected one so    |
|                                  | that the previous region is complete, i.e. the new      |
|                                  | start point for the selected region is the end point of |
|                                  | the previous region on the timeline                     |
+----------------------------------+---------------------------------------------------------+
| Trim to Next                     | Same as above, with the end of the selected region      |
|                                  | aligned to the start of the following one.              |
+----------------------------------+---------------------------------------------------------+
| Ranges                                                                                     |
+----------------------------------+---------------------------------------------------------+
| Set Loop Range                   | Creates a Loop range based on the selected regions,     |
|                                  | i.e. the start of the loop range is the start of the    |
|                                  | earliest region, and the end of the loop is the end of  |
|                                  | the latest region.                                      |
+----------------------------------+---------------------------------------------------------+
| Set Punch                        | Same as above, for the Punch range                      |
+----------------------------------+---------------------------------------------------------+
| Add Single Range Marker          | Same as above, for the Edit range                       |
+----------------------------------+---------------------------------------------------------+
| Add Range Marker Per Region      | For each selected region, creates its own Edit range    |
|                                  | based on the boundaries of each region                  |
+----------------------------------+---------------------------------------------------------+
| Set Range Selection              | Creates a range selection based on the boundaries of    |
|                                  | the selected regions                                    |
+----------------------------------+---------------------------------------------------------+
| Fades                                                                                      |
+----------------------------------+---------------------------------------------------------+
| □ Fade In                        | Activates/deactivates the Fade In at the start of the   |
|                                  | region                                                  |
+----------------------------------+---------------------------------------------------------+
| □ Fade Out                       | Same as above, for the Fade out at the end of the       |
|                                  | region                                                  |
+----------------------------------+---------------------------------------------------------+
| □ Fades                          | Shortcut to activate/deactivate both the fade in and    |
|                                  | fade out                                                |
+----------------------------------+---------------------------------------------------------+
| Duplicate                                                                                  |
+----------------------------------+---------------------------------------------------------+
| Duplicate                        | Creates a copy of the selected region(s) and appends it |
|                                  | to the original                                         |
+----------------------------------+---------------------------------------------------------+
| Multi-Duplicate...               | Shows the [Duplicate]{.kbd .menu} dialog, allowing to   |
|                                  | create multiple copies, or a not-integer number of      |
|                                  | copies (the last one will then be truncated)            |
+----------------------------------+---------------------------------------------------------+
| Fill Track                       | Creates duplicates until it fills the session, i.e.     |
|                                  | reaches the End marker of the session. The last         |
|                                  | duplicate may be truncated to fit in                    |
+----------------------------------+---------------------------------------------------------+
| Export...                        | Shows the [[Export]{.kbd .menu}                         |
|                                  | dialog](@@export-dialog), with all parameters set to    |
|                                  | export only the selected region(s)                      |
+----------------------------------+---------------------------------------------------------+
| Bounce (without processing)      | Creates a bounce, i.e. a version of the region with all |
|                                  | the edits (boundaries, envelope), as a new region in    |
|                                  | the Editor List, without any of the effects of the      |
|                                  | mixer strip                                             |
+----------------------------------+---------------------------------------------------------+
| Bounce (with processing)         | Same as above, *with* the effects of the mixer strip    |
+----------------------------------+---------------------------------------------------------+
| Remove                           | Deletes the region from the edit (no file is harmed in  |
|                                  | the process, and the region stays in the Editor for     |
|                                  | later use)                                              |
+----------------------------------+---------------------------------------------------------+
```
