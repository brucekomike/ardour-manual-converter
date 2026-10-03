# Track Modes
Audio tracks in Ardour have a [mode]{.dfn} which affects how they behave
when recording:

|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Layered        | Tracks in [layered mode]{.dfn} will record non-destructively --- new data is written to new files, and when overdubbing, new regions will be layered on top of existing ones. This is the recommended mode for most workflows. When recording with the [layered mode]{.dfn}, Ardour only does input monitoring.                                                                                                                                                                                                                        |
| Non-Layered    | Tracks using [non-layered mode]{.dfn} will record non-destructively---new data is written to new files, but when overdubbing, the existing regions are trimmed so that there are no overlaps. This does not affect the previously recorded audio data, and trimmed regions can be expanded again at will. Non-layered mode can be very useful for spoken word material, especially in combination with [push/pull trimming](@@pushpull-trimming). When recording with the [non-layered mode]{.dfn}, Ardour only does input monitoring. |
| Sound on Sound | Tracks using [Sound on Sound mode]{.dfn} will record non-destructively --- new data is written to new files, but when overdubbing, new regions will be layered on top of existing ones in non-opaque mode which means both existing and new material will be played back after the recording is over. This is convenient for a variety of use cases, such as adding MIDI Control Change events on top of recorded live performance. When recording in the [sound-on-sound mode]{.dfn}, Ardour does cue monitoring.                     |

Results of recording in layered and non-layered modes are visually the
same. However, with the sound-on-sound mode lower layers are visible
under upper layers, because in that case new regions with overdubs are
created with disabled *Opaque* setting.

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/region-layering-modes-overlaid.png"
style="width:75.0%"
alt="Layered, non-layered, and sound-on-sound modes" />
<figcaption>Layered, non-layered, and sound-on-sound modes in overlaid
view</figcaption>
</figure>

To illustrate the difference, here is the screenshot of the same tracks,
but this time --- in *Stacked* track mode (rather than *Overlaid* as on
the screenshot above).

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/region-layering-modes-stacked.png" style="width:75.0%"
alt="Layered, non-layered, and sound-on-sound modes in stacked view" />
<figcaption aria-hidden="true">Layered, non-layered, and sound-on-sound
modes in stacked view</figcaption>
</figure>

The overdub is an opaque region on top of the original content for the
*Layered* mode. For the *Non-Layered* mode, it completely replaces the
matching part of the original content. And for the *Sound on Sound*
mode, it\'s a transparent region on top of the original content.

The switch between layered, non-layered, and sound-on-sound modes is a
global setting available in the main toolbar right below the buttons
enabling Punch In and Punch Out.

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/layering-switch.png" class="hdimage"
alt="Layering switch" />
<figcaption aria-hidden="true">Layering switch</figcaption>
</figure>
