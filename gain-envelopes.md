# Gain Envelopes
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/gain-envelope1.png" alt="Default gain envelope" />
<figcaption>A gain envelope (in green).</figcaption>
</figure>

In Ardour, every audio [region]{.dfn} has a [gain envelope]{.dfn}. It is
a form of automated gain change that is embedded in the region. The gain
envelope remains associated with the region when it is moved or copied.

Region Gain envelope is only visible in the Draw and Edit modes.
Clicking on the Draw tool will cause all the gain envelopes on all
regions to show themselves. These will appear as lines with square dots
([control points]{.dfn}) at the beginning and end of each region. The
vertical axis represents gain, with the top of the region representing
`+6dB` and the bottom representing `-inf dB` (silence). By default, the
line starts and ends at `0dB`; the control points can be moved up and
down to change the amount of gain at that point.

Gain follows the line between control points continuously and accurately
during playback, and adjusts the gain for that region accordingly.
Unlike fader gain [automation](@@automation), region-gain is not
smoothed to prevent zipper-noise or amplitude modulation.

## Manipulating Gain Envelopes
{#manipulating-gain-envelopes style="clear: both"}

The default envelope is neutral (`0dB`) and disabled (gray line).
Changing the gain by dragging any of the two existing points or adding
new points in draw mode automatically enables the envelope. Clicking
anywhere in the region where there are no existing control points adds a
control point to the envelope; it will appear *on the line* at the
X-axis of the mouse\'s current position in the region.

Region gain envelope can be disabed for selected regions via [Region \>
Gain \> Envelope Active]{.kbd .menu}.

<figure class="center">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/gain-envelope2.png" alt="Complex gain envelope" />
<figcaption>A more complex gain envelope.</figcaption>
</figure>

Once added, a control point can be [Left]{.kbd .mouse} clicked and
dragged to the desired location. Hovering over a control point will show
its current level in dB. [Left]{.kbd .mouse} clicking a control point
and pressing [Delete]{.kbd}, or [Right]{.kbd .mod3 .mouse} clicking a
control point deletes it.
