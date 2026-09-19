# Creating Music with Ardour
Ardour can be used in many different ways, from extremely simple to
extremely complex. Many projects can be handled using the following kind
of [workflow]{.dfn}:

## Stage 1: Creating The Project
{#creating-the-project}

The first step is to create a new [session]{.dfn}, or open an existing
one. A session consists of a folder containing a session file that
defines all the information about the session. All media files used by
the session are usually stored within the session folder.

More details on sessions can be found in [Sessions](@@sessions) chapter.

## Stage 2: Creating and Importing Audio and MIDI Data
{#creating-and-importing-audio-midi}

Once a session has been created, it will be necessary to add some audio
and/or MIDI material to it---which can be done in one of 3 ways:

-   [Record]{.dfn} incoming audio or MIDI data, either via audio or MIDI
    hardware connected to the computer, or from other applications
-   [Create]{.dfn} new MIDI data using the mouse and/or various dialogs
-   [Import]{.dfn} existing media files into the session

[MIDI recordings]{.dfn} consist of performance data (\"play note X at
time T\") rather than actual sound. As a result, they are more flexible
than actual audio, since the precise sound that they will generate when
played depends on where the MIDI data is sent to. Two different
synthesizers may produce very different sounds in response to the same
incoming MIDI data.

[Audio recordings]{.dfn} can be made from external instruments with
electrical outputs (keyboards, guitars, etc.), or via microphones or
other sound capturing equipment.

Ardour can use the [JACK Audio Connection Kit]{.dfn} for all audio and
MIDI I/O, making recording audio/MIDI from other applications
fundamentally identical to recording audio/MIDI from audio/MIDI
hardware.

## Stage 3: Editing and Arranging
{#editing-arranging}

Once there is material within the session, it can be arranged in time.
This is done in one of the two main windows of Ardour: the
[Editor]{.dfn} window.

Audio/MIDI data appears in chunks called [regions]{.dfn}, which are
arranged into horizontal lanes called [tracks]{.dfn}. Tracks are stacked
vertically in the Editor window. Regions can be copied, shortened,
moved, and deleted without changing the actual data stored in the
session at all---Ardour is a [non-destructive]{.dfn} editor. (Almost)
nothing done while editing will ever modify the files stored on disk
(with the exception of the session file itself).

Many [transformations]{.dfn} can be done to the contents of regions,
again without altering anything on disk. It is possible to alter, move,
delete and remove silence from audio regions, for example.

MIDI regions can also be copied, moved, shortened, or deleted without
altering the MIDI files, though any edit like adding, suppressing or
moving *notes* inside a region results in a modification of the
underlying MIDI file.

## Stage 4: Mixing and Adding Effects
{#mixing-effects}

Once the arrangement of the session is mostly complete, the next step is
the [mixing]{.dfn} phase. Mixing is a broad term to cover the way the
audio signals that the session generates during playback are processed
and added together into a final result that is actually heard. It can
involve altering the relative levels of various parts of the session,
adding effects that improve or transform certain elements, and others
that bring the sound of the whole session to a new level.

Ardour allows [automation]{.dfn} of changes to any mixing parameters
(such as volume, panning, and effects controls)---it will record the
changes made over time, using a mouse or keyboard or some external
control device, and can play back those changes later. This is very
useful because often the settings needed will vary in one part of a
session compared to another---rather than using a single setting for the
volume of a track, it may need increases followed by decreases (for
example, to track the changing volume of a singer). Using automation can
make all of this relatively easy.

## Stage 5: Exporting
{#exporting}

Once the arrangement and mix of the session is finalized, a single audio
file that contains a ready-to-listen to version of the work is usually
desired. Ardour allows the [exporting]{.dfn} of audio files in a variety
of formats (simultaneously in some cases). This exported file would
typically be used in creating a CD, or be the basis for digital
distribution of the work.

Of course it is sometimes desirable to export material that isn\'t
finished yet---for example, to give a copy to another party to mix on
their own system. Ardour allows exporting as much of a session as
desired, at any time, in any supported format.
