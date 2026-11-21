# Non-Linear Workflow Principles
The Cue window allows working with music ideas in a non-linear fashion.
Instead of navigating the timeline and placing regions of audio and MIDI
data at a particular point in time, short clips that contain rhythmic
and melodic patterns can be triggered to play a certain amount of times,
then automatically trigger another clip to be played.

The concept has been introduced and popularized by Ableton and since
then found its way into many other applications. Ardour draws many ideas
from Ableton Live, as well as from several other digital audio
workstations, and adapts them to Ardour\'s specifics. Someone familiar
with Live will find many aspects to be similar, but the Cue\'s feature
set is not a 100% copy of that from any other application.

Here are some basics concepts of the non-linear workflow shared by
multiple applications including Ardour.

## Grid and scenes

All clips are organized in a kind of a grid. The grid provides an
overview of all the musical ideas, all the rhythmic patterns, short
melodies, and sound effects that can be used in a composition.

One dimension of the grid, usually represented by a track, would
accumulate clips played with roughly the same kind of an instrument,
e.g. all drum patterns, or all basslines etc.

The other dimension, usually called scenes (or cues, in Ardour) would
organize these clips so that it is possible to play multiple clips at
the same time by pressing just one button. So if one wants a particular
bassline played along a particular drum sequence, they should be placed
in the same scene.

Ardour specifics are explained in the [Cue window
elements](@@cue-window-elements) chapter.

## Slots and clips

Cells in a grid are usually called slots. They are a kind of a container
that can hold an audio or a MIDI clip. Typically, a clip can be loaded
into a slot from a disk by pointing the file selector to it, or loaded
from a pre-recorded library of reusable clips, or recorded in place.
More information about that cqan be found in the [Populating the cue
grid](@@populating-the-cue-grid) chapter.

## Launching

In a non-linear workflow, a clip can be triggered to play in multiple
ways. Most of the time it\'s either pressing a corresponding silicon pad
on an external grid controller attached via MIDI, or scrolling the mouse
wheel downwards over the slot that contains the clip, or just clicking a
\'Play\' button next to clip\'s name.

Usually, a slot can be configured to respond to some ways to trigger
clip playback and ignore others. This is discussed in depth in the [Clip
Launch Options](@@clip-launch-options) chapter.

## Follow actions

A clip can play in a loop until stopped directly, or it can play a
user-defined amount of time and then trigger another clip in the track.
As an example, a composition can start with one rhythmic pattern played
four times and the next rhythmic patterns is played eight times, then a
third one is started.

This is typically achieved through so called follow actions. In an
example above, for the first clip (or, rather, slot), a follow count
must be set (4 times), and the follow action usually called \"Next\" is
used. This will get the clip in that first slot to play 4 times then
trigger the playback of a clip in the second slot.

Every application has its own set of follow actions. Most common ones
are repeating the clip indefinitely, triggering the previous/next slot,
or jumping to a slot in a particular scene.

More information about follow actions in Ardour can be found
[here](@@clip-follow-actions).

## Musical time and stretching

In a non-linear workflow, all work is happening in musical time: both
audio and MIDI clips are measured in bars and beats.

By default, an application that supports a non-linear workflow will
attempt to estimate beats per minute in an audio clip and then stretch
or squeeze the clip so that it would match the bpm of the session and
wrap neatly around bars. That way, a clip that originally has a
different tempo that the one in the session would stay in sync with
other clips.

Stretch options in Ardour are explained [here](@@clip-stretch-options).
