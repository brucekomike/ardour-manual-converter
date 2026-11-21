# The Session Menu
The [Session]{.kbd .menu} menu groups together everything related to the
session and the file operations.

```{eval-rst}
+----------------------------------+-------------------------------------------------+
| New...                           | Creates a [new](@@newopen-session-dialog)       |
|                                  | session                                         |
+----------------------------------+-------------------------------------------------+
| Open...                          | Opens an existing session                       |
+----------------------------------+-------------------------------------------------+
| Recent...                        | Opens a list of recent sessions that can be     |
|                                  | opened                                          |
+----------------------------------+-------------------------------------------------+
| Close                            | Closes the current session (but not Ardour)     |
+----------------------------------+-------------------------------------------------+
| Save                             | Saves the current session                       |
+----------------------------------+-------------------------------------------------+
| Save As...                       | Saves to a new session (with options)           |
+----------------------------------+-------------------------------------------------+
| Rename...                        | Changes the name of the session                 |
+----------------------------------+-------------------------------------------------+
| Snapshot (& keep working on      | Create a [Snapshot](@@snapshots) but any        |
| current version)...              | subsequent change will be saved to this session |
+----------------------------------+-------------------------------------------------+
| Snapshot (& switch to new        | Same thing, and any subsequent change will be   |
| version)...                      | saved to this new snapshot session              |
+----------------------------------+-------------------------------------------------+
| Save Template...                 | Saves the session as a                          |
|                                  | [template](@@session-templates), without the    |
|                                  | audio                                           |
+----------------------------------+-------------------------------------------------+
| Archive...                       | Exports the session as a [compressed            |
|                                  | file](@@backup-and-sharing-of-sessions) for     |
|                                  | archiving or sharing purposes, optionally       |
|                                  | compressing the audio to FLAC                   |
+----------------------------------+-------------------------------------------------+
| Add Track, Bus or VCA...         | Adds a [new                                     |
|                                  | track/bus/VCA](@@adding-tracks-busses-and-vcas) |
|                                  | to the session, same as the [Track \> Add       |
|                                  | Track, Bus or VCA...]{.kbd .menu}               |
+----------------------------------+-------------------------------------------------+
| Import                           | Opens the                                       |
|                                  | [Import](@@adding-pre-existing-material)        |
|                                  | windows, to add media to the session            |
+----------------------------------+-------------------------------------------------+
| Import PT session                | Import a ProTools© session file. Not everything |
|                                  | in the original session can be imported.        |
+----------------------------------+-------------------------------------------------+
| Open Video...                    | Imports a [video                                |
|                                  | file](@@video-timeline-and-monitoring) in the   |
|                                  | session                                         |
+----------------------------------+-------------------------------------------------+
| Remove Video                     | Removes the video part of the session (the      |
|                                  | video timeline disappears)                      |
+----------------------------------+-------------------------------------------------+
| Loudness Assistant...            | Shows the Loudness Analyzer and Normalizer,     |
|                                  | allowing an in-depth analysis of the master     |
|                                  | bus\' volume for the final export               |
+----------------------------------+-------------------------------------------------+
| Export                                                                             |
+----------------------------------+-------------------------------------------------+
| Quick Audio Export...            | [Export](@@quick-audio-export) a selection or   |
|                                  | the entire session to audio with just a few     |
|                                  | settings                                        |
+----------------------------------+-------------------------------------------------+
| Export to Audio File(s)...       | [Export](@@mixdown) all or part of the session  |
|                                  | in audio form                                   |
+----------------------------------+-------------------------------------------------+
| Stem export...                   | [Exports each track](@@export-dialog) as its    |
|                                  | own audio file (for e.g. DAW interchange)       |
+----------------------------------+-------------------------------------------------+
| Export to Video File             | Exports the session to a [video                 |
|                                  | file](@@workflow-amp-operations)                |
+----------------------------------+-------------------------------------------------+
| □ Properties                     | Shows the [Session                              |
|                                  | Properties](@@session-properties) dialog,       |
|                                  | allowing to fine-tune the parameters of the     |
|                                  | current session                                 |
+----------------------------------+-------------------------------------------------+
| Monitor Section                                                                    |
+----------------------------------+-------------------------------------------------+
| □ Use Monitor Section            | Shortcut for the homonymous session property,   |
|                                  | adds a [Monitor Section](@@monitor-section) to  |
|                                  | the Mixer                                       |
+----------------------------------+-------------------------------------------------+
| □ Mute                           | Shortcut for the global monitor \"Mute\"        |
|                                  | control also available in the mixer\'s Monitor  |
|                                  | Section                                         |
+----------------------------------+-------------------------------------------------+
| □ Dim                            | Shortcut for the global monitor \"Dim\" control |
|                                  | also available in the mixer\'s Monitor Section  |
+----------------------------------+-------------------------------------------------+
| □ Mono                           | Shortcut for the global monitor \"Mono\"        |
|                                  | control also available in the mixer\'s Monitor  |
|                                  | Section                                         |
+----------------------------------+-------------------------------------------------+
| Metadata                                                                           |
+----------------------------------+-------------------------------------------------+
| Edit Metadata...                 | Opens the [Metadata](@@metadata) window, where  |
|                                  | information about the session can be saved      |
+----------------------------------+-------------------------------------------------+
| Import Metadata...               | Creates the metadata by extracting them from    |
|                                  | another session                                 |
+----------------------------------+-------------------------------------------------+
| Clean-Up                                                                           |
+----------------------------------+-------------------------------------------------+
| Bring all media into session     | Copies all the media files imported from        |
| folder                           | outside the session folder in that folder, see  |
|                                  | [Cleaning up Sessions](@@cleaning-up-sessions)  |
+----------------------------------+-------------------------------------------------+
| Rebuild Peak Files               | Reinitializes the buffered images representing  |
|                                  | the audio files                                 |
+----------------------------------+-------------------------------------------------+
| Clean-up Unused Sources...       | Quarantines all the media files not used in the |
|                                  | session to a specific sub-folder of the session |
+----------------------------------+-------------------------------------------------+
| Clean-up Unused Regions...       | Deletes the regions that are not used in the    |
|                                  | session                                         |
+----------------------------------+-------------------------------------------------+
| Flush Wastebasket                | Deletes those quarantined files                 |
+----------------------------------+-------------------------------------------------+
| Lock                             | Locks the session by showing an Unlock window   |
|                                  | that (until clicked) blocks every action on     |
|                                  | Ardour\'s window                                |
+----------------------------------+-------------------------------------------------+
| Quit                             | Exits Ardour. Prompts for saving the session if |
|                                  | it has been modified.                           |
+----------------------------------+-------------------------------------------------+
```
