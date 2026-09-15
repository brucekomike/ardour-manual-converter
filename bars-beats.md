# Bars:Beats
[BBT markers]{.dfn} allow resetting the timeline to a particular bar and
beat. Most of the time a BBT marker will reset it to 1\|1\|0 (the very
first beat of the very first bar) so that for each song in a multi-song
session there would be a musical time origin. However it\'s entirely
possible to reset to an arbitrary value such as 7\|3\|0.

To create a new BBT marker, []{.kbd .mod1n}-click on the Bars:Beats
ruler. This will open a dialog titled [New Music Time]{.kbd .window}
where you can name the marker and define what bar (left field) and beat
(right field) this marker should reset the time to.

![New Music Time dialog](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/new-music-time.png){.hdimage}

The timeline grid and the ruler will be updated accordingly:

![The BBT marker resets the musical
time](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/bbt-marker-resets-musical-time.png){.hdimage}

Dragging a BBT marker right or left will reset the musical time at a
different position on the timeline.

Right-clicking on a BBT marker opens a menu with two options:
[Edit...]{.kbd .menu} and [Remove]{.kbd .menu}.

Choosing [Edit...]{.kbd .menu} opens the [Edit Musical Time]{.kbd .menu}
dialog where it\'s possible to rename the marker and set a different bar
and/or beat to reset the musical time to:

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/edit-bbt-marker.png" class="hdimage"
alt="Edit Musical Time" />
<figcaption>The Edit Musical Time dialog</figcaption>
</figure>

Choosing [Remove]{.kbd .menu} deletes the marker.
