# Rulers
![Ardour\'s Ruler](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/ruler.png){style="width:100%;"}

The [ruler]{.dfn} scales the session along time, allows navigating, and
can be marked for different uses.

One of its main uses is to move the playhead: clicking anywhere on the
timeline will bring the playhead at this location in time. Also, using
the mouse\'s scrollwheel while hovering the ruler will zoom in or out
([⇑]{.kbd .mouse}/[⇓]{.kbd .mouse} ).

The ruler is made of a succession of rows, each having a special role
related to time. Adding or removing rows can be done by [right]{.kbd
.mouse} clicking anywhere in the ruler\'s header on the left, and
ticking any of:

|                          |                                                                                                                                                                                  |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Mins:Secs]{.dfn}        | scaling the session with the Mins:Secs:mSec notation                                                                                                                             |
| [Timecode]{.dfn}         | scaling the session with the Hours:Mins:Secs:Frames notation                                                                                                                     |
| [Samples]{.dfn}          | scaling the session with the sample number notation                                                                                                                              |
| [Bars:Beats]{.dfn}       | slicing the time according to the time signature                                                                                                                                 |
| [Time Signature]{.dfn}   | shows the time signature. It can be changed along the timeline, by [Right-click]{.kbd .mouse} \> [New Time Signature]{.kbd .menu}. The Bars:Beats ruler will reflect the change. |
| [Tempo]{.dfn}            | shows the BPM. It can be changed along the timeline, by [Right-click]{.kbd .mouse} \> [New Tempo]{.kbd .menu}. The Bars:Beats ruler will reflect the change.                     |
| [Range Markers]{.dfn}    | allow to create and modify ranges directly on the Ruler.                                                                                                                         |
| [Location Markers]{.dfn} | is meant to receive any kind of marker, user generated or from Ardour itself.                                                                                                    |
| [Arrangement]{.dfn}      | allows creating range sections like a verse, a chorus, a bridge etc.                                                                                                             |
| [Video Timeline]{.dfn}   | shows thumbnails of the [video](@@video-timeline-and-monitoring) in the timeline                                                                                                 |

Most rulers allow placing markers to serve a specific purpose: mark a
point in time, define a loop range, or something else entirely.

Most of the operations on the markers are described in [Working with
Markers](@@working-with-markers), additional information on Time
Signature, Tempo, Bars:Beats, and Timecode is available in the [Tempo
and Time Signature](@@tempo-and-meter) chapter.
