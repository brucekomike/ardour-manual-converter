# The View Menu
The [View]{.dfn} menu sets how the session is seen, and what\'s visible
or not.

```{eval-rst}
+--------------------------------+------------------------------------------------------+
| □ Maximise Editor Space        | Puts the Editor window in full screen mode           |
+--------------------------------+------------------------------------------------------+
| □ Maximize Mixer Space         | Puts the Mixer window in full screen mode            |
+--------------------------------+------------------------------------------------------+
| Region Layers                                                                         |
+--------------------------------+------------------------------------------------------+
| Stacked Layer Display          | When multiple takes are available, this will display |
|                                | them on top of one another                           |
+--------------------------------+------------------------------------------------------+
| Overlaid Layer Display         | When multiple takes are available, the most recent   |
|                                | one will be displayed on top of older ones           |
+--------------------------------+------------------------------------------------------+
| Automation                                                                            |
+--------------------------------+------------------------------------------------------+
| Toggle All Existing Automation | Show or hides all the [automation                    |
|                                | lanes](@@automation) that have been edited by the    |
|                                | user                                                 |
+--------------------------------+------------------------------------------------------+
| Primary Clock                                                                         |
+--------------------------------+------------------------------------------------------+
| Focus On Clock                 | Sets the focus on the [main                          |
|                                | clock](@@transport-clocks), allowing to type in      |
|                                | numbers directly to change the playhead position     |
+--------------------------------+------------------------------------------------------+
| Timecode                       | Sets the main clock in timecode mode, so it displays |
|                                | time in the Hours:Minutes:Seconds:Frames format      |
+--------------------------------+------------------------------------------------------+
| Bars & Beats                   | Sets the main clock in musical time mode, so it      |
|                                | displays time in the Bars:Beats:Ticks format         |
+--------------------------------+------------------------------------------------------+
| Minutes & Seconds              | Sets the main clock in absolute time mode, so it     |
|                                | displays time in the                                 |
|                                | Hours:Minutes:Seconds.Milliseconds format            |
+--------------------------------+------------------------------------------------------+
| Samples                        | Sets the main clock in samples time mode, so the     |
|                                | time is displayed in samples from the absolute start |
+--------------------------------+------------------------------------------------------+
| Secondary Clock                                                                       |
+--------------------------------+------------------------------------------------------+
| Timecode                       | Same as for the main clock (see above)               |
+--------------------------------+------------------------------------------------------+
| Bars & Beats                   | Same as for the main clock                           |
+--------------------------------+------------------------------------------------------+
| Minutes & Seconds              | Same as for the main clock                           |
+--------------------------------+------------------------------------------------------+
| Samples                        | Same as for the main clock                           |
+--------------------------------+------------------------------------------------------+
| Rulers                                                                                |
+--------------------------------+------------------------------------------------------+
| □ Min:Sec                      | Shows (when checked) or hides a line in [the         |
|                                | Ruler](@@ruler) with the time formatted as           |
|                                | Hours:Minutes:Seconds.Milliseconds                   |
+--------------------------------+------------------------------------------------------+
| □ Timecode                     | Same as above, with the time formatted as            |
|                                | Hours:Minutes:Seconds:Frames                         |
+--------------------------------+------------------------------------------------------+
| □ Samples                      | Same as the above, with the time displayed in        |
|                                | samples from the absolute start                      |
+--------------------------------+------------------------------------------------------+
| □ Bars & Beats                 | Same as the above, with the time formatted as        |
|                                | Bars:Beats:Ticks                                     |
+--------------------------------+------------------------------------------------------+
| □ Time Signature               | Shows / hides the time signature line in the ruler,  |
|                                | where the signature can be adjusted along the        |
|                                | playline                                             |
+--------------------------------+------------------------------------------------------+
| □ Tempo                        | Shows / hides the Tempo line, where the BPM can be   |
|                                | changed with markers                                 |
+--------------------------------+------------------------------------------------------+
| □ Range Markers                | Shows / hides the Range line, where ranges can be    |
|                                | defined                                              |
+--------------------------------+------------------------------------------------------+
| □ Loop/Punch Ranges            | Shows / hides the Loop/Punch line, where loops and   |
|                                | Punches can be defined                               |
+--------------------------------+------------------------------------------------------+
| □ CD Markers                   | Shows / hides the Range line, where CD Markers can   |
|                                | be defined                                           |
+--------------------------------+------------------------------------------------------+
| □ Location Markers             | Shows / hides the Markers line, where custom markers |
|                                | can be defined                                       |
+--------------------------------+------------------------------------------------------+
| □ Cue markers                  | Shows / hides the Cue line, where Cue markers can be |
|                                | set to trigger entire cues                           |
+--------------------------------+------------------------------------------------------+
| □ Video Timeline               | Shows / hides the Video timeline, where frames of    |
|                                | the video are shown for syncing purposes             |
+--------------------------------+------------------------------------------------------+
| Zoom                                                                                  |
+--------------------------------+------------------------------------------------------+
| Zoom In                        | Zooms in, focusing the *Zoom Focus* (see below)      |
+--------------------------------+------------------------------------------------------+
| Zoom Out                       | Zooms out                                            |
+--------------------------------+------------------------------------------------------+
| Zoom to Session                | Adjust the zoom value so that all the session (as    |
|                                | defined by its start and end markers) fit in the     |
|                                | window                                               |
+--------------------------------+------------------------------------------------------+
| Zoom to Extents                | Adjust the zoom value so that all objects (markers,  |
|                                | regions, etc...) fit in the window                   |
+--------------------------------+------------------------------------------------------+
| Zoom to Selection              | Adjust the zoom value so that all the selected       |
|                                | regions fit in the window                            |
+--------------------------------+------------------------------------------------------+
| Zoom to Selection (Horizontal) | Adjust the horizontal zoom value so that all the     |
|                                | selected regions fit in the window, without changing |
|                                | the vertical zoom                                    |
+--------------------------------+------------------------------------------------------+
| Fit Selection (Vertical)       | Fits the selected track(s) in the window. If too     |
|                                | many tracks are selected, they\'ll be reduced to     |
|                                | their minimum height.                                |
+--------------------------------+------------------------------------------------------+
| Toggle Zoom State              | Reverts to last zoom state (kind of \"undo\" for     |
|                                | zoom, even if edits have been made in-between)       |
+--------------------------------+------------------------------------------------------+
| Expand Track Height            | Increases the height of the selected tracks. If no   |
|                                | track is selected, then all the tracks are expanded  |
+--------------------------------+------------------------------------------------------+
| Shrink Track Height            | Same as above, but reduces the height of the tracks  |
+--------------------------------+------------------------------------------------------+
| Zoom Focus                                                                            |
+--------------------------------+------------------------------------------------------+
| ○ Zoom Focus Left              | Sets the screen\'s left side as the zoom target,     |
|                                | i.e. when zooming in, the left side of the screen    |
|                                | will stay at the same place in the timeline          |
+--------------------------------+------------------------------------------------------+
| ○ Zoom Focus Right             | Same, with the right of the screen                   |
+--------------------------------+------------------------------------------------------+
| ○ Zoom Focus Center            | Same, with the center of the screen                  |
+--------------------------------+------------------------------------------------------+
| ○ Zoom Focus Playhead          | Sets the playhead as the focus point of the zoom,    |
|                                | i.e. the point in time that will stay fixed          |
+--------------------------------+------------------------------------------------------+
| ○ Zoom Focus Mouse             | Same as above, with the mouse pointer                |
+--------------------------------+------------------------------------------------------+
| ○ Zoom Focus Edit Point        | Same as above, with the Edit Point                   |
+--------------------------------+------------------------------------------------------+
| Next Zoom Focus                | Circles between the previous modes                   |
+--------------------------------+------------------------------------------------------+
| Scroll                                                                                |
+--------------------------------+------------------------------------------------------+
| Scroll Tracks Down             | Scrolls the view toward the bottom of the session    |
|                                | from one screen (vertically, so along tracks)        |
+--------------------------------+------------------------------------------------------+
| Scroll Tracks Up               | Same as above, towards the top                       |
+--------------------------------+------------------------------------------------------+
| Scroll Forward                 | Scrolls the view toward the right of the session     |
|                                | from one screen (horizontally, so along time)        |
+--------------------------------+------------------------------------------------------+
| Scroll Backward                | Same as above, to the left                           |
+--------------------------------+------------------------------------------------------+
| Video Monitor                                                                         |
+--------------------------------+------------------------------------------------------+
| Original Size                  | When the [Video                                      |
|                                | Monitor](@@video-timeline-and-monitoring) is active, |
|                                | resets its size to the original size, i.e. 1 pixel   |
|                                | in the video is 1 pixel on screen                    |
+--------------------------------+------------------------------------------------------+
| □ Letterbox                    | When checked, forces the ratio (width/height) to be  |
|                                | the one of the original video. If unchecked, the     |
|                                | video will be stretched to fit the window            |
+--------------------------------+------------------------------------------------------+
| □ Always on Top                | Stays above all other windows, enabling to work in   |
|                                | Ardour without the video windows to be hidden in the |
|                                | background                                           |
+--------------------------------+------------------------------------------------------+
| □ Fullscreen                   | Sets the Xjadeo window to be fullscreen. Can be      |
|                                | useful in a dual monitor setup                       |
+--------------------------------+------------------------------------------------------+
| □ Timecode                     | When checked, displays a Timecode over the video, in |
|                                | the Hours:Minutes:Seconds:Frames format              |
+--------------------------------+------------------------------------------------------+
| □ Frame number                 | When checked, shows the absolute frame number inside |
|                                | the video, i.e. this image is the *n*th of the video |
+--------------------------------+------------------------------------------------------+
| □ Timecode Background          | Adds a black background to the timecode for          |
|                                | readability                                          |
+--------------------------------+------------------------------------------------------+
| Editor Views                                                                          |
+--------------------------------+------------------------------------------------------+
| Save View *n*                  | Saves the position on the timeline in the memory,    |
|                                | horizontally and vertically (along time and tracks)  |
+--------------------------------+------------------------------------------------------+
| Go to View *n*                 | Loads and displays a saved position (see above)      |
+--------------------------------+------------------------------------------------------+
| □ Show Editor Mixer            | When checked, the selected tracks\' mixer strip is   |
|                                | displayed on the left of the editor window, allowing |
|                                | for a quick access to e.g. effects and routing       |
+--------------------------------+------------------------------------------------------+
| □ Show Editor List             | In the Editor window, shows the [Editor              |
|                                | List](@@editor-lists), giving access to a number of  |
|                                | handy lists (regions, tracks, ...)                   |
+--------------------------------+------------------------------------------------------+
| □ Show Summary                 | If checked, in the Editor, shows the                 |
|                                | [Summary](@@summary), allowing a faster navigation   |
|                                | in the session                                       |
+--------------------------------+------------------------------------------------------+
| □ Show Group Tabs              | If checked, makes the groups visible as tabs on the  |
|                                | left in the Editor, and on the top in the mixer      |
+--------------------------------+------------------------------------------------------+
| □ Show Marker Lines            | If checked, each marker is extended across all the   |
|                                | tracks in the editor with a line of the same color   |
+--------------------------------+------------------------------------------------------+
| □ Mixer: Show Mixer List       | In the Mixer view, shows the Mixer list, giving      |
|                                | access to some handy lists ([Favorite                |
|                                | plugins](@@favorite-plugins-window), [The Strip      |
|                                | list](@@strips-list),...)                            |
+--------------------------------+------------------------------------------------------+
| □ Mixer: Show VCAs             | In the Mixer view, shows the VCA Strips if there are |
|                                | any                                                  |
+--------------------------------+------------------------------------------------------+
| □ Mixer: Show Monitor Section  | If the [Use monitoring section on this session]{.kbd |
|                                | .option} has been checked in the [Session Properties |
|                                | window](@@session-properties#properties-monitoring), |
|                                | shows or hides the Monitor Section in the Mixer      |
+--------------------------------+------------------------------------------------------+
| □ Mixer: Show Foldback Strip   | In the Mixer view, shows the Foldback Strip if there |
|                                | are any                                              |
+--------------------------------+------------------------------------------------------+
```
