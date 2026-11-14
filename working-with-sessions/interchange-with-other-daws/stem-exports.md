# Stem Exports
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/export-dialog-stem-export.png" width="500"
alt="Stem export" />
<figcaption>The Stem Export dialog</figcaption>
</figure>

[Stem exporting]{.dfn} allows to transfer files between different
systems and programs by exporting each track individually, including
silence, to keep them in sync. All data will be lost except the actual
audio/MIDI. This is one of the most common methods of interchange
because it works between all DAWs.

The [Stem Export]{.kbd .window} window, accessed via the [Session \>
Export \> Stem Export...]{.kbd .menu} menu, is very similar to the
[Export dialog](@@export-dialog), except the \'Channels\' tab appears
slightly differently: in this case each chosen channel (track or bus) is
exported to its own file, instead of all channels being mixed together
into a single file.

The exported tracks or busses can, by checking [Apply track/bus
processing]{.kbd .option}, be exported with the effects/processors
applied, so that the destination system does not need those effects
plugins.

The toolbar in the Stem Export window also provides a quick way to
select either audio or MIDI tracks or busses.
