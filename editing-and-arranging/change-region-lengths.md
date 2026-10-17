# Trimming Regions
Changing the [length]{.dfn} of a region is a very common editing
operation, often known as [trimming]{.dfn}. There are several ways to
accomplish this with Ardour, and some very useful specialized trimming
operations.

## Drag-Trimming With the Mouse

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/trimming-region-before.png"
alt="Trimming region - before" /> <img
src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/trimming-region-after.png" alt="Trimming region - after" />
<figcaption>Trimming region - before and after</figcaption>
</figure>

In Grab mode, moving the pointer near the beginning or end of the region
changes the cursor to indicate that trimming is possible, and the edge
of the region can then be [Left]{.kbd .mouse}-dragged in both
directions.

Trimming will obey [Snap settings](@@grid-controls).

## Other Trimming operations

There are several commands for region trimming. Some use the [edit
point](@@edit-point-control) to determine where to trim to. Some are not
bound to any keys by default (but could be via the [Keybindings
Editor](@@keyboard-shortcuts)).

These command are both in the [Region \> Trim]{.kbd .menu} main menu
(with a region selected) or in the context menu of a region, [
[right]{.kbd .mouse} click on a region \> *Name_Of_The_Region* \>
Trim]{.kbd .menu}

|                                              |                                                                                                                                                  |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [Trim Start at Edit Point]{.dfn} ([j]{.kbd}) | Trim selected region(s) start to edit point.                                                                                                     |
| [Trim End at Edit Point]{.dfn} ([k]{.kbd})   | Trim selected region(s) end to edit point.                                                                                                       |
| [Trim to Loop/Punch]{.dfn}                   | Trim selected region(s) beginning and end to the loop/punch boundaries (if it exists).                                                           |
| [Trim to Previous]{.dfn} ([j]{.kbd .mod1})   | Trim the start of selected region(s) to the end of the previous region. If the region is too short, it is extended to its maximum to the left.   |
| [Trim to Next]{.dfn} ([k]{.kbd .mod1})       | Trim the end of selected region(s) to the start of the following region. If the region is too short, it is extended to its maximum to the right. |
