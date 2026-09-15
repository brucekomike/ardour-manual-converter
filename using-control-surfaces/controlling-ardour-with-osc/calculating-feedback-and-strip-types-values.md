# Feedback and strip-types values
*/set_surface* has two values the user needs to calculate before use. In
general these will not be calculated at run time, but beforehand. There
may be more than one button with different values to turn various kinds
of feedback on or off or to determine which kinds of strips are
currently viewed/controlled.

Both *feedback* and *strip-types* use bitsets to keep track what they
are doing. Any number in a computer is made out of bits that are on or
off, but we represent them as normal base 10 numbers. Any one bit turned
on will add a unique value to the number as a whole. So for each kind of
feedback or strip type to be used, that number should be added to the
total.

## strip_types

strip_types is an integer made up of bits. The easy way to deal with
this is to think of strip_types items being worth a number and then
adding all those numbers together for a value to send. Strip Types will
determine What kind of strips will be included in bank. This would
include: Audio, MIDI, busses, VCAs, Master, Monitor and hidden or
selected strips.

-   1: AudioTracks.
-   2: MidiTracks.
-   4: AudioBusses.
-   8: MidiBusses.
-   16: VCAs.
-   32: Master.
-   64: Monitor.
-   128: FoldbackBusses.
-   256: Selected.
-   512: Hidden.
-   1024: Use Group.

Selected and Hidden bits are normally not needed as Ardour defaults to
showing Selected strips and not showing Hidden strips. The purpose of
these two flags is to allow showing only Selected strips or only Hidden
strips. Using Hidden with other flags will allow Hidden strips to show
inline with other strips.

Use Group on will tell ardour that any control on a strip that is part
of a group will affect all strips within that group. Default is off or
the control should only affect the strip the control is applied to. The
`/use_group f state` command can be used to temporarily change this on
the fly.

Some handy numbers to use might be: 15 (all tracks and busses - 1 + 2 +
4 + 8), 31 (add VCAs to that - 15 + 16). Master or Monitor strips are
generally not useful on a surface that has dedicated controls for these
strips as there are /master\* and /monitor\* commands already. However,
on a surface with just a bank of fader strips, adding master or monitor
would allow access to them within the banks. Selected would be useful
for working on a group or a set of user selected strips. Hidden shows
strips the GUI has hidden. As such, a control surface will likely have a
number of buttons with different strip_types for convenience.

-   Mixer - All strip types [/set_surface/strip_types 159]{.kbd .osc}
-   Audio Tracks - Just Audio tracks that can record
    [/set_surface/strip_types 1]{.kbd .osc}
-   MIDI Tracks - Tracks with at least 1 MIDI input that can record
    [/set_surface/strip_types 2]{.kbd .osc}
-   Busses - A mix of all busses, possibly including VCAs
    [/set_surface/strip_types 156]{.kbd .osc}
-   Selected - All strips that are currently selected
    [/set_surface/strip_types 256]{.kbd .osc}
-   Hidden - All hidden strips [/set_surface/strip_types 512]{.kbd .osc}
-   Custom - see [Making a user selected strip
    list.](@@osc58-custom-strips) [/strip/custom/mode 1]{.kbd .osc}

### Using hidden strips
{#hidden}

Ardour allows any of it\'s strips to be hidden so that they do not show
up on the GUI mixer or editor. OSC follows the GUI by default and will
not show hidden strips. As of Ardour 6.0 the OSC commands include
[/select/hide *y/n*]{.kbd .osc} for the selected strip and [/strip/hide
*ssid* *y/n*]{.kbd .osc} for any strip. This allows the control surface
to hide or unhide a strip. What may not be obvious is that hiding a
strip makes it disappear and become unselected. So if a selected strip
is hidden, it is no longer selected and the select channel will show the
default select strip (Master). In order to show a hidden strip, the
hidden strips need to be shown first using the [/set_surface/strip_types
512]{.kbd .osc} command to show only hidden strips. Then use the
[/strip/hide *SSID* 0]{.kbd .osc} or [/select/hide 0]{.kbd .osc} to show
that strip. Of course, because only hidden strips are showing, the strip
you have set to no long hide will seem to vanish. A
[/set_surface/strip_types 159]{.kbd .osc} will then show the default
strip types or replace the 159 with the desired strip_types.

When hiding more than one strip in a row, check the strip name before
hiding as the strips will move as each strip is hidden just as it does
with the GUI mixer. So to hide strips 5, 6 and 7, the hide button for
`ssid` 5 is pressed 3 times. A more intuitive method would be to hide
strips from right to left (7, 6 and 5) which will work as expected.

In short, shown strips can only be hidden when they are viewable and
hidden strip can only shown (or un-hid) when strip_types include hidden
strips.

## feedback

Feedback is an integer made up of bits. The easy way to deal with this
is to think of feedback items being worth a number and then adding all
those numbers together for a value to send.

-   1: Button status for strips.
-   2: Variable control values for strips.
-   4: Send SSID (or for \`/select/\*\` messages the send or plugin
    parameter id) as path extension.
-   8: heartbeat to surface.
-   16: Enable master section feedback.
-   32: Send Bar and Beat.
-   64: Send timecode.
-   128: Send meter as dB (-193 to +6) or 0 to 1 depending on gainmode
-   256: Send meter a 16 bit value where each bit is a level and all
    bits of lower level are on. For use in a LED strip. This will not
    work if the above option is turned on.
-   512: Send signal present, true if level is higher than -40dB
-   1024: Send position in samples
-   2048: Send position in time, hours, minutes, seconds and
    milliseconds
-   8192: Turn on select channel feedback
-   16384: Use OSC 1.0 /reply instead of #reply
-   32768: Report 8x8 Trigger Grid status
-   65536: Report Mixer Scene status

So using a value of 19 (1 + 2 + 16) would turn on feedback for strip and
master controls, but leave meters, timecode and bar/beat feedback off.
