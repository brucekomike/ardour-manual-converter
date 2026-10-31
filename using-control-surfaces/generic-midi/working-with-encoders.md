# Generic MIDI and Encoders
Encoders are showing up more frequently on controllers. However, they
use the same MIDI events as Continuous Controllers and they have no
standard way of sending that information as MIDI events.

Encoders that send the same continuous values as a pot would are not
discussed here as they are already supported by `ctl`.

Encoders as this page talks about them send direction and offset that
the DAW will add to or subtract from the current value.

The 4 kinds of 7 bit encoders supported are:

- enc-r: Relative Signed Bit. If the most sign bit is set, Then the
  offset is positive. The lower 6 significant bits are the offset.
  `<Binding channel="1" enc-r="13" …` The offset value is formed as
  `0svvvvvv`. Where s is the sign or direction and vvvvvv is the number
  of ticks turned.
- enc-l: Relative Signed Bit 2\". If the most sign bit is unset, Then
  the offset is positive. The lower 6 significant bits are the offset.
  This is the same as enc-r but with the direction of turn reversed.
  This is the method the Mackie Control Protocol uses.
  `<Binding channel="1" enc-l="13" …` The offset value is formed as
  `0svvvvvv`. Where s is the sign or direction and vvvvvv is the number
  of ticks turned.
- enc-2: Relative 2s Complement. Positive offsets are sent as normal
  from 1 to 64 and negative offsets are sent as 2s complement negative
  numbers. This is a signed 7 bit int.
  `<Binding channel="1" enc-2="13" …`
- enc-b: Relative Binary Offset. Positive offsets are sent as offset
  plus 64 and negative offsets are sent as 64 minus offset. 64 is zero,
  65 is +1, 63 is -1. `<Binding channel="1" enc-b="13" …`

If the wrong one is chosen, either the positive or negative side will
act incorrectly. It is not really possible to auto detect which one the
controller is using. Trial and error is the only way if the
specification of the controller is not known.

Many controllers have more than one choice as well, check the manual for
the surface.

14 bit encoders are also supported with:

- rpn-delta - The value is expected to be a signed 14bit value that is
  added to the current value. For use with encoders
- nrpn-delta - The value is expected to be a signed 14bit value that is
  added to the current value. For use with encoders
