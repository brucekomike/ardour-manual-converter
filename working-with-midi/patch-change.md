# Patch Change
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/patch_change.png"
alt="A patch change in a MIDI region" />
<figcaption aria-hidden="true">A patch change in a MIDI
region</figcaption>
</figure>

A [Patch Change]{.dfn} is Ardour\'s description for a combination of
MIDI program change and bank select messages, that typically instruct a
synthesizer or sampler to select a sound to use on any given channel.
Patch changes are shown within MIDI regions as small rectangles or
[flags]{.dfn}, with a vertical line showing where in the region the
patch change will occur.

## Inserting Patch Changes

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/region-midi-r-click-menu.png"
alt="Region &gt; MIDI context menu" />
<figcaption>MIDI context menu</figcaption>
</figure>

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/patch-change-dlg.png" alt="Patch Change dialog" />
<figcaption aria-hidden="true">Patch Change dialog</figcaption>
</figure>

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/patch-r-click-menu.png"
alt="Patch Change context menu" />
<figcaption aria-hidden="true">Patch Change context menu</figcaption>
</figure>

A patch change is inserted by first ensuring that the mouse is in [Grab
Mode](@@toolbox), then [right]{.kbd .mouse}-clicking on the MIDI region
where the patch change is desired, then selecting [\<Region Name\> \>
MIDI \> Insert Patch Change\...]{.kbd .menu}. The desired patch is then
chosen from the dialog that appears.

Inserted patch changes always appear in the selected region at the [Edit
Point](@@edit-point-control).

## Modifying Patch Changes

A patch change can be modified in [Internal Edit Mode](@@toolbox) by
[right]{.kbd .mouse}-clicking on it, then selecting the desired patch
from the menu that appears. A patch change can also be modified by
hovering the mouse pointer over the patch change to be modified and
moving the mouse wheel until the desired program number is selected. The
bank number can be modified similarly by holding down the []{.kbd .mod3}
key while moving the mouse wheel until the desired bank is selected.

## Moving Patch Changes

A patch change can be moved, within the region in which it resides, by
[left]{.kbd .mouse}-clicking it and dragging it to the desired location.

## Removing Patch Changes

A patch change can be removed by holding down the []{.kbd .mod3} key and
then [right]{.kbd .mouse}-clicking on it.

## Names for Patch Numbers: MIDNAM files
{#midnam}

MIDNAM files assign human-readable names to the \"sound coordinates\"
(Program Change, Bank Select) of MIDI synthesizers and devices. A number
of MIDNAM files come bundled with Ardour; if the MIDNAM for a device is
not included with Ardour, [a custom MIDNAM file can be
created](@@midnam-ref) for device in question.

### Selecting a device

Selecting a MIDNAM is only possible if there is no MIDI synth on the
track in question or the MIDI synth does not have a MIDNAM associated
with it. In this case, it is possible to select the desired MIDNAM from
a combobox in the MIDI track\'s header, usually directly below the
track\'s fader. See [MIDI Track Controls](@@midi-track-controls) for
more details.
