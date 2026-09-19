# Editing Clocks
## Clock Modes

Every clock in Ardour has multiple different, selectable [clock
modes]{.dfn}. Each mode displays time using different units. The clock
mode can be changed by [Right]{.kbd .mouse}-clicking on the clock and
selecting the desired mode from the menu. Some clocks are entirely
independent of any other clock\'s mode; others are linked so that
changing one changes all clocks in that group. The different modes are:

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Timecode        | Time is shown as [SMPTE timecode]{.dfn} in Hours:Minutes:Seconds:Frames, measured from the timecode zero point on the timeline (which may not correspond to the session start and/or absolute zero on the timeline, depending on configurable timecode offsets). The frames value is dictated by either the Timecode frames-per-second [session property](@@session-properties#properties-timecode), or, if slaved to an external timecode master, the master\'s setting. Under the transport clocks is an indication of the current timecode source (`INT`{.sample} means that Ardour is its own timecode source). |
| Bars:Beats      | Time is shown as Bars:Beats:Ticks, indicating [musical time]{.dfn}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Minutes:Seconds | Time is shown as Hours:Minutes:Seconds.Milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Seconds         | Time is shown as Seconds.Deciseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Samples         | Time is shown as a [sample count]{.dfn}. The number of samples per second is given by the current sample rate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Changing clock values with the keyboard

New values for the clock can be typed in after clicking on the relevant
clock. Clicking on the clock will show a thin vertical cursor bar just
to the right of the next character to be overwritten. Time should be
typed in the same order as the current clock mode---if the clock is in
Timecode mode, it should be hours, minutes, seconds, frames. So, to
change to a time of 12:15:20:15 one would type
[1]{.kbd}[2]{.kbd}[1]{.kbd}[5]{.kbd}[2]{.kbd}
[0]{.kbd}[1]{.kbd}[5]{.kbd}. Freshly typed numbers will appear in a
different color, from right to left, overwriting the existing value.
Mid-edit, after typing [3]{.kbd}[2]{.kbd}[2]{.kbd}[2]{.kbd} the clock
might look like this:

![A clock being edited in Ardour](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/clockedit.png)

Finishing the edit is done by pressing [ENTER]{.kbd} or [Tab]{.kbd}. The
[ESC]{.kbd} key allows to exit an edit without changing the clock. If an
entry is mis-typed so that the new value would be illegal (for example,
resulting in more than 30 frames when Timecode is set to 30 frames per
second), the clock will reset at the end of the edit, and move the
cursor back to the start to allow for another try.

## Avoiding the mouse entirely

There is a shortcut available to edit the transport clocks entirely
without the mouse. It can be found in the [Keyboard
Shortcuts](@@keyboard-shortcuts) window, [Global \> Transport \> Focus
On Clock]{.kbd .menu}. If bound to a key ([/]{.kbd} by default), then
pressing that key is equivalent to clicking on the primary (left)
transport clock, and editing can begin immediately.

## Entering Partial Times

One detail of the editing design that is not immediately obvious is that
it is possible to enter part of a full time value.

As an example, supposing that the clock is in Bars:Beat mode, displaying
`024|03|0029`{.sample}, altering the value to the first beat of the
current bar can be done by clicking on the clock and typing
[0]{.kbd}[1]{.kbd}[0]{.kbd}[0]{.kbd}[0]{.kbd}[0]{.kbd}. Similarly, if it
is in Minutes:Seconds mode, displaying `02:03:04.456`{.sample}, getting
to exactly 2 hours can be achieved by clicking on the clock and typing
[0]{.kbd}[0]{.kbd}[0]{.kbd}[0]{.kbd}[0]{.kbd}[0]{.kbd}[0]{.kbd} to reset
the minutes, seconds and milliseconds fields.

## Entering Delta Times

Values can also be typed into the clock that are intended as a relative
change, rather than a new absolute value, by *ending* the edit by
pressing [+]{.kbd} or [-]{.kbd} (the ones on any keypad will also work).
The plus key will add the entered value to the current value of the
clock, minus will subtract it. For example, if the clock is in Samples
mode and displays `2917839`{.sample}, moving it back 2000 samples is
done by typing [2]{.kbd}[0]{.kbd}[0]{.kbd}[0]{.kbd} and [-]{.kbd},
rather than ending with [Enter]{.kbd} or [Tab]{.kbd}.

## Changing clock values with the mouse

### Using a scroll wheel

With the mouse pointer over the clock, moving the scroll wheel changes
the clock values. Moving the scroll wheel up ([⇑]{.kbd .mouse})
increases the value shown on the clock, moving it down ([⇓]{.kbd
.mouse}) decreases it. The step size is equal to the unit of the field
hovered over (seconds, hours, etc.).

### Dragging the mouse

With the mouse pointer over the clock, pressing the left mouse button
and dragging also affects the clocks: dragging upwards increases the
value shown on the clock, dragging downwards decreases it, again with a
step size equal to the unit of the field where the drag began on.
