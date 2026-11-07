# The Ranges and Marks Lists
The [Ranges & Marks List]{.dfn} is a tab in the [Editor Lists]{.dfn}
area on the right of the Editor window. If the editor list area isn\'t
visible it can be enabled by checking [View \> Show Editor List]{.kbd
.option}. The Ranges & Marks list can be used as a single point of
control for all range and location markers (including the punch and loop
ranges), or as a supplement to other methods of working with them.

## Common elements

Each section has a set of [editable [clock
widgets](@@editing-clocks)]{.dfn} which display the location of a
marker, or the start, end, and duration times of a range, respectively.

The [Use PH]{.kbd .menu} buttons allows to set the corresponding clock
to the current playhead position. A [Middle]{.kbd .mouse} click on any
of the clocks will move the playhead to that location. Both functions
are also available from the clock context menus.

Right clicking on any of the clocks brings up a context menu that allows
changing of the display between Timecode, Bars:Beats, Minutes:Seconds,
and Samples.

The [---]{.kbd .menu} (subtract) button in front of each user-defined
range or marker in the list allows that particular item to be removed.
The name fields of custom ranges and markers can be edited.

The [Hide]{.kbd .option} checkboxes make markers and ranges invisible on
the respective ruler to reduce visual clutter; the markers remain active
however, and can be used normally.

Selecting [Lock]{.kbd .option} prevents the respective marker from being
moved until unlocked. Where applicable, [Glue]{.kbd .option} fixes the
marker position relative to the current musical position expressed in
bars and beats, rather than the absolute time. This will make the
respective marker follow changes in the tempo map.

At the bottom of the list are buttons to add new markers or ranges.

## List sections

|  |  |
|----|----|
| Loop/Punch Ranges | This list shows the current [loop]{.dfn} and [punch]{.dfn} range settings. Since these are built-in ranges, they cannot be renamed or removed. |
| Markers (Including CD Index) | This section lists the session\'s [markers]{.dfn}. By ticking [CD]{.kbd .option}, Ardour is instructed to create a [CD track index]{.dfn} from this marker, which will be included in the TOC or CUE file when exporting. |
| Ranges (Including CD Track Ranges) | This is the list of [ranges]{.dfn} (including [CD track ranges]{.dfn}). Ticking [CD]{.kbd .option} will convert the range to a [CD track]{.dfn}, which will again be included in exported TOC or CUE files. This is relevant for Disk-At-Once recordings that may contain audio data between tracks. |
