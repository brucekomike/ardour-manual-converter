# Strip Silence from Audio Regions
![The Strip Silence window](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/strip-silence-window.png)

The [Strip Silence]{.dfn} tool allows to remove the parts of one or
multiple regions that are below a user-defined silence threshold. It
does *not* destroy the underlying audio, but trims the regions according
to the silence threshold parameter. The edit applies to all selected
regions, allowing batch processing.

The window, accessible either through the [Region \> Edit \> Strip
Silence]{.kbd .menu} menu or [[right]{.kbd .mouse} click on a region \>
*Name_Of_The_Region* \> Edit \> Strip Silence]{.kbd .menu}is made of:

|                        |                                                                                                                                                                                  |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Threshold]{.dfn}      | The audio level under which the audio is considered silent (in dBFS)                                                                                                             |
| [Minimum length]{.dfn} | A minimum number of samples for Ardour to create a split. Under this number, the region won\'t be sliced                                                                         |
| [Fade length]{.dfn}    | Ardour adds fades, both in and out, to the trimmed regions, to the created region (so the sliced regions are longer by both the in and out fades duration, expressed in samples) |
| A progress bar         | showing the time Ardour takes to compute the trimming based on the current parameters                                                                                            |

Changing any parameter in the window is reflected in the main editor:
the silent segments are highlighted and the number and durations of the
shortest segments is displayed, helping fine-tune the parameters.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/strip-silence-audio.png"
alt="strip silence: view of the audio" /> <img
src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/strip-silence-after.png"
alt="strip silence: view of the audio after" />
<figcaption>Strip Silence : a view of the audio while changing the
parameters, and after treatment</figcaption>
</figure>

The minimum length for silence can be useful when editing very
percussive material and just needing to automatically trim the ends of a
region.
