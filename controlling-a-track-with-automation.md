# Controlling a Track with Automation
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/automation-menu1.png" height="211" />
<figcaption>The top-level automation menu</figcaption>
</figure>

A parameter on a given track can be automated by clicking on the
track\'s [A]{.kbd .menu} button and selecting a parameter to control
from the menu that appears. The same menu is displayed in the
[Automation]{.kbd .menu} submenu in track\'s [right]{.kbd .mouse}-click
menu.

Once a parameter has been selected, an automation lane for that
parameter will appear beneath the track. The lane thus shown will be
empty; from here an automation curve must be defined.

If the height of the automation lane is too small to see all of its
controls, the height can be increased by [left]{.kbd .mouse}-clicking on
the bottom border of the lane and dragging it down.

There are three ways to define an automation curve:

-   Recording it using [Write]{.kbd .menu} mode
-   Recording it using [Touch]{.kbd .menu} mode
-   Drawing it using the mouse

### Recording an Automation Curve Using Write Mode

To create an automation curve using [Write]{.kbd .menu} mode, first set
the lane\'s mode selector to [Write]{.kbd .menu}, then set the playhead
to the position where the automation curve should start, then set the
transport to play. While the playhead is moving, Ardour will
continuously record any changes made with the lane\'s fader. Even if no
changes are made to the fader, they will overwrite anything that existed
in the lane where the playhead is moving. When the desired automation
curve has been recorded, stop the transport.

After the transport is stopped, the lane\'s mode selector will
automatically switch to [Touch]{.kbd .menu} mode---it is generally a bad
idea to leave an automation lane in [Write]{.kbd .menu} mode, as it is a
destructive operation that makes it easy to inadvertently overwrite
existing automation curves.

### Recording an Automation Curve Using Touch Mode
{#track-automation-record-curve}

Creating an automation curve using [Touch]{.kbd .menu} mode is similar
to the method employed in creating one using [Write]{.kbd .menu} mode;
the only difference is that changes are written to the automation curve
*only* when the lane\'s fader is moved---at all other times, whatever
was in the automation curve will remain as it was.

[Touch]{.kbd .menu} mode is useful when only small parts of the
automation curve need touching up versus [Write]{.kbd .menu} mode, which
is usually used to create the automation curve in the first place.

### Drawing an Automation Curve Using the Mouse
{#track-automation-draw-curve}

In [[Draw]{.dfn} mode](@@toolbox), [control points]{.dfn} can be entered
in the automation lane in multiple ways.

-   By [left]{.kbd .mouse}-clicking in the lane at a point where there
    is no existing control point. Once added, a control point can be
    [left]{.kbd .mouse}-clicked and dragged to any desired location.
    Hovering over a control point will show its current value.
    **Warning:** creating a verbose automation with many control points
    can cause some plugins to overuse available system resources.
-   By [left]{.kbd .mouse}-clicking in the lane and drawing a free line
    from left to right.
-   By pressing [Ctrl]{.kbd}, then pressing [left]{.kbd .mouse} in the
    lane and moving the mouse pointer from left to right or from right
    to left to preview a line segment, then releasing the mouse button
    to complete the action.

It\'s possible to combine free and straight lines in one go by pressing
[Ctrl]{.kbd} for when you need a straight line and releasing the button
when you\'re done drawing a straight line segment.

## Controlling the Track
{#track-automation-controlling-track}

Once an automation curve has been defined through any of the methods
outlined above, the track won\'t do anything with it until the lane that
the curve was defined in is set to [Play]{.kbd .menu} mode. Then, during
playback, as the playhead moves through the automation curve, the
lane\'s control will move in accord with the curve.

The lane\'s fader will *not* be responsive to manual input while it is
in [Play]{.kbd .menu} mode.

## Removing Automation
{#track-automation-removing}

To remove a control point, [left]{.kbd .mouse}-click it and press
[Delete]{.kbd}, or []{.kbd .mod3n} [right]{.kbd .mouse}-click on it.

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/automation-audio-r-click-menu.png" />
<figcaption>The automation lane context menu.</figcaption>
</figure>

Clearing the entire automation lane is done by [right]{.kbd
.mouse}-clicking on the lane to be cleared, and selecting [Clear]{.kbd
.menu} from the menu that appears.
