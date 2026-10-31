# Quick groups
Having a persistent group of tracks and/or busses has a number of pros,
such as being able to control faders of multiple tracks at once, at any
moment in time. However, Ardour also supports \"quick\" temporary
groups.

Selecting multiple tracks or busses either in the Editor or in the Mixer
window allows treating those tracks and/or busses as a group as long as
the tracks/busses are selected. This means:

- Adjusting fader position in one track/bus will change faders\'
  positions of other selected tracks/busses by the same amount. The same
  applies to input trim changes.
- Toggling Solo, Mute, Rec-enable, Solo Safe, Solo Isolate, Monitoring
  controls in one track/bus will toggle the same type of control in
  other selected tracks/busses.

If one of the selected tracks/busses belongs to a persistent group,
selecting it will automatically all the other members of that persistent
group and affect respective controls there as well. This can be worked
around by opening group\'s setting and changing what controls are shared
in the group.

There are two cases where quick groups will not work as expected:

1.  When a change to a control in a selected track/bus comes from a
    hardware control surface.
2.  When you use the mouse scroll wheel to adjust faders (this is a
    temporary limitation).
