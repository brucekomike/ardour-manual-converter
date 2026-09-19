# Using the PreSonus FaderPort
Ardour has full support for the Presonus Faderport controller. This is a
compact control surface featuring a single motorized fader, a single
knob (encoder) and 24 buttons with fixed labels. It is a relatively
low-cost device that functions very well to control a single (selected)
track or bus, along with a variety of other \"global\" settings and
conditions.

## Connecting the Faderport

The Faderport comes with a single USB socket on the back. Connect a
suitable USB cable from there to a USB port on your computer. As of the
end of 2015, you should avoid USB3 ports---these cause erratic behaviour
with the device. This issue might get fixed by Presonus in the future.

Ardour uses the Faderport in what Presonus calls \"native\" mode. You do
not need to do anything to enable this---Ardour will set the device to
be in the correct mode. In native mode, the Faderport sends and receives
ordinary MIDI messages to/from the host, and the host understands the
intended meaning of these messages. We note this detail to avoid
speculation about whether Ardour supports the device via the HUI
protocol---it does not.

The Faderport will be automatically recognized by your operating system,
and will appear in any of the lists of possible MIDI ports in both
Ardour and other similar software.

To connect the Faderport to Ardour, open the Preferences dialog, and
then click on \"Control Surfaces\". Click on the \"Enable\" button in
the line that says \"Faderport\" in order to activate Ardour\'s
Faderport support. Then double click on the line that says
\"Faderport\". A new dialog will open, containing (among other things)
two dropdown selectors that will allow you to identify the MIDI ports
where your Faderport is connected.

![The Faderport configuration dialog](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/faderport_dialog.png)

Once you select the input and output port, Ardour will initialize the
Faderport and it will be ready to use. You only need do this once: once
these ports are connected and your session has been saved, the
connections will be made automatically in this and other future
sessions.

You do not need to use the power supply that comes with the Faderport
but without it, the fader will not be motorized. This makes the overall
experience of using the Faderport much less satisfactory, since the
fader will not move when Ardour tells it to, leading to very out-of-sync
conditions between the physical fader position and the \"fader
position\" inside the program.

## Using the Faderport

The Faderport\'s controls can be divided into three groups:

1.  Global controls such as the transport buttons
2.  Controls which change the settings for particular track or bus
3.  Controls which alter which track or bus is modified by the
    per-track/bus controls.

Because the Faderport has only a single set of per-track controls, by
default those controls operate on the first selected track or bus. If
there is no selected track or bus, the controls will do nothing.

### Transport Buttons

The transport buttons all work as you would expect.

```{eval-rst}
+-----------------------------------+-----------------------------------+
| Rewind                            | When pressed on its own, starts   |
|                                   | the transport moving backwards.   |
|                                   | Successive presses speed up the   |
|                                   | \"rewind\" behaviour.             |
|                                   |                                   |
|                                   | If pressed while also holding the |
|                                   | Stop button, the playhead will    |
|                                   | return to the zero position on    |
|                                   | the timeline.                     |
|                                   |                                   |
|                                   | If pressed while also holding the |
|                                   | Shift button, the playhead will   |
|                                   | move to the session start marker. |
+-----------------------------------+-----------------------------------+
| Fast Forward                      | When pressed on its own, starts   |
|                                   | the transport moving faster than  |
|                                   | normal. Successive presses speed  |
|                                   | up the \"fast forward\"           |
|                                   | behaviour.                        |
|                                   |                                   |
|                                   | If pressed while also holding the |
|                                   | Shift button, the playhead will   |
|                                   | move to the session end marker.   |
+-----------------------------------+-----------------------------------+
| Stop                              | Stops the transport. Also used in |
|                                   | combination with the Rewind       |
|                                   | button to \"return to zero\".     |
+-----------------------------------+-----------------------------------+
| Play                              | Starts the transport. If pressed  |
|                                   | while the transport is already    |
|                                   | rolling at normal speed, causes   |
|                                   | the playhead to jump to the start |
|                                   | of the last \"roll\" and continue |
|                                   | rolling (\"Poor man\'s            |
|                                   | looping\").                       |
+-----------------------------------+-----------------------------------+
| Record Enable                     | Toggles the global record enable  |
|                                   | setting                           |
+-----------------------------------+-----------------------------------+
```

### Other Global Controls

The [Mix]{.kbd .button}, [Proj]{.kbd .button}, [Trns]{.kbd .button}
buttons do not obviously correspond to any particular functions or
operations in Ardour. We have therefore allowed users to choose from a
carefully curated set of possible actions that seem related to the
button labels in some clear way. This can be done via the Faderport
configuration dialog accessed via `Preferences > Control Surfaces`. Each
button has 3 possible actions associated with it:

-   Plain Press: action to be taken when the button is pressed on its
    own.
-   Shift-Press: action to be taken when the button is pressed in
    conjunction with the Shift button.
-   Long Press: action to be taken when the button is pressed on its own
    and held down for more than 0.5 seconds.

Click on the relevant drop-down selector to pick an action as you
prefer.

The User button also has no obvious mapping to specific Ardour
functionality, so we allow users to choose from *any* possible GUI
action. The menu for selecting the action is somewhat confusing and it
can be hard to find what you\'re looking for. However, all possible
actions are there, so keep looking!

```{eval-rst}
+-----------------------------------+-----------------------------------+
| Mix                               | Possible actions include:         |
|                                   |                                   |
|                                   | -   Toggle Editor & Mixer         |
|                                   |     visibility                    |
|                                   | -   Show/Hide the Editor mixer    |
|                                   |     strip                         |
+-----------------------------------+-----------------------------------+
| Proj                              | Possible actions include:         |
|                                   |                                   |
|                                   | -   Toggle Meterbridge visibility |
|                                   | -   Toggle Session Summary        |
|                                   |     visibility                    |
|                                   | -   Toggle Editor Lists           |
|                                   |     visibility                    |
|                                   | -   Zoom to session               |
|                                   | -   Zoom in                       |
|                                   | -   Zoom out                      |
+-----------------------------------+-----------------------------------+
| Trns                              | Possible actions include:         |
|                                   |                                   |
|                                   | -   Toggle Locations window       |
|                                   |     visibility                    |
|                                   | -   Toggle Metronome              |
|                                   | -   Toggle external sync          |
|                                   | -   Set Playhead at current       |
|                                   |     pointer position              |
+-----------------------------------+-----------------------------------+
| Undo/Redo                         | Undo Causes the last operation    |
|                                   | carried out in the editor to be   |
|                                   | undone. When pressed in           |
|                                   | conjunction with the Shift        |
|                                   | button, it causes the most recent |
|                                   | undone operation to be re-done.   |
+-----------------------------------+-----------------------------------+
| Punch                             | When pressed on its own, toggles  |
|                                   | punch recording. If there is no   |
|                                   | punch range set for the session,  |
|                                   | this will do nothing.             |
|                                   |                                   |
|                                   | When pressed in conjunction with  |
|                                   | the Shift button, this moves the  |
|                                   | playhead to the previous Marker   |
+-----------------------------------+-----------------------------------+
| User                              | See above. Any and all            |
|                                   | GUI-initiated actions can be      |
|                                   | driven with by pressing this      |
|                                   | button on its own, or with a      |
|                                   | \"long\" press.                   |
|                                   |                                   |
|                                   | When pressed in conjunction with  |
|                                   | the Shift button, this will move  |
|                                   | the playhead to the next marker.  |
+-----------------------------------+-----------------------------------+
| Loop                              | When pressed on its own, this     |
|                                   | toggles loop playback. If the     |
|                                   | Ardour preference                 |
|                                   | \"Loop-is-mode\" is enabled, this |
|                                   | does nothing to the current       |
|                                   | transport state. If that          |
|                                   | preference is disabled, then      |
|                                   | engaging loop playback will also  |
|                                   | start the transport.              |
|                                   |                                   |
|                                   | When pressed in conjunction with  |
|                                   | the Shift button, this will       |
|                                   | create a new (unnamed) marker at  |
|                                   | the current playhead position.    |
+-----------------------------------+-----------------------------------+
```

### Per-track Controls

```{eval-rst}
+-----------------------------------+-----------------------------------+
| Mute                              | This toggles the mute setting of  |
|                                   | the currently controlled          |
|                                   | track/bus. The button will be lit |
|                                   | if the track/bus is muted.        |
+-----------------------------------+-----------------------------------+
| Solo                              | This toggles the solo (or listen) |
|                                   | setting of the currently          |
|                                   | controlled track/bus. The button  |
|                                   | will be lit if the track/bus is   |
|                                   | soloed (or set to listen mode).   |
+-----------------------------------+-----------------------------------+
| Rec                               | This toggles the record-enabled   |
|                                   | setting of the currently          |
|                                   | controlled track/bus. The button  |
|                                   | will be lit if the track is       |
|                                   | record-enabled. This button will  |
|                                   | do nothing if the Faderport is    |
|                                   | controlling a bus.                |
+-----------------------------------+-----------------------------------+
| Fader                             | The fader controls the gain       |
|                                   | applied to the currently          |
|                                   | controlled track/bus. If the      |
|                                   | Faderport is powered, changing    |
|                                   | the gain in Ardour\'s GUI or via  |
|                                   | another control surface, or via   |
|                                   | automation, will result in the    |
|                                   | fader moving under its own        |
|                                   | control.                          |
+-----------------------------------+-----------------------------------+
| Knob/Dial/Encoder                 | The knob controls 1 or 2 pan      |
|                                   | settings for the current          |
|                                   | controlled track/bus. When used   |
|                                   | alone, turning the knob controls  |
|                                   | the \"azimuth\" or \"direction\"  |
|                                   | (between left and right) for the  |
|                                   | panner in the track/bus (if any). |
|                                   | This is all you need when         |
|                                   | controlling tracks/busses with 1  |
|                                   | input and 2 outputs.              |
|                                   |                                   |
|                                   | If controlling a 2 input/2 output |
|                                   | track/bus, Ardour\'s panner has   |
|                                   | two controls: azimuth (direction) |
|                                   | and width. The width must be      |
|                                   | reduced to less than 100% before  |
|                                   | the azimuth can be changed.       |
|                                   | Pressing the \"Shift\" button     |
|                                   | while turning the knob will alter |
|                                   | the width setting.                |
|                                   |                                   |
|                                   | The knob can also be turned while |
|                                   | the \"User\" button is held, in   |
|                                   | order to modify the input gain    |
|                                   | for the currently controlled      |
|                                   | track.                            |
+-----------------------------------+-----------------------------------+
| Read                              | Enables playback/use of fader     |
|                                   | automation data by the controlled |
|                                   | track/bus.                        |
+-----------------------------------+-----------------------------------+
| Write                             | Puts the fader for the controlled |
|                                   | track/bus into automation write   |
|                                   | mode. While the transport is      |
|                                   | rolling, all fader changes will   |
|                                   | be recorded to the fader          |
|                                   | automation lane for the relevant  |
|                                   | track/bus.                        |
+-----------------------------------+-----------------------------------+
| Touch                             | Puts the fader for the controlled |
|                                   | track/bus into automation touch   |
|                                   | mode. While the transport is      |
|                                   | rolling, touching the fader will  |
|                                   | initiate recording all fader      |
|                                   | changes until the fader is        |
|                                   | released. When the fader is not   |
|                                   | being touched, existing           |
|                                   | automation data will be           |
|                                   | played/used to control the gain   |
|                                   | level.                            |
+-----------------------------------+-----------------------------------+
| Off                               | This disables all automation      |
|                                   | modes for the currently           |
|                                   | controlled track/bus. Existing    |
|                                   | automation data will be left      |
|                                   | unmodified by any fader changes,  |
|                                   | and will not be used for          |
|                                   | controlling gain.                 |
+-----------------------------------+-----------------------------------+
```

### Track Selection Controls

You can manually change the track/bus controlled by the Faderport by
changing the selected track in Ardour\'s editor window. If you select
more than 1 track, the Faderport will control the first selected track
and *only* that track/bus.

```{eval-rst}
+-----------------------------------+-----------------------------------+
| Left (arrow)                      | This causes the Ardour GUI to     |
|                                   | select the previous track/bus     |
|                                   | (using the current visual order   |
|                                   | in the editor window), which will |
|                                   | in turn cause the Faderport to    |
|                                   | control that track. If there is   |
|                                   | no previous track/bus, the        |
|                                   | selected track/bus is left        |
|                                   | unchanged, and the Faderport      |
|                                   | continues to control it.          |
+-----------------------------------+-----------------------------------+
| Right (arrow)                     | This causes the Ardour GUI to     |
|                                   | select the next track/bus (using  |
|                                   | the current visual order in the   |
|                                   | editor window), which will in     |
|                                   | turn cause the Faderport to       |
|                                   | control that track. If there is   |
|                                   | no next track/bus, the selected   |
|                                   | track/bus is left unchanged, and  |
|                                   | the Faderport continues to        |
|                                   | control it.                       |
+-----------------------------------+-----------------------------------+
| Output                            | Pressing the Output button causes |
|                                   | the Faderport to control the      |
|                                   | fader, pan, mute and solo         |
|                                   | settings of the Master bus. If    |
|                                   | your session does not contain a   |
|                                   | Master bus, it does nothing. This |
|                                   | is a toggle button---pressing it  |
|                                   | again returns Faderport to        |
|                                   | controlling whichever track/bus   |
|                                   | was selected before the first     |
|                                   | press of the Output button.       |
|                                   |                                   |
|                                   | If your session uses Ardour\'s    |
|                                   | monitor section, you can use      |
|                                   | Shift-Output to assign it to the  |
|                                   | Faderport in the same way that    |
|                                   | Output assigns the Master bus.    |
|                                   | This is also a toggle setting, so |
|                                   | the second Shift-Output will      |
|                                   | return the Faderport to           |
|                                   | controlling whichever track/bus   |
|                                   | was selected before.              |
|                                   |                                   |
|                                   | If you press Shift-Output after a |
|                                   | single press to Output (i.e.      |
|                                   | control the Monitor Section while |
|                                   | currently controlling the Master  |
|                                   | bus) or vice versa (i.e. control  |
|                                   | the Master bus while currently    |
|                                   | controlling the Monitor Section), |
|                                   | the press will be ignored. This   |
|                                   | avoids getting into a tricky      |
|                                   | situation where it is no longer   |
|                                   | apparent what is being controlled |
|                                   | and what will happen if you try   |
|                                   | to change it.                     |
+-----------------------------------+-----------------------------------+
| Bank                              | The \"Bank\" button is currently  |
|                                   | not used by Ardour                |
+-----------------------------------+-----------------------------------+
```
