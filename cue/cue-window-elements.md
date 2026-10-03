# Cue window elements
For cues, Ardour generally follows the design pattern of other
applications that support a grid-based non-linear workflow.

![The Cue window
elements](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/cue-window-elements.png){style="width:75%;"}

The main elements of the [Cue]{.dfn} window are:

1.  Grid of tracks and cues, playback indicators
2.  Mixer channel section
3.  Clip and trigger slot options
4.  Clip editor
5.  Sidebar: Clips, Tracks, Sources, and Regions

## Grid
{#cue_window_grid}

The trigger slots [grid]{.dfn} is comprised of tracks (stacked
horizontally) and cues (stacked vertically). Tracks group clips played
by roughly the same instrument (or set of instruments, in case of drums
and percussion). Cues group clips that will be played simultaneously.

Every [trigger slot]{.dfn} with a clip inside contains three elements:
launch button/indicator, clip title, and follow action
selector/indicator.

[Cue buttons]{.dfn} (A to P) to the left of the grid initiate the
playback of an entire cue. Right-clicking on them opens a menu where
it\'s possible to set the same options for all clips and trigger slots
in that cue:

-   Follow action
-   Launch style
-   Quantization
-   Color

The [playback indication area]{.dfn} displays four pieces of data for
each track:

-   Clip playback progress
-   Which cue the playing clip belongs to
-   MIDI clip indication
-   Follow count

Similarly to cue playback buttons, the playback indication area has a
right-click menu where it\'s possible to set the same options for all
clips and trigger slots in a track of choice.

[This chapter](@@playing-back-the-cues) provides more information on
playback in the [Cue]{.dfn} window.

## Mixer channel section
{#cue_window_mixer_channels}

The mixer channel section is very similar to what\'s available in the
[Mixer]{.dfn} window: there\'s the [processor box](@@processor-box), the
same [panner](@@panning), as well as the [mute and the
solo](@@muting-and-soloing) buttons. Both the fader and the meter are
horizontal, there is no choice for a type of meter.

## Clip and trigger slot options
{#cue_window_clip_options}

The bottom section contains several groups of controls:

-   [Clip Properties](@@clip-properties): full name of a clip in the
    selected trigger slot, loading a different clip, gain control
-   [Launch Options](@@clip-launch-options): how the clips\' playback is
    triggered and within what musical time unit it is quantized
-   [Follow Actions](@@clip-follow-actions): how many times one clip is
    played and what other clip\'s playback is triggered next
-   [Stretch Options](@@clip-stretch-options) (audio-only): stretching
    the original audio data to match current session tempo, adjusting
    assumed original tempo for creative purposes

## Sidebar
{#cue_window_sidebar}

Ardour defaults to displaying the [Clips](@@clips-overview) tab as the
clips browser is commonly used for pulling reusable clips into the
project.

In the Cue context, the [Tracks]{.dfn} tab is mostly useful for marking
a track as visible or not visible in the Cue window.

Both the [Sources]{.dfn} and the [Regions]{.dfn} tabs can work as
drag-and-drop sources for:

-   Placing audio and MIDI data to trigger slots
-   Creating new tracks
-   Creating new reusable clips available from the Clips browser
