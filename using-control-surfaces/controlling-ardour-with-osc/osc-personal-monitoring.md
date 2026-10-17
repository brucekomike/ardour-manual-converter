# Personal Monitoring Control
Personal monitoring can allow a performer with a smart phone to set
their personal monitor mix for a floor wedge or in-ear monitoring. In
Ardour 5.6 OSC commands to allow this were added for use with aux buses.
Ardour 6.0 added Foldback buses for this purpose and these commands work
directly for those.

### Setup

Foldback buses can be added from the GUI (see: [Foldback
section](@@foldback-strip)) or using the [/cue/new_bus]{.kbd .osc} OSC
command.

-   Create a bus for each performer who will have personal monitoring. A
    good practice is to name the bus with the performers name.
-   Connect the output of that bus to one of the audio interface\'s
    playback ports that is not otherwise used.
-   Add a foldback send to each channel the performer needs to hear in
    their personal mix. Many performers only need three or four sources
    to be mixed. If the performer needs to hear a a set of inputs that
    are combined into a bus, adding the foldback send to that bus may
    make more sense than adding ten drum channels for example.
-   If the performer wishes to hear effects in their monitor, an extra
    send from the effects bus or a plugin can be added in line in the
    foldback bus itself. Foldback sends are always just before the
    Fader.

This gives stage or studio monitoring for the performer.

### The OSC commands and feedback for personal monitoring

All of the personal monitoring commands and feedback start with a
*/cue*. It is expected that a surface used as a personal monitor control
will use only */cue* commands.

There is one OSC command apart from the `/cue` commands:
[`/select/add_fldbck_send`](#select-fldbck)

Most phone OSC applets (TouchOSC, Control) require manual port to be
set. There are certainly more controls than needed. Using send enables
for example, may lead to wasted time discovering why a send has no
sound. A good easy to use controller that fits on most phones while
still being controllable even with big fingers might look like:

```{eval-rst}
+-----------------------------------+-----------------------------------+
| <figure>                          | <figure>                          |
| <img                              | <img                              |
| s                                 | src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/osc-cue-control.jpg" |
| rc="/images/osc-cue-touchosc.jpg" | alt="Control Screenshot" />       |
| alt="TouchOSC Screenshot" />      | <figcaption>Personal Monitor      |
| <figcaption>Personal Monitor      | controller using                  |
| controller using                  | Control</figcaption>              |
| TouchOSC</figcaption>             | </figure>                         |
| </figure>                         |                                   |
+-----------------------------------+-----------------------------------+
```

Ardour is not limited to talking to one personal monitor controller at a
time, but is able to deal with many simultaneously, each controlling its
own foldback bus.

The send controls and feedback all have the send id (1 to n) in line as
part of the OSC path. So the path for the second send would be
*/cue/send/fader/2* to set the level. It is considered that most
surfaces used for this will only be able to handle one parameter.

#### Commands

[/cue/connect]{.kbd .osc}

Returns a list of foldback busses and connects to the first.

[/cue/bus *index*]{.kbd .osc}

where *index* is an integer or float which is the foldback bus number
this surface will use.

[/cue/next_bus]{.kbd .osc}

Sets the the foldback bus to one bus higher.

[/cue/previous_bus]{.kbd .osc}

Sets the foldback bus to one bus lower. This can also be used as a
\"connect\" button to save space in a phone layout.

[/cue/connect_output *output*]{.kbd .osc}

where *output* is a string that is the name of an output port or the
number of the output port if the port is a system:playback port to
connect the foldback bus to.

[/cue/new_bus *name* *l-output* *r-output*]{.kbd .osc}

where *name* is the name for the new foldback bus as a string,
*l-output* (optional) is the name of the output port to connect to. And
*r-output* (if present) will make the new foldback bus stereo and
connect the right output port to the named port. All parameters are
string type.

[/cue/new_send *strip*]{.kbd .osc}

where *strip* is a string with the name of the strip to add a foldback
send to that sends to the current foldback bus.

[/cue/fader *position*]{.kbd .osc}

where *position* is a float for the position of the fader between 0.0
and 1.0.

[/cue/mute *state*]{.kbd .osc}

where *state* is a float of 0.0 for mute off and 1.0 for the foldback
bus mute on.

[/cue/send/fader/*id* *position*]{.kbd .osc}

where *position* is a float for the position of the send fader between
0.0 and 1.0.

[/cue/send/enable/*id* *state*]{.kbd .osc}

where *state* is a float of 0.0 for disable and 1.0 for enable.

#### Feedback

|                                              |                                                                                                                   |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [/cue/name *name*]{.kbd .osc}                | where *name* is a string that is the name of the currently selected foldback bus.                                 |
| [/cue/name/*id* *name*]{.kbd .osc}           | where *name* is a string that is the name of the foldback bus that *id* belongs to.                               |
| [/cue/fader *position*]{.kbd .osc}           | where *position* is a float from 0.0 to 1.0 that shows the fader position for the selected foldback bus.          |
| [/cue/mute *state*]{.kbd .osc}               | where *state* is a float of 0.0 or 1.0 that shows the state of the mute for the selected foldback bus.            |
| [/cue/signal *activity*]{.kbd .osc}          | where *activity* is a float of 0.0 or 1.0 that shows audio activity for the selected foldback bus.                |
| [/cue/send/name/*id* *name*]{.kbd .osc}      | where *name* is a string that is the name of the channel that send *id* belongs to.                               |
| [/cue/send/fader/*id* *position*]{.kbd .osc} | where *position* is a float from 0.0 to 1.0 that is the position for the fader for the send that *id* belongs to. |
| [/cue/send/enable/*id* *state*]{.kbd .osc}   | where *state* is a float of 0.0 or 1.0 that is the state of the enable for the send that *id* belongs to.         |

While a fader is being adjusted, the corresponding */\*/name* text will
give the level in db.

## Setting up a Foldback bus from a selected strip
{#select-fldbck}

A selected or expanded strip can create a foldback send and create a
foldback bus at the same time using: [/select/add_fldbck_send
*name*]{.kbd .osc} where *name* is a string with the name of the desired
foldback bus. If the name matches an existing foldback bus the new send
will be added to the selected or expanded strip that feeds that bus. If
there is no strip of that name, one will be created.
