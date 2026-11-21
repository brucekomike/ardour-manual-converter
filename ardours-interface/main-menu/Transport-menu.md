# The Transport Menu
The [Transport]{.dfn} menu handles how Ardour handles the playback and
playhead.

```{eval-rst}
+----------------------------------+-----------------------------------------------------+
| Start/Stop                       | Starts or stops the playhead, and recording if it   |
|                                  | is armed                                            |
+----------------------------------+-----------------------------------------------------+
| Play                                                                                   |
+----------------------------------+-----------------------------------------------------+
| Play Selection                   | Only plays the selected duration of the session,    |
|                                  | based on the current range or selected region(s)    |
+----------------------------------+-----------------------------------------------------+
| Solo Selection                   | Only plays the selected regions of the session.     |
|                                  | Regions that are not selected, even on a track with |
|                                  | selected regions, wont be played                    |
+----------------------------------+-----------------------------------------------------+
| Play w/Preroll                   | As the previous menu, except it starts the playback |
|                                  | a few bars or seconds before the beginning of the   |
|                                  | selection (the amount of time can be set in the     |
|                                  | [Preferences](@@preferences#preferences-transport)) |
+----------------------------------+-----------------------------------------------------+
| Start/Continue/Stop              | Leaves loop play or range play mode but without     |
|                                  | stopping the transport                              |
+----------------------------------+-----------------------------------------------------+
| Play from Edit Point and Return  | Starts the playback at the [Edit                    |
|                                  | point](@@edit-point-control), and when stopped,     |
|                                  | goes back to the original location                  |
+----------------------------------+-----------------------------------------------------+
| Play Loop Range                  | If a [Loop range](@@the-loop-range) is defined,     |
|                                  | play it and loop until stopped                      |
+----------------------------------+-----------------------------------------------------+
| Start Recording                  | This is a shortcut to trigger the global recording, |
|                                  | and start playback at once                          |
+----------------------------------+-----------------------------------------------------+
| Stop and Forget Capture          | Stops the recording, removes the newly created      |
|                                  | material, and goes back to the original position    |
+----------------------------------+-----------------------------------------------------+
| Enable Record                    | Triggers the global recording. Next time \"Play\"   |
|                                  | is pressed, it will record on the track(s) that are |
|                                  | armed for recording                                 |
+----------------------------------+-----------------------------------------------------+
| Record w/Preroll                 | As the Start Recording menu, except it starts the   |
|                                  | recording a few bars or seconds before the          |
|                                  | playhead\'s position (the amount of time can be set |
|                                  | in the                                              |
|                                  | [Preferences](@@preferences#preferences-transport)) |
+----------------------------------+-----------------------------------------------------+
| Record w/Count-In                | As the Start Recording menu, except it waits for 2  |
|                                  | bars before the playhead\'s position. The Metronome |
|                                  | will tick (even if disabled) during the count-in    |
+----------------------------------+-----------------------------------------------------+
| Forward                          | Plays the audio forwards from the playhead on. If   |
|                                  | the audio is already playing forwards, increment    |
|                                  | its speed by 50%.                                   |
+----------------------------------+-----------------------------------------------------+
| Rewind                           | Plays the audio backwards from the playhead on. If  |
|                                  | the audio is already playing backwards, increment   |
|                                  | its speed by 50%.                                   |
+----------------------------------+-----------------------------------------------------+
| Transition to Roll               | Plays the audio forwards, with a speed of 1 (real   |
|                                  | time)                                               |
+----------------------------------+-----------------------------------------------------+
| Transition to Reverse            | Plays the audio backwards, with a speed of 1 (real  |
|                                  | time)                                               |
+----------------------------------+-----------------------------------------------------+
| Set Loop from Selection          | Converts the selection into a [Loop                 |
|                                  | range](@@the-loop-range) by placing loop markers at |
|                                  | the start and end of the selected range             |
+----------------------------------+-----------------------------------------------------+
| Set Punch from Selection         | Same thing, for [Punch](@@punch-range)              |
+----------------------------------+-----------------------------------------------------+
| Set Session Start/End from       | Same thing, for the start and end markers of the    |
| Selection                        | session, defining the session\'s length             |
+----------------------------------+-----------------------------------------------------+
| Playhead                                                                               |
+----------------------------------+-----------------------------------------------------+
| Playhead to Mouse                | Set the position of the playhead at the current     |
|                                  | position of the mouse cursor                        |
+----------------------------------+-----------------------------------------------------+
| Playhead to Active Mark          | If a marker is selected, set the position of the    |
|                                  | playhead at the position of the marker              |
+----------------------------------+-----------------------------------------------------+
| Center Playhead                  | Centers the view on the playhead without changing   |
|                                  | the zoom level (putting the playhead in the middle  |
|                                  | of the screen)                                      |
+----------------------------------+-----------------------------------------------------+
| Nudge Playhead Forward           | Shifts the position of the playhead to the right by |
|                                  | the amount shown in the [nudge                      |
|                                  | timer](@@nudge-controls)                            |
+----------------------------------+-----------------------------------------------------+
| Nudge Playhead Backward          | Same thing, to the left                             |
+----------------------------------+-----------------------------------------------------+
| Move to Next Transient           | When transient have been set, moves the playhead to |
|                                  | the next one to the right                           |
+----------------------------------+-----------------------------------------------------+
| Move to Previous Transient       | Same, to the left                                   |
+----------------------------------+-----------------------------------------------------+
| Playhead to Next Grid            | Regardless of the state of the Grid Mode, goes to   |
|                                  | the next grid to the right, as set by the           |
|                                  | [Snap/Grid unit](@@grid-controls)                   |
+----------------------------------+-----------------------------------------------------+
| Playhead to Previous Grid        | Same, to the left                                   |
+----------------------------------+-----------------------------------------------------+
| Playhead to Next Region Boundary | Moves the playhead to the right to the next         |
|                                  | beginning or end of region on the selected track    |
|                                  | or, if no track is selected, on all tracks          |
+----------------------------------+-----------------------------------------------------+
| Playhead to Previous Region      | Same, to the left                                   |
| Boundary                         |                                                     |
+----------------------------------+-----------------------------------------------------+
| Playhead to Next Region Boundary | Moves the playhead to next beginning or end of      |
| (No Track Selection)             | region, be it on the selected track or any other    |
+----------------------------------+-----------------------------------------------------+
| Playhead to Previous Region      | Same, to the left                                   |
| Boundary (No Track Selection)    |                                                     |
+----------------------------------+-----------------------------------------------------+
| Playhead to Next Region Sync     | Moves the playhead to next Region Sync Point, that  |
|                                  | is by default the beginning of a region but [can be |
|                                  | moved](@@grid-controls)                             |
+----------------------------------+-----------------------------------------------------+
| Playhead to Previous Region Sync | Same, to the left                                   |
+----------------------------------+-----------------------------------------------------+
| Jump to Next Mark                | moves the playhead to the next                      |
|                                  | [marker](@@creating-location-markers) on the Ruler  |
+----------------------------------+-----------------------------------------------------+
| Jump to Previous Mark            | Same, to the left                                   |
+----------------------------------+-----------------------------------------------------+
| Jump to Loop Start               | moves the playhead to the [loop](@@the-loop-range)  |
|                                  | start marker if a loop exists                       |
+----------------------------------+-----------------------------------------------------+
| Jump to Loop End                 | Same, for the loop end marker                       |
+----------------------------------+-----------------------------------------------------+
| Go to Zero                       | Sends the playhead to the 00:00:00:00 time,         |
|                                  | regardless of the sessions Start marker             |
+----------------------------------+-----------------------------------------------------+
| Go to Start                      | Sends the playhead to the Start marker of the       |
|                                  | session                                             |
+----------------------------------+-----------------------------------------------------+
| Go to End                        | Sends the playhead to the End marker of the session |
+----------------------------------+-----------------------------------------------------+
| Go to Wall Clock                 | Sends the playhead to the current value of system   |
|                                  | time, as shown on the top right of the [Status      |
|                                  | bar](@@status-bar)                                  |
+----------------------------------+-----------------------------------------------------+
| Active Mark                                                                            |
+----------------------------------+-----------------------------------------------------+
| To Next Region Boundary          | Moves the currently selected                        |
|                                  | [marker](@@working-with-markers) to the next region |
|                                  | beginning or end                                    |
+----------------------------------+-----------------------------------------------------+
| To Previous Region Boundary      | Same, to the left                                   |
+----------------------------------+-----------------------------------------------------+
| To Next Region Sync              | Moves the currently selected to the next region     |
|                                  | sync point (by default: beginning or end of the     |
|                                  | region)                                             |
+----------------------------------+-----------------------------------------------------+
| To Previous Region Sync          | Same, to the left                                   |
+----------------------------------+-----------------------------------------------------+
| Markers                                                                                |
+----------------------------------+-----------------------------------------------------+
| Add Mark from Playhead           | Creates a Marker at the position of the playhead    |
+----------------------------------+-----------------------------------------------------+
| Remove Mark at Playhead          | Removes any marker at the position of the playhead  |
+----------------------------------+-----------------------------------------------------+
| Toggle Mark at Playhead          | Combine the 2 previous: if a marker exists, deletes |
|                                  | it, otherwise create it                             |
+----------------------------------+-----------------------------------------------------+
| Locate to Mark *n*               | If it exists, goes to the *n-th* marker             |
+----------------------------------+-----------------------------------------------------+
| Set Session Start from Playhead  | Puts the Start of the session marker at the         |
|                                  | playhead\'s position                                |
+----------------------------------+-----------------------------------------------------+
| Set Session End from Playhead    | Puts the End of the session marker at the           |
|                                  | playhead\'s position                                |
+----------------------------------+-----------------------------------------------------+
| Cues                                                                                   |
+----------------------------------+-----------------------------------------------------+
| Trigger Cue *A → H*              | Starts the playback and triggers the *A → H* line   |
|                                  | of the [Cue                                         |
|                                  | grid](@@cue-window-elements#cue_window_grid)        |
+----------------------------------+-----------------------------------------------------+
| □ Time Master                    | Sets Ardour as the Time master, i.e. Ardour sends   |
|                                  | the time information to the audio system            |
+----------------------------------+-----------------------------------------------------+
| □ Punch In/Out                   | Based on the Punch in and Punch out markers if they |
|                                  | exist, tells Ardour to record only between those    |
|                                  | two points                                          |
+----------------------------------+-----------------------------------------------------+
| □ Punch In                       | Based on the Punch in marker, only allow to record  |
|                                  | from this point on                                  |
+----------------------------------+-----------------------------------------------------+
| □ Punch Out                      | Based on the Punch out marker, forbids recording    |
|                                  | before this point                                   |
+----------------------------------+-----------------------------------------------------+
| □ Auto Input                     | If checked, automatically switch the                |
|                                  | [monitor](@@monitor-setup-in-ardour) from *input*   |
|                                  | to *playback*mode when playing                      |
+----------------------------------+-----------------------------------------------------+
| □ Follow Range                   | If checked, selecting a range moves the playhead to |
|                                  | its beginning                                       |
+----------------------------------+-----------------------------------------------------+
| □ Auto Play                      | If checked, moving the playhead in the ruler starts |
|                                  | the playback                                        |
+----------------------------------+-----------------------------------------------------+
| □ Auto Return                    | If checked, when the playback is stopped, go back   |
|                                  | to the previous position of the playhead. If not,   |
|                                  | the playhead stays where it is when the playback is |
|                                  | stopped                                             |
+----------------------------------+-----------------------------------------------------+
| □ Click                          | Activates/deactivates the click track (metronome)   |
+----------------------------------+-----------------------------------------------------+
| □ Follow Playhead                | If checked, while playing, when the playhead        |
|                                  | reaches the right of the screen, Ardour scrolls one |
|                                  | screen to the right to keep the playhead visible at |
|                                  | all times                                           |
+----------------------------------+-----------------------------------------------------+
| □ Stationary Playhead            | If checked *and* if [Follow playhead]{.kbd .menu}   |
|                                  | is checked, on playback, the playhead stays at the  |
|                                  | center of the screen, and the session scrolls       |
+----------------------------------+-----------------------------------------------------+
| □ Use External Positional Sync   | If checked, allows Ardour to be controlled by       |
| Source                           | external program                                    |
+----------------------------------+-----------------------------------------------------+
| Panic (Send MIDI all-notes-off)  | Immediately stops all MIDI playback (useful e.g.    |
|                                  | when a MIDI bug in encountered)                     |
+----------------------------------+-----------------------------------------------------+
```
