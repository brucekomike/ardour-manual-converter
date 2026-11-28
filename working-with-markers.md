# Markers Basics
Ardour supports multiple types of markers, all designed for particular
tasks: single markers that define a location, single markers that change
a value, paired markers that define a range on a timeline etc.

## Creating New Markers

There are several ways to create markers in Ardour.

The most common way is to right-click over a ruler and select a menu
item called like [Add \> Loop Range]{.kbd .menu} (for the [Range
Markers]{.kbd .title} ruler) or [Add New Tempo]{.kbd .menu} (for the
[Tempo]{.kbd .title} ruler).

![Adding a New Range
Marker](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/new-range-markers.gif){style="width:50%;"}

Some of the markers can be created from context menus on the canvas.
E.g. range markers can be created by creating a range, opening the
context (right-click) menu and choosing [Add Range Markers]{.kbd .menu}.

Additionally, location markers and range markers can be created from the
[Ranges & Marks]{.kbd .title} sidebar by clicking [Ranges & Marks]{.kbd
.title} or [Ranges & Marks]{.kbd .title} respectively.

## Moving Markers

Once a single or a paired marker has been added, it can be moved around.

### Single marker
{#moving-single-marker}

[Left]{.kbd .mouse}-clicking and dragging moves a single marker to a new
location on the timeline.

Additionally, markers can be moved to playhead position by
right-clicking and choosing the [Move Mark to Playhead]{.kbd .menu} menu
item.

### Multiple markers
{#moving-multiple-marker}

It is possible to move multiple markers by the same distance.
[Left]{.kbd .mouse .mod1}-clicking each discrete marker, or [Left]{.kbd
.mouse .mod3}-clicking the first and last markers of a range of markers
selects them, then dragging one to a new location will move all selected
markers together.

The markers are bounded by the zero point on the timeline. In other
words, the first marker in the selection cannot move to the left of zero
on the timeline.

### Both ends of a range marker
{#moving-entire-range-marker}

By [left]{.kbd .mod1 .mouse}-dragging either end of the range marker,
the other end will move by the same distance.

## Renaming Markers

Some markers on the ruler can have unique names: location markers, CD
markers, range markers. Double-clicking on them opens a dialog where a
different name can be submitted.

![Renaming a Marker](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/renaming-a-marker.gif){.hdimage}

Alternatively, right-clicking on a marker will open a context menu with
a menu item called [Rename\...]{.kbd .title} or [Rename Range\...]{.kbd
.title}, depending on the type of the marker. The same dialog for
submitting a new name will appear.

## Editing Marker\'s Properties
{#editing-marker-properties}

Markers on rulers such as [Time Signature]{.kbd .title} or [Tempo]{.kbd
.title} don\'t have unique names, however they do have other properties
that can be edited. The principle is the same as with renaming:
double-clicking on a marker or right-clicking and choosing the
[Edit\...]{.kbd .title} menu item.

## Hiding Markers

Most marker types can be temporarily hidden from the ruler if the user
chooses to do so. The user interface for that is available in the
[Ranges & Marks]{.kbd .title} sidebar: it is a simple [Hide]{.kbd
.title} checkbox for each marker.

![Hiding Markers](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/regions-and-marks.png){.hdimage}

Clicking the respective [Hide]{.kbd .title} checkbox again will reveal
the marker on the ruler again.

## Removing Markers

There are three ways to permanently delete a marker. The first one is to
right-click the marker of choice, then select [Remove]{.kbd .menu} in
the menu.

![Removing a Location Marker](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/remove-a-marker.png){.hdimage}

The second one is to click a marker to select it, keep hovering the
mouse pointer, then press [Del]{.kbd .key}.

The third way is to click the markers\' [x]{.kbd .button} button in the
*Ranges & Marks* sidebar.

## Controlling markers visibility

Right-clicking on the ruler displays two submenus: [Show Locations]{.kbd
.menu} and [Show Ranges]{.kbd .menu}. You can select to display all
types of location or range markers, or just one particular type.

## Additional Actions
{#additional actions}

Depending on the type of a marker additional actions are possible, such
as moving the playhead to a location marker\'s position or zooming to a
range saved with range markers. This is covered in dedicated subchapters
for respective ruler/marker types.
