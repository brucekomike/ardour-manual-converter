# Which Regions Are Affected?
This section explains the rules used to decide which regions are
affected by editing operations. They don\'t really have to be
understood---hopefully things will Just Work---but it may be useful
eventually.

Editing operations in Ardour either operate on a single point in time
([Split]{.kbd .menu} being the obvious example) or on two points (which
can also be considered to be a range of sorts), [Separate]{.kbd .menu}
is a good example of this.

Most operations will operate on the currently selected region(s), but if
no regions are selected, the region that the mouse is in will be used
instead. Single-point operations will generally pick a set of regions to
use based on the following rules:

- If the [Edit Point](@@edit-point-control) is [mouse]{.kbd .menu}, then
  - if the mouse is over a selected region, or no region, use all
    selected regions, or
  - if the mouse is over an unselected region, use just that region.
- For all other Edit Points
  - use the selected regions *and* those that are both under the edit
    position *and* on a selected track, or on a track which is in the
    same active edit-enabled route group as a selected region.

The rationale here for the two different rules is that the mouse Edit
Point is special in that its position indicates both a time and a track;
the other edit points ([Playhead]{.kbd .menu},[Marker]{.kbd .menu})
indicate a time only.
