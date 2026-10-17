# Zoom Controls
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/toolbar-zoom.png" alt="Editor toolbar&#39;s zoom" />
<figcaption aria-hidden="true">Editor toolbar's zoom</figcaption>
</figure>

The zoom controls allow to navigate the session along both the time and
track axes. The controls are described from right to left :

## Along the time axis
{#zoom-along-time-axis}

The drop down *Zoom Focus* ([Playhead]{.kbd .menu} by default) menu
allows to select a focus point for the zoom, i.e. the center of the
zoom, to choose amongst:

-   [Left]{.dfn} of the screen
-   [Right]{.dfn} of the screen
-   [Center]{.dfn} of the screen
-   [Playhead]{.dfn}
-   [Mouse]{.dfn}
-   [Edit Point]{.dfn} as set in the [Edit point](@@edit-point-control)
    control.

The two zoom buttons ([−]{.kbd .menu} and [+]{.kbd .menu}) use this zoom
focus to zoom out and in respectively.

The [\[ \]]{.kbd .menu} *Zoom to session* button is a handy shortcut to
zoom out or in until all the session (as defined by its [start/end
markers](@@working-with-markers)) fits horizontally.

## Along the tracks axis
{#zoom-along-track-axis}

Two buttons [Shrink tracks]{.kbd .menu} and [Expand tracks]{.kbd .menu}
reduce or expand the vertical size of the selected tracks. If no track
is selected, all the tracks will be shrunk or expanded each time the
button is pushed.

Last, the dropdown menu ([\*]{.kbd .menu} by default) allows changing
the number of visible tracks to fit vertically on screen.

There *is* a minimal track height to keep it visible, so according to
the vertical screen size, some high number can have no effect.

Besides numbers that correspond to the number of tracks to show, there
are two special choices:

-   [Selection]{.dfn} that focus on the selected tracks. If the selected
    tracks are not contiguous, the unselected tracks inbetween will be
    hidden, see the [Track and Bus list](@@the-tracks-and-busses-list).
-   [All]{.dfn} that fits all the tracks of the sessions vertically
    (provided there\'s enough screen estate).
