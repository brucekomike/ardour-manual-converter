# Track Layering
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/track-layer-dialog.png"
alt="The Track layering menu" />
<figcaption aria-hidden="true">The Track layering menu</figcaption>
</figure>

Ardour allows arbitrary [layering]{.dfn} of regions---there can any
number of regions at a given position. By default, the regions are
[overlaid]{.dfn} in the editor window, to save vertical space.

However, this display mode can be confusing for tracks with many
overdubs, because its not obvious in which order the overdubs are
layered. Although there are other methods of moving particular regions
to the top of an overlapping set, and although Ardour also has playlists
to manage [takes](@@playlist-usecases) a bit more efficiently than just
continually layering, there are times when being able to clearly see all
regions in a track without any overlaps is reassuring and useful.

The example below shows a track with a rather drastic overdub situation,
viewed in normal [overlaid mode]{.dfn}:

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/overlaps_layered.png"
alt="Overlapping regions in overlaid mode" />
<figcaption aria-hidden="true">Overlapping regions in <em>overlaid</em>
mode</figcaption>
</figure>

This display can be changed by [right]{.kbd .mouse} clicking on the
track header, showing the menu displayed above. There are two choices
for layers, and [overlaid]{.kbd .menu} is currently selected. Clicking
on [stacked]{.kbd .menu}, the track display changes to:

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/layers_stacked.png"
alt="Overlapping regions in stacked mode" />
<figcaption aria-hidden="true">Overlapping regions in <em>stacked</em>
mode</figcaption>
</figure>

Regions can still be moved around as usual, and can be dragged so that
they overlay each other again, but when the mouse button is released,
things will flip back to them all being stacked cleanly. The number of
[lanes]{.dfn} for the track is determined by the maximum number of
regions existing in any one spot throughout the track, so if a track has
10 overdubs stacked up in one spot, it will end up with 10 lanes.
Obviously, using a large track height works much better for this than a
small one.
