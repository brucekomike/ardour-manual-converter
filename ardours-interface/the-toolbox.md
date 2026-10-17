# Toolbox
<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/toolbar-tools.png" style="width:50.0%"
alt="Editor toolbar&#39;s tools, aka toolbox" />
<figcaption>Editor toolbar's tools, AKA toolbox.</figcaption>
</figure>

## Global Edit mode

Ardour has a global [Edit Mode]{.dfn} selector at the left side of the
Editing toolbar, which affects how regions are moved or copied:

|                      |                                                                       |
|----------------------|-----------------------------------------------------------------------|
| [Slide]{.kbd .menu}  | Regions move freely. Ardour creates overlaps when necessary.          |
| [Ripple]{.kbd .menu} | Editing affects the regions to the \"right\" of the edit (see below). |
| [Lock]{.kbd .menu}   | No region motion is permitted (except for \"nudge\").                 |

The general idea behind the Ripple edit mode is this:

-   Deleting a range will move later regions to compensate for the
    deleted time
-   Deleting a region will move later regions to compensate for the
    deleted region\'s length
-   Moving a region will move later regions to compensate for the length
    of the move
-   Inserting a new region (via dragging or via Paste) will move later
    regions to the right to compensate

Within this general behavior several variations are available as Ripple
edit modes:

1.  [Selected]{.dfn}. Only applies the ripple logic to currently
    selected tracks. After making a selection, you can use the
    [Alt]{.kbd .button} modifier and click on tracks to add or remove
    them to/from the selection. Markers will stay intact.
2.  [All]{.dfn}. Applies the ripple logic to all tracks on the timeline
    and shifts location, CD, and cue markers accordingly. Selecting a
    range with this mode will automatically make a time-constrained
    selection in all tracks of the project.
3.  [Interview]{.dfn}. This mode works just like the [Selected]{.dfn}
    mode with one exception: when you select a range and press
    [Del]{.kbd .button}, this will remove the selected portion of either
    audio or MIDI without shifting other clips to the left to match the
    freed space on the timeline. The main use case for this mode is
    editing interviews where you want the ripple behavior to edit out
    e.g. periods of silence, while being able to just delete e.g. an
    out-of-place noise or an exclamation by the interviewer.

If [Snap To Grid]{.kbd .menu} is enabled, then regions can only move so
that they align with locations determined by the current snap settings
(beats, or seconds, or other region boundaries, etc). See [Snap To the
Grid](@@grid-controls) for details.

## The Edit Point selector
{#edit-point}

Numerous editing operations require the definition of an Edit Point,
that is chosen in this selector. More information about the Edit Point
can be found [here](@@edit-point-control).

## The *Smart* mode toggle switch
{#smart-mode}

The [Smart Mode]{.dfn} toggle button (shortcut: [y]{.kbd}) to the left
of the mouse mode buttons modifies the behavior of [Grab Mode]{.dfn}:
when enabled, the mouse behaves as if it is in [Range Mode]{.dfn} in the
upper half of a region, while behaving as if it is in [Grab Mode]{.dfn}
in the lower half. This makes it possible to avoid constant switching
between these two modes.

## Mouse Modes

Editing [regions](@@working-with-regions) and their contents is very
complex and, by virtue of this, requires different [Mouse Modes]{.dfn}
in order to be able to perform typical editing chores in a way that is
powerful and makes sense.

|               |                       |
|---------------|-----------------------|
| **Mode**      | **Keyboard Shortcut** |
| Grab          | [G]{.kbd}             |
| Range         | [R]{.kbd}             |
| Cut           | [C]{.kbd}             |
| Audition      | None                  |
| Stretch       | [T]{.kbd}             |
| Grid          | [Y]{.kbd}             |
| Draw          | [D]{.kbd}             |
| Internal Edit | [E]{.kbd}             |

Changes to the mouse pointer only occur when hovering over the track
canvas; the mouse pointer *always* changes to a hand in the ruler area
regardless of what mode is selected, and always moves the
[playhead](@@controlling-playback) to the position [left]{.kbd
.mouse}-clicked on---as long as there is no marker or other tag under
the mouse position clicked on.

### Grab Mode
{#object}

[Grab Mode]{.dfn} is used for selecting, moving, deleting and copying
objects. In this mode, the mouse pointer appears as a hand and can be
used to select and perform various operations on objects such as
regions, markers etc.... This is the most common mode to work in, as it
allows the for selection and moving of
[regions](@@working-with-regions), as well as the modification of
control points in [automation lanes](@@automation-lanes).

### Range Mode
{#range}

In [Range Mode]{.dfn}, the mouse pointer appears as a vertical line;
[left]{.kbd .mouse}-clicking on the track canvas will display the time
at the position clicked on. [left]{.kbd .mouse}-clicking and dragging on
the track canvas will create a time range for the track clicked and
dragged on; adjacent tracks can be selected as well by dragging the
mouse into them. Once a time range has been defined, it can be resized
by [left]{.kbd .mouse}-clicking on either the left-hand or right-hand
side of the range and dragging the mouse to the desired position.

### Cut Tool Mode
{#cut}

In [Cut Tool Mode]{.dfn}, the mouse pointer appears as a pair of
scissors and allows for the separation of any region into two distinct
regions by [left]{.kbd .mouse}-clicking at the desired point of
separation. If more than one track is selected, then all the regions on
the selected tracks will be split at the point clicked on. If no track
is selected, then only the region hovered by the mouse cursor will be
split.

### Stretch Mode
{#stretch}

In [Stretch Mode]{.dfn}, the mouse pointer appears as an expanding
square symbol and is used to resize regions using a timestretch
algorithm. Resizing a region is done by [left]{.kbd .mouse}-clicking on
the right-hand side of the region and dragging the edge to the desired
position; once the button is released a [Time Stretch Audio]{.kbd .menu}
dialog will appear, as detailed in the dedicated
[Stretching](@@stretching) page.

### Audition Mode
{#audition}

[left]{.kbd .mouse}-clicking on a given region using [Audition
Mode]{.dfn} will play the the session for the time span of that region.
The regions can also be [scrubbed]{.dfn} by [left]{.kbd .mouse}-clicking
and dragging in the direction desired; the amount dragged in one
direction or the other will determine the playback speed.

### Grid Mode
{#grid}

The Grid mode has been designed to easily create and edit tempo maps.

[Left]{.kbd .mouse}-clicking on the timeline above a bar line creates a
new tempo marker.

[Left]{.kbd .mouse}-clicking and dragging on the timeline above a bar
line when a tempo marker already exists in that position changes the
value of the current and the previous markers to accomodate for.

[Left]{.kbd .mouse}-clicking and dragging on the timeline anywhere
between two bar lines creates a tempo ramp.

### Draw Mode
{#draw}

In [Draw Mode]{.dfn}, the mouse pointer will change to a pencil; the
effect it will have depends on the type of track or region it is
utilized in.

In an [audio track](@@audio-track-controls), a green line will appear in
the region which is that region\'s [[gain
envelope]{.dfn}](@@gain-envelopes). [left]{.kbd .mouse}-clicking
anywhere in a given region between two existing [control points]{.dfn}
will add one to the region at the X-coordinate clicked on with the
Y-coordinate being on the line connecting the control points on either
side of the new one. [left]{.kbd .mouse}-clicking on a control point
will allow it to be moved to any point in the region in between the
control points that bound it on either side of itself. And finally,
[left]{.kbd .mouse}-clicking on a control point and pressing the
[delete]{.kbd} key or holding down the []{.kbd .mod3n} key while
[right]{.kbd .mouse}-clicking on it will delete the control point.

In an [automation lane](@@automation-lanes), if any automation is
defined in it, a green line connecting its control points will appear in
the lane. Control points in the lane are manipulated in exactly the same
way as they are in a region\'s gain envelope (see previous paragraph for
details).

In a [MIDI track](@@midi-track-controls),

-   [left]{.kbd .mouse}-clicking in a part of the track that has no
    region, creates a one-bar long region, while [left]{.kbd
    .mouse}-dragging will create a region of arbitrary length.
-   [left]{.kbd .mouse}-clicking on a region in Percussive mode creates
    a diamond indicating a hit.
-   [left]{.kbd .mouse}-clicking on a region in Sustained mode creates a
    note whose duration is one [Grid unit](@@grid-controls), while
    [left]{.kbd .mouse}-dragging creates a note of arbitrary Grid units
    length.

### Internal Edit Mode
{#edit-internal}

In [Internal Edit Mode]{.dfn}, the mouse pointer will change to
cross-hairs.

-   On an automation lane, it allows to edit the automation like the
    Draw tool.
-   On a MIDI region, it allows to lasso-select multiple notes at a
    time.
-   On an audio region, it displays the current level of the signal and
    allows to edit the region gain like the Draw tool.
