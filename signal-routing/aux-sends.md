# Aux Sends
[Auxiliary sends]{.dfn} are simple [processors](@@processor-box) in a
bus or track channel strip. They tap the signal at a specific point in
the signal flow (pre-fader, post-fader, before or after EQs and other
plugins, etc.) and send a copy of that signal to a bus, without
affecting the normal signal flow downwards to the channel fader.

Aux sends from several tracks are collectively sent to a [bus]{.dfn} in
Ardour, to create a monitor mix for a musician, or to feed an effect
unit. A bus used in this way is considered an auxiliary bus or [Aux
bus]{.dfn} even though it is the same as any other bus. The output of
such a bus might be routed to separate hardware outputs (in the case of
headphone or monitor wedge mixes), or returned to the main mix (in the
case of an effect).

Aux sends do not show up outside of Ardour either on the audio device or
as JACK ports, [External Sends](@@external-sends) should be used to send
audio to the audio device or Jack ports. External Sends can send the
tapped signal somewhere else directly, which is not usually possible on
hardware mixers.

It may be useful to [compare and
contrast](@@comparing-aux-sends-and-subgroups) the use of aux sends with
[subgrouping](@@subgrouping).

## Adding a new aux bus

New busses can be created using the [Session \> Add Track, Bus or
VCA...]{.kbd .menu} menu, and selecting [Audio Busses]{.kbd .menu} in
the Template/Type selector on the left of the [Add Track/Bus/VCA]{.kbd
.menu} dialog.

## Adding a send to an aux bus

Context-clicking on the processor box for the track to send to the bus,
and choosing [New Aux Send ...]{.kbd .menu} shows a submenu, listing the
busses. Choosing one bus will add a send (which will be visible in the
processor box). Note that if the only existing bus is the Master Bus,
the menu will be grayed out.

### Pre-fader and Post-fader Aux Sends

Depending on whether the context-click happened above or below the fader
in the processor box, the new aux send can be placed before or after the
fader in the channel strip.

- [Post-fader]{.dfn} aux sends are typically used when using an aux for
  shared signal processing (FX), so that the amount of effect is always
  proportional to the main mix fader.
- [Pre-fader]{.dfn} sends ensure that the level sent to the bus is
  controlled *only* by the send, not the main fader---this is typical
  when constructing headphone and monitor wedge mixes.

The color of the processor will reflect this pre/post position (red for
[Pre]{.for-red}, green for [Post]{.for-green}). Dragging and dropping
the send inside the processor box before or after the Fader processor
changes the type of fader accordingly.

## Adding a new aux bus and sending a Track Group to it

All members of a group can be sent to a new aux bus at once with a
single click. After creating the [track group](@@track-and-bus-groups)
(and adding tracks to it), context-clicking on the group tab allows to
choose either [Add New Aux Bus (pre-fader)]{.kbd .menu} or [Add New Aux
Bus (post-fader)]{.kbd .menu}. A new aux bus will be created, and a new
aux send added to every member of the track group that connects to this
aux bus.

## Altering Send Levels

The amount of the signal received by a send that it delivers to the bus
it connects to can be altered in two ways:

### Using the Send Fader

Every send processor has a small horizontal fader that can be adjusted
in the usual way. It is not very big and so this can be a little
unsatisfactory if a very fine control over the send level is required.

### Map Aux Sends To Main Faders

In Mixer mode, pressing the button marked [Show Sends]{.kbd .menu} on a
aux bus will alter the channel strip for every track or bus that feeds
the aux bus. Many aspects of the strip will become insensitive and/or
change their visual appearance. More importantly, the main fader of the
affected channel strips will now control the send level and **not** the
track gain. This gives a larger, more configurable control to alter the
level. Clicking the [Show Sends]{.kbd .menu} button of the aux bus again
reverts the channel strips to their normal use.

## Disabling Sends

Clicking on the small LED in the send display in the processor box of
the channel strip will enable/disable the send. When disabled, only
silence will be delivered to the aux bus by this track. When enabled,
the signal arriving at the send will be delivered to the aux bus.

## Send Panning

Send panners can be configured to either be independent of the main
panner, or to follow it. The latter could be useful for Reverb effects,
or for in-ear monitor mixes delivered in stereo.
