# Working With Regions
## What Regions Are

[Regions]{.dfn} are the basic elements of editing and composing in
Ardour. In most cases, a region represents a single contiguous section
of one or more media files. Regions are defined by a fixed set of
attributes:

- the audio or [MIDI]{.abbr
  title="Musical Instrument Digital Interface"} [source file(s)]{.dfn}
  they represent,
- an [offset]{.dfn} (the \"start point\") in the audio or MIDI file(s),
  and
- a [length]{.dfn}.

When placed into a playlist, they gain additional attributes:

- a [position]{.dfn} along the timeline, and
- a [layer]{.dfn}.

There are other attributes as well, but they do not *define* the region.
Things to know about regions:

Regions Are Cheap

By themselves, regions consume very little in terms of computer\'s
resources. Each region requires a small amount of memory, and represents
a rather small amount of CPU work if placed into an active track. So,
multiplying regions creation whenever needed should not be much of an
issue CPU wise.

Regions Are Not Files

Although a region can represent an entire audio file, they are never
equivalent to an audio file. Most regions represent just parts of an
audio file(s) on disk, and removing a region from a track has nothing to
do with removing the audio file(s) from the disk (the [Destroy]{.kbd
.menu} operation, one of Ardour\'s few destructive operations, can
affect this). Changing the length of a region has no effect on the audio
file(s) on disk. Splitting and copying regions does not alter the audio
file in any way, nor does it create new audio files (only
[recording]{.dfn}, and the [Export]{.kbd .menu}, [Bounce]{.kbd .menu}
and [Reverse]{.kbd .menu} operations create new audio files).

## Selecting regions

Pointing at a region and single-clicking it with the Grab tool selects
that region. Multiple regions can be selected at the same time:

- [Ctrl]{.kbd}-[left]{.kbd .mouse}-click adds individual regions to the
  selection.
- [Shift]{.kbd}-[left]{.kbd .mouse}-click adds consecutive regions to
  the selection, Ardour considers all regions of the same track to the
  right from the currently selected track as consecutive regions.

Selection of multiple regions is always temporary and is not preserved
once you click elsewhere or press [Esc]{.kbd}. To make such a selection
permanent, create a group of regions in one of the following ways:

- Press [Ctrl]{.kbd}+[G]{.kbd}
- Use [Region \> Group Selected Regions]{.kbd .menu} in the main menu
- Use [Selected Regions \> Group Selected Regions]{.kbd .menu} in the
  right-click menu.

To break a group of regions back into individual regions, do one of the
following things:

- Press [Shift]{.kbd}+[Ctrl]{.kbd}+[G]{.kbd}
- Use [Region \> Ungroup Selected Regions]{.kbd .menu} in the main menu
- Use [Selected Regions \> Ungroup Selected Regions]{.kbd .menu} in the
  right-click menu.

## Region Operations

Selecting a region with a single-click makes it possible to perform
various operations on it. These operations are mostly accessible from
the main [Region]{.kbd .menu} menu on top or from the right-click menu.

Some operations like editing fade in/out are accessible with just the
mouse pointer.
