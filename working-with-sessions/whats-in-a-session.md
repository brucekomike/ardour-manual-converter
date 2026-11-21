# What's in a Session?
The [Session]{.dfn} is the fundamental document type that is created and
modified by the Ardour workstation. A Session is a folder on a computer
filesystem that contains all the items that pertain to a particular
project or \"recording/editing/mixing session\".

The Session folder includes these files and folders:

- *`session_name`*`.ardour` the main session snapshot
- `*.ardour`, any additional snapshots
- *`session_name`*`.ardour.bak`, the auto-backup snapshot
- *`session_name`*`.history`, the undo history for the session
- `instant.xml`, which records the last-used zoom scale and other
  metadata
- `interchange/`, a folder which holds the raw audio and MIDI files
  (whether imported or recorded)
- `export/`, a folder which contains any files created by the [Session
  \> Export]{.kbd .menu} function
- `peaks/`, a folder which contains waveform renderings of all audio
  files in the session
- `analysis/`, a folder which contains transient and pitch information
  of each audio file that has been analysed
- `dead sounds/`, a folder which contains sound files which Ardour has
  detected are no longer used in the session (during a [Session \>
  Clean-up \> Clean-up Unused Sources]{.kbd .menu} operation, will be
  purged by [Flush Waste Basket]{.kbd .menu}, see [Cleaning Up
  Sessions](@@cleaning-up-sessions))

A session combines some setup information (such as audio and MIDI
routing, musical tempo & meter, timecode synchronization, etc.) with one
or more Tracks and Buses, and all the Regions and Plug-Ins they contain.

Ardour supports loading session files created with older versions of the
program. The oldest known version is 2.8 released in 2009. With very few
exceptions, Ardour will load all session data from such files. The data
that cannot be supported (e.g. the old way of storing region fades) will
be skipped entirely.
