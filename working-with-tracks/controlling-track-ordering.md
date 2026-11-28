# Track Ordering
Ardour does not impose any particular ordering of tracks and busses in
either the editor or mixer windows. The default arrangements are as
follows:

- In the [Editor]{.dfn} window, the Master bus will always be on top
  unless hidden. Tracks and busses will appear in their initial order,
  from top to bottom. The monitor section (if used) is never visible in
  the editor window.
- In the [Mixer]{.dfn} window, the tracks and busses will be displayed
  in their initial order, from left to right. The Master bus is always
  on the far right and occupies its own pane, so that it is always
  visible no matter how many other mixer strips are present. If a
  Monitor section is used, it shows up at the right edge of the mixer
  window; it can also be torn off into a separate window.

## Reordering Tracks

The [track ordering]{.dfn} of the Editor and Mixer is
[synchronized]{.dfn}: if a track is reordered in one window, the
ordering in the other window will follow.

### Reordering in the Editor Window

There are three ways to reorder tracks/busses in the Editor window:

- Selecting the tracks to be moved, then dragging them up or down with
  the mouse (available since Ardour 8.7).
- Selecting the tracks to be moved, then using [Track \> Move Selected
  Tracks Up]{.kbd .menu} (shortcut: [↑]{.kbd .mod1}) or [Track \> Move
  Selected Tracks Down]{.kbd .menu} (shortcut: [↓]{.kbd .mod1}).
- Selecting the tracks to be moved in the [[Tracks & Busses]{.kbd .menu}
  panel of the Editor Lists](@@the-tracks-and-busses-list) dock, then
  dragging them up or down.

### Reordering in the Mixer Window

Within the [Strips List](@@strips-list) pane at the top left of the
Mixer window, tracks and busses can be freely dragged-and-dropped into
any desired order.

### \"Collecting\" Group Members

Tracks and Busses that are members of a group can be reordered so that
they display contiguously within the Editor and Mixer windows, by
[Right]{.kbd .mouse}-clicking on the group tab and choosing
[Collect]{.kbd .menu}.

## Ordering of New Tracks

When [adding new tracks](@@adding-tracks-busses-and-vcas), the
[Insert:]{.kbd .menu} field allows to determine their placement. New
tracks will be placed *Last* by default, so after the rightmost (in the
mixer) or bottom-most (in the editor) selected track. If no tracks are
selected, new tracks will be added at the end, regardless of the choice.

Because new tracks are automatically selected, they can be quickly
reordered in the editor window via the keyboard shortcuts after adding
them.

## Track Ordering and Remote Control IDs

Every track and bus in Ardour is assigned a [remote control ID]{.dfn}.
When a [control surface](@@control-surfaces) or any other remote control
is used to control Ardour, these IDs are used to identify which track(s)
or buss(es) are the intended target of incoming commands.

Remote IDs are assigned to tracks and busses in the order that they
appear in the mixer window from left to right, starting from #1; manual
assignment of remote IDs is not possible. The master bus and monitor
section can be accessed by name.
