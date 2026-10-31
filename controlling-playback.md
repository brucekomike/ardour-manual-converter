# Controlling Playback
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/the-playhead.png" alt="The playhead" />
<figcaption aria-hidden="true">The playhead</figcaption>
</figure>

The [playhead]{.dfn} is a red vertical line that indicates the current
position of playback.

## Positioning the Playhead

### Positioning the playhead at the current pointer position

Pressing [P]{.kbd} will set the playhead to the current position of the
mouse pointer, if it is within the editor track area.

### Positioning the playhead on the timeline

A [Left]{.kbd .mouse} click anywhere on the [Ruler](@@ruler) will move
the playhead to that position.

### Positioning the playhead with the transport clocks

Clicking on either the primary or secondary transport clock and [editing
their value](@@editing-clocks) moves the playhead to a specific
position.

### Positioning the playhead at a marker

[Right]{.kbd .mouse} clicking on the marker and selecting either [Locate
to Here]{.kbd .menu} or [Play from Here]{.kbd .menu} will place the
playhead at the marker\'s position.

Alternatively, placing the mouse pointer on the marker and pressing
[P]{.kbd} sets the playhead precisely on the marker location.

## Looping the Transport

When the [loop transport](@@the-loop-range) button is pressed, the
playhead will jump the start of the loop range, and continue to the end
of that range before returning to the start and repeating.

While looping, a light green area is displayed in the Ruler over the
tracks to show the loop range.

By default, looping is bound to the [l]{.kbd} key.
