# Generic MIDI Binding Maps
Ardour 2.X supported [[MIDI learning]{.dfn}](@@generic-midi-learn) for
more or less any control. This was a nice feature that quite a few other
DAWs are providing by now, but it didn\'t allow Ardour to work \"out of
the box\" with sensible defaults for existing commercial MIDI
controllers. In Ardour 3 and later versions, we have augmented the MIDI
learn feature with the ability to load a [MIDI binding map]{.dfn} for a
given controller, which can set up an arbitrary number of physical
controls with anything inside Ardour that can be controlled.

As of this writing we offer presets for the following devices/modes:

-   AKAI MPD32
-   AKAI APC mini
-   AKAI APC mini mk2
-   AKAI MidiMix EQ Mode
-   AKAI MidiMix Normal Mode
-   AKAI MPK61
-   AKAI MPK 225 (Normal): preset 6
-   AKAI MPK 225 (Eq mode): preset 6
-   AKAI MPK249
-   AKAI MPK mini mk1
-   AKAI MPK mini mk3
-   AKAI MPK miniplus
-   Alesis Q49 MKII
-   Alesis QX25
-   Alesis VI25
-   Arturia KeyLab 49
-   Arturia Keylab 49/61/88 mk2 (MCU/Analog Lab mode)
-   Arturia MiniLab 3
-   Arturia MiniLab mk2
-   Behringer BCF2000 Factory Preset 2
-   Behringer BCF2000 Mackie Control
-   Behringer DDX3216
-   Devine VersaKey
-   Donner StarryPad
-   Donner DMK25 SpacLine
-   E-MU Xboard 61
-   Korg nanoKONTROL
-   Korg nanoKONTROL w/Master
-   Korg nanoKONTROL Studio
-   Korg nanoKONTROL2
-   Korg nanoKONTROL2 With Master
-   Korg Taktile (mode 9)
-   LAudio EASYCONTROL.9
-   M-Audio Axiom 25 - Transport Controls
-   M-Audio Axiom 49 MkII
-   M-Audio Axiom 61
-   M-Audio Axiom AIR Mini 32
-   M-Audio Axiom Air 25 (2015 Model) - Transport Controls
-   M-Audio Oxygen 49
-   M-Audio Oxygen 61 v3
-   M-Audio Oxygen25 (3rd Gen)
-   M-Audio Oxygen25 (factory default)
-   M-Audio Oxygen61 V3 by samtuke
-   M-Audio Oxygen8 V2
-   Nektar Impact GX
-   Nektar Impact LX
-   Nektar Panorama
-   Novation Impulse 49
-   Novation Impulse 61
-   Novation Launch Control XL
-   Novation LaunchKey 49
-   Novation Launchkey 25
-   Roland A-30
-   Roland SI-24
-   Roland V-Studio 20
-   WiiMote via midikb
-   Yamaha KX25 Transport Controls

At this time, new binding maps need to be created with a text editor.

MIDI binding maps are accessible by double-clicking [Edit \> Preferences
\> Control Surfaces \> Generic MIDI]{.kbd .menu}. Ardour will retain
your selection after you choose one.

## Creating new MIDI maps

### The Basic Concept

Since the beginning of time (well, sometime early in the 2.X series),
Ardour has had the concept of identifying each track and bus with a
[remote control ID]{.dfn}. This ID uniquely identifies a track or bus so
that when messages arrive from elsewhere via MIDI or OSC, we can
determine which track or bus they are intended to control. See [remote
control IDs](@@controlling-track-ordering) for more information. You
just need to know that there is a \"first track\" and its remote control
ID is 1, and so on.

### Getting Started

MIDI bindings are stored in files with the suffix \".map\" attached to
their name. The minimal content looks like this:

    <?xml version="1.0" encoding="UTF-8"?>
    <ArdourMIDIBindings version="1.0.0" name="The name of this set of bindings" manufacturer="Maker of the MIDI device">
    </ArdourMIDIBindings>

So, to start, create a file with that as the initial contents.

The file should be located in the midi_maps sub directory located in the
[Ardour configuration
directory](@@files-and-directories-ardour-knows-about)

### Finding out what your MIDI control surface sends

This is the most complex part of the job, but it\'s still not very hard.
You need to connect the control surface to an application that will show
you the information that the device sends each time you modify a knob,
slider, button etc. There are a variety of such applications (notably
`gmidimon` and `kmidimon`, but you can actually use Ardour for this if
you want. Start Ardour in a terminal window, connect MIDI ports up, and
in the Preferences window, enable \"Trace Input\" on the relevant MIDI
port. A full trace of the MIDI data received will show up in the
terminal window. (Note: in Ardour3, you get a dedicated, custom dialog
for this kind of tracing.)

### Types of Bindings

There are two basic kinds of bindings you can make between a MIDI
message and something inside Ardour. The first is a binding to a
specific parameter of a track or bus. The second is a binding to
something that will change Ardour\'s state in some way (the
\"something\" could either be called a function or an action, see
below).

#### Binding to Track/Bus controls

A track/bus binding has one of three basic structures

` <Binding `*`msg specification`*` uri="`*`… control address …`*`"/> <Binding `*`msg specification`*` function="`*`… function name …`*`"/> <Binding `*`msg specification`*` action="`*`… action name …`*`"/> `

#### Message specifications

You can create a binding for either 3 types of channel messages, or for
a system exclusive (\"sysex\") message. A channel message specification
looks like this:

` <Binding channel="1" ctl="13" … `

This defines a binding for a MIDI Continuous Controller message
involving controller 13, arriving on channel 1. There are 16 MIDI
channels, numbered 1 to 16. Where the example above says `ctl`, you can
alternatively use `note` (to create binding for a Note On message) or
`pgm` (to create a binding for a Program Change message).

Continuous Controllers (CCs) have coninued to evolve for different
controllers. The use of Encoders, RPN, NRPN, and controller buttons that
give a 0 value when released instead of toggling are now supported.
These all have their own type. The whole list of CC types are:

-   ctl - sets a CC to the value sent (works the same as `note` with the
    `momentary` parameter set)
-   ctl-toggle - for CC controls that send a 127 for button press and 0
    for button release. The release is ignored and the value is toggled
    with each press. (works the same as `note`)
-   ctl-dial - passes the CC value to the controlled object
-   rpn - The CC value may be a 14 bit value
-   nrpn - The CC number and the value may both be 14 bit values
-   rpn-delta - The value is expected to be a signed 14bit value that is
    added to the current value. For use with encoders
-   nrpn-delta - The value is expected to be a signed 14bit value that
    is added to the current value. For use with encoders
-   enc-r, enc-l, enc-2 and enc-b - For 7 bit encoders. [Learn more
    about working with encoders](@@generic-midi-and-encoders)

Ardour 5.12 has a bug with the encoder detection where the first encoder
message resets the control to 0. Setting \"Enable Feedback\" on allows
encoders to work as expected.

You can also bind sysex messages:

` <Binding sysex="f0 0 0 e 9 0 5b f7" …. <Binding sysex="f0 7f 0 6 7 f7" …. `

The string after the `sysex=` part is the sequence of MIDI bytes, as
hexadecimal values, that make up the sysex message.

Finally, you can bind a totally arbitrary MIDI message:

` <Binding msg="f0 0 0 e 9 0 5b f7" …. <Binding msg="80 60 40" …. `

The string after the `msg=` part is the sequence of MIDI bytes, as
hexadecimal values, that make up the message you want to bind. Using
this is slightly less efficient than the other variants shown above, but
is useful for some oddly designed control devices.

As of Ardour 4.6 it is possible to use multi-event MIDI strings such as
two event CC messages, RPN or NRPN.

The `sysex=` and `msg=` bindings will only work with `function=` or
`action=` control addresses. They will *not* work with the `uri=`
control addresses. Controls used with `uri=` require a *Value* which is
only available in a known place with channel mode MIDI events.

#### Control address

A [control address]{.dfn} defines what the binding will actually
control. There are quite a few different things that can be specified
here:

Enable Feedback applies to these \"Control Addresses\" only.

|                         |                                                                         |
|-------------------------|-------------------------------------------------------------------------|
| /route/gain             | the gain control (\"fader\") for the track/bus                          |
| /route/trim             | the trim control for the track/bus (new in 4.1)                         |
| /route/solo             | a toggleable control for solo (and listen) of the track/bus             |
| /route/mute             | a toggleable control to mute/unmute the track/bus                       |
| /route/recenable        | a toggleable control to record-enable the track                         |
| /route/panwidth         | interpreted by the track/bus panner, should control image \"width\"     |
| /route/pandirection     | interpreted by the track/bus panner, should control image \"direction\" |
| /route/plugin/parameter | the Mth parameter of the Nth plugin of a track/bus                      |
| /route/send/gain        | the gain control (\"fader\") of the Nth send of a track/bus             |

Each of the specifications needs an address, which takes various forms
too. For track-level controls (solo/gain/mute/recenable), the address is
one the following:

|                         |                                                                                                               |
|-------------------------|---------------------------------------------------------------------------------------------------------------|
| a number, e.g. \"1\"    | identifies a track or bus by its remote control ID                                                            |
| B, followed by a number | identifies a track or bus by its remote control ID within the current bank (see below for more on banks)      |
| S, followed by a number | identifies a selected track in order they have been selected, S1 should be the same track as the Editor Mixer |
| one or more words       | identifies a track or bus by its name                                                                         |

For send/insert/plugin controls, the address consists of a track/bus
address (as just described) followed by a number identifying the
plugin/send (starting from 1). For plugin parameters, there is an
additional third component: a number identifying the plugin parameter
number (starting from 1).

One additional feature: for solo and mute bindings, you can also add
`momentary="yes"` after the control address. This is useful primarily
for NoteOn bindings---when Ardour gets the NoteOn it will solo or mute
the targeted track or bus, but then when a NoteOff arrives, it will
un-solo or un-mute it.

#### Bindings to Ardour \"functions\"

There is currently no feedback available for functions.

Rather than binding to a specific track/bus/plugin control, it may be
useful to have a MIDI controller able to alter some part of Ardour\'s
state. Ardour\'s Generic MIDI support provides a small number of
easily-used \"functions\" to do the most common operations, using a
binding that looks like this:

` <Binding channel="1" note="13" function="transport-roll"/> `

In this case, a NoteOn message for note number 13 (on channel 1) will
start the transport rolling.

Note that a much greater number of operations are possible using
actions, described below.

The following function names are available:

|                     |                                                               |
|---------------------|---------------------------------------------------------------|
| `transport-stop`    | stop the transport                                            |
| `transport-roll`    | start the transport \"rolling\"                               |
| `transport-zero`    | move the playhead to the zero position                        |
| `transport-start`   | move the playhead to the start marker                         |
| `transport-end`     | move the playhead to the end marker                           |
| `loop-toggle`       | turn on loop playback                                         |
| `toggle-rec-enable` | toggle the global record button                               |
| `rec-enable`        | enable the global record button                               |
| `rec-disable`       | disable the global record button                              |
| `next-bank`         | move track/bus mapping to the next bank (see Banks below)     |
| `prev-bank`         | move track/bus mapping to the previous bank (see Banks below) |

#### Binding to Ardour \"actions\"

It is not possible to have feedback available for actions because these
represent keyboard shortcuts which are input only.

You can also bind a sysex or arbitrary message to any of the items that
occur in Ardour\'s main menu (and its submenus). The [list of
actions](@@list-of-menu-actions) shows all available values of
*action-name*.

To create a binding between an arbitrary MIDI message (we\'ll use a
note-off on channel 1 of MIDI note 60 (hex) with release velocity 40
(hex)), the binding file would contain:

` <Binding msg="80 60 40" action="Editor/temporal-zoom-in"/> `

The general rule, when taken an item from the keybindings file and using
it in a MIDI binding is to simply strip the `<Action>` prefix of the
second field in the keybinding definition.

#### Transport controls via MMC

Some controllers like the Arturia KeyLab 49 have transport control
buttons that send MIDI Machine Control (MMC) commands by default. In
Ardour, MMC commands are mapped automatically to their corresponding
transport functions, but need to be received on the `ardour:MMC in` MIDI
port. In [Window \> MIDI Connections]{.kbd .menu}, ensure that the MIDI
controller is connected to the `MMC in` port found in the `Ardour Misc`
right-hand side tab.

Additionally in [Transport \>
Chase](@@preferences#preferences-transport-chase) preferences, make sure
that [Respond to MMC commands]{.dfn} is checked and [Inbound MMC device
ID:]{.dfn} is the same as the MIDI controller\'s internal setting
(usually 127 or 0).

### Banks and Banking

Because many modern control surfaces offer per-track/bus controls for
far fewer tracks & busses than many users want to control, Ardour offers
the relatively common place concept of [banks]{.dfn}. Banks allow you to
control any number of tracks and/or busses easily, regardless of how
many faders/knobs etc. your control surface has.\
To use banking, the control addresses must be specified using the [bank
relative]{.dfn} format mentioned above (\"B1\" to identify the first
track of a bank of tracks, rather than \"1\" to identify the first
track).

One very important extra piece of information is required to use
banking: an extra line near the start of the list of bindings that
specifies how many tracks/busses to use per bank. If the device has 8
faders, then 8 would be a sensible value to use for this. The line looks
like this:

` <DeviceInfo bank-size="8"/> `

In addition, you probably want to ensure that you bind something on the
control surface to the `next-bank` and `prev-bank` functions, otherwise
you and other users will have to use the mouse and the GUI to change
banks, which rather defeats the purpose of the bindings.

### The Selected Strip

Often times one wants to just deal with the strip currently selected by
the GUI (or the control surface). In the same way as with banks above
the selected strip can be designated with *S1*.

## A Complete (though muddled) Example

    <?xml version="1.0" encoding="UTF-8"?>
    <ArdourMIDIBindings version="1.0.0" name="pc1600x transport controls" manufacturer="Peavey">
      <DeviceInfo bank-size="16"/>
      <Binding channel="1" ctl="1"   uri="/route/gain B1"/>
      <Binding channel="1" ctl="2"   uri="/route/gain B2"/>
      <Binding channel="1" ctl="3"   uri="/route/send/gain B1 1"/>
      <Binding channel="1" ctl="4"   uri="/route/plugin/parameter B1 1 1"/>
      <Binding channel="1" ctl="6"   uri="/bus/gain master"/>

      <Binding channel="1" note="1"  uri="/route/solo B1"/>
      <Binding channel="1" note="2"  uri="/route/solo B2" momentary="yes"/>

      <Binding channel="1" note="15"  uri="/route/mute B1" momentary="yes"/>
      <Binding channel="1" note="16"  uri="/route/mute B2" momentary="yes"/>

      <Binding channel="1" enc-r="11"   uri="/route/pandirection B1"/>
      <Binding channel="1" enc-r="12"   uri="/route/pandirection B2"/>

      <Binding sysex="f0 0 0 e 9 0 5b f7" function="transport-start"/>
      <Binding sysex="f0 7f 0 6 7 f7" function="rec-disable"/>
      <Binding sysex="f0 7f 0 6 6 f7" function="rec-enable"/>
      <Binding sysex="f0 0 0 e 9 0 53 0 0 f7" function="loop-toggle"/>

      <Binding channel="1" note="13" function="transport-roll"/>
      <Binding channel="1" note="14" function="transport-stop"/>
      <Binding channel="1" note="12" function="transport-start"/>
      <Binding channel="1" note="11" function="transport-zero"/>
      <Binding channel="1" note="10" function="transport-end"/>
    </ArdourMIDIBindings>

Please note that channel, controller and note numbers are specified as
decimal numbers in the ranges 1-16, 0-127 and 0-127 respectively (the
channel range may change at some point).
