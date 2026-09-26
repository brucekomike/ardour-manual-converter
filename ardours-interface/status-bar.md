# Status Bar
![The Status Bar](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/status-bar.png)

The status bar is an informative bar at the top of the window. Right
clicking anywhere on the Status Bar allows to choose which of this
information is displayed, through a checkbox menu, among:

|                                       |                                                                                                                                                                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Path to Session:                      | the folder where the session files are                                                                                                                                                                          |
| Snapshot Name and Modified Indicator: | the name of the snapshot being worked on. If the session has been modified since last save, the name is prefixed with an asterisk (\*).                                                                         |
| Active Peak-file work:                | *(only shows up while creating peaks)* displays the number of peak files left to create                                                                                                                         |
| File Format:                          | the file format used in the session, including when recording                                                                                                                                                   |
| Timecode Format:                      | is the timecode, i.e. the number of frames per second used by the session (for videos)                                                                                                                          |
| Audio:                                | gives the sample rate used in the session, and the latency computed from the buffer size                                                                                                                        |
| Disk Space:                           | reports the remaining hard disk space as the time that can be recorded with the current session setting                                                                                                         |
| DSP:                                  | for *D*igital *S*ound *P*rocessing, shows worst case system load used by Ardour and plugins for realtime processing. The value is the percentage of *time required to process* vs. *time available to process*. |
| Wall Clock                            | showing the system time (especially useful in full screen mode)                                                                                                                                                 |
| Log button                            | that indicates if Ardour has encountered any warning or error.                                                                                                                                                  |

Some of these indicators also double as a shortcut to a relevant action,
triggered by double clicking the info field:

|                                                        |                                                                                                                                     |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Path to Session / Snapshot Name and Modified Indicator | opens the session path in the file explorer                                                                                         |
| File Format:                                           | opens the *Media* section of the [Session Properties](@@session-properties#properties-media)                                        |
| Timecode Format:                                       | opens the *Timecode* section of the [Session Properties](@@session-properties#properties-timecode)                                  |
| Audio:                                                 | opens the [Audio MIDI Setup](@@audio-midi-setup) window.                                                                            |
| Log button                                             | The log button turns yellow when a warning is shown, and red when an error occurs. Clicking the log button gives access to the log. |
