# Audio Track Controls
<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/typical-audio-track-controls.png"
alt="audio track controls" />
<figcaption>An audio track header section</figcaption>
</figure>

Each track shows a [header section]{.dfn}, for settings relevant to this
track only.

Changing the height of the track can be done either:

-   By using the [Track \> Height]{.kbd .menu} menu. The [Fit selection
    (Vertical)]{.kbd .menu} (default: [F]{.kbd}) is particularly useful.
-   By double-clicking an empty space in the track header, to toggle the
    track\'s height between the *Normal* and *Largest* track heights
    from this menu.
-   Or by grabbing the bottom of the track header with a [ left]{.kbd
    .mouse} click and drag.

At the top-left of the controls is the name of the track, which can be
edited by double-clicking on it. The new name must be unique within the
session.

Underneath the name is the track\'s main level fader. Changing it will
affect the whole track :

-   [dragging]{.kbd .mouse} will change the fader\'s value as per the
    mouse\'s position
-   [clicking]{.kbd .mod1 .mouse} will set the fader to −∞
-   [clicking]{.kbd .mod3 .mouse} will reset the fader to its original
    0dB position.

On the right-hand side of the headers are level meters for the outputs
of the track (1 level per output).

The control buttons are:

|                                       |                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [●]{.kbd style="color:red;"} (Record) | The button with the pink circle arms the track for recording. When armed, the entire button will turn pink, and change to bright red as soon as the transport is rolling and the track is recording. [Right]{.kbd .mouse} clicking will allow to en/disable Rec-safe, protecting the track against accidental recording. |
| [M]{.kbd} (Mute)                      | Mutes the track. [Right]{.kbd .mouse} clicking displays a menu which dictates what particular parts of the track should be muted.                                                                                                                                                                                        |
| [S]{.kbd} (Solo)                      | Soloes the track. The behaviour of the solo system is described in detail in the section [Muting and Soloing](@@muting-and-soloing). [Right]{.kbd .mouse} clicking will allow to en/disable Solo isolate and Solo safe.                                                                                                  |
| [P]{.kbd} (Playlist)                  | Opens a playlist menu when clicked. The menu offers various operations related to the track\'s [playlist](@@playlists).                                                                                                                                                                                                  |
| [A]{.kbd} (Automation)                | Opens the automation menu for the track. For details see [Automation](@@automation).                                                                                                                                                                                                                                     |
| [G]{.kbd} (Group)                     | Allows to assign the track to an existing or a new group. For details see [Track and bus groups](@@track-and-bus-groups).                                                                                                                                                                                                |
