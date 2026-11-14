# Making Selections
Many editing operations in Ardour require to first [select one or more
regions]{.dfn} to change them in some way. A single region, or multiple
regions can be selected, including regions in different tracks. When a
region is selected, it will appear in a darker color than unselected
regions.

If a track is a member of a group that is active and has the
[Select]{.kbd .option} property enabled, then Ardour will attempt to
match whatever selections is made in one track across every other track
of the group. See [Corresponding Regions
Selection](@@corresponding-regions-selection) for more information on
precisely how selections will be propagated to other tracks.

## Track Selection

Tracks are [selected]{.dfn} by clicking on the Track header at the left
of the Editor window. Multiple tracks can be selected with [Left]{.kbd
.mod1 .mouse} clicks, or a range of consecutive tracks with [Left]{.kbd
.mod3 .mouse}.

## Region Selection

Using the [Grab Mode tool](@@toolbox), [left]{.kbd .mouse} clicking on a
region selects it. If [Smart mode](@@toolbox) is enabled, the lower half
of the region must be clicked.

## Deselecting a Region

Still using the [Grab Mode tool](@@toolbox), [Left]{.kbd .mouse
.mod1}-clicking the region deselects it. If [Smart mode](@@toolbox) is
enabled, the lower half of the region must be clicked.

Note that a [left]{.kbd .mouse .mod1} click simply toggles the selected
status of an object, so it can be used to select unselected regions too.

## Selecting Multiple Regions in a Track

This can be achieved in different ways:

- [Left]{.kbd .mouse .mod1}-clicking each region.
- Dragging a rubberband box from an empty point in a track before the
  first region to select to a point within or after the last region to
  select. Using [left]{.kbd .mouse .mod1}-drag allows doing it multiple
  times.
- If the regions are all adjacent to one another, clicking the first
  region to select, then [Left]{.kbd .mouse .mod3}-clicking the last
  one.

## Selecting All Regions in a Track

The [Select \> Select All In Track]{.kbd .menu} option in the context
menu ([Right]{.kbd .mouse} click on the track) selects all the regions
in the track at once.

See the [Track Context Menu](@@track-context-menu) for more information
on other per-track selection operations that are available.

## Selecting Multiple Regions Across Different Tracks

This can be achieved by a [left]{.kbd .mouse .mod1}-click or [Left]{.kbd
.mouse .mod3}-click on the regions to select.

## Selecting a Region From the Region List

Clicking the name of the region in the [Region List](@@the-region-list).
selects it. This will do nothing for whole-file regions, since they do
not exist anywhere in a playlist or track.
