# Playing Back the Cues
It is possible to play both individual clips and entire cues.

## Playing and Stopping Individual Clips

There are generally two ways to trigger a slot with a clip inside.

1.  Pressing a mouse button over the button to the left of the clip\'s
    name (Ardour defaults to Trigger launch style which has a classical
    triangle playback icon)
2.  Sending a note-on event from an external or a virtual MIDI
    controller

How Ardour responds to releasing the mouse button or sending a note-off
event depends on the trigger launch style. [This
chapter](@@clip-launch-options) covers that topic.

Once the clip starts playing, the playback indication panel for that
track lights up with some information:

![Playback
indication](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/trigger-slot-playing.png){style="width:50%;"}

Left to right:

-   Clip progress, in the form of a sliding pie chart
-   Which cue is playing (it\'s C on the screenshot)
-   MIDI clip indication, an icon representing two beamed 1/16 notes
-   Follow count, e.g. \'1/2\' on the screenshot means the clip is
    currently being played the first time out of two times total

One way to stop a playing clip is to click the square-shaped icon in any
of the empty slots in the track of interest.

Ardour allows assigning arbitrary keys on MIDI controllers to trigger
cue slots by:

1.  [Right]{.kbd .mouse}-clicking on the trigger slot of interest
2.  Choosing [MIDI Learn]{.kbd .menu} in the newly opened window
3.  Pressing a key on the MIDI controller

An existing assignment can be removed using the [MIDI un-Learn]{.kbd
.menu} command in the same right-click menu.

This use of MIDI devices and its learning function is separate from,
functions differently to, and is not to be confused with the use of MIDI
devices as control surfaces.

For a MIDI device to be used to trigger clips it must be defined as
Default trigger input in the [Triggering]{.kbd .menu} page of the
[Preferences]{.kbd .menu} dialog and/or be connected to the
`ardour:Cue Control in` MIDI port.

## Playing and Stopping Entire Cues

Clicking a round-shaped button with a Latin letter inside launches the
playback of the entire cue, that is, all clips in all trigger slots of a
cue.

![Entire Cue
Playback](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/entire-cue-playback.png){style="width:75%;"}

The time when playback of each slot starts depends on the launch
quantization setting. If there is no quantization selected, playback
will start immediately regardless of the playhead\'s position. However,
if the launch quantization is set to 1 bar, playback will only start
once the playhead passes the start of the closest bar. This ensures that
however long each clip is when measured in beats, all clips in one cue
will play in sync.

Clicking the square-shaped button under the last letter-coded cue
(**P**) will stop playback of all cues and all clips in all trigger
slots. Just like with playback, the time playback stops depends on
quantization settings of each trigger slot.
