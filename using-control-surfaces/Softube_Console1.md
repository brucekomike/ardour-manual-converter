# Using the Softube Console1
Ardour has a good support for the Softube Console1 controller.

## Connecting the Console1

Console1 comes with a single USB Socket on the back. Connect a suitable
USB cable from there to a USB port on your computer.

Ardour uses the Console1 as a generic MIDI controller. You do not need
to do anything to enable this---The Console1 sends and receives ordinary
MIDI controller messages to/from the host, and the host understands the
intended meaning of these messages. We note this detail to avoid
speculation about whether Ardour supports the native mode, which sends
MIDI Sysex Messages---it does not.

The Console1 will be automatically recognized by your operating system,
and will appear in any of the lists of possible MIDI ports in both
Ardour and other similar software.

To connect the Console1 to Ardour, open the Preferences dialog, and then
click on \"Control Surfaces\". Click on the \"Enable\" button in the
line that says \"Console1\" in order to activate Ardour\'s Console1
support. Then double click on the line that says \"Console1\". A new
dialog will open, containing two dropdown selectors that will allow you
to identify the MIDI ports where your Console1 is connected.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/c1_settings.png" style="width:100.0%"
alt="The Console 1 configuration dialog" />
<figcaption>The Console1 configuration dialog</figcaption>
</figure>

Once you select the input and output port, Ardour will initialize the
Console1 and it will be ready to use. You only need do this once: once
these ports are connected and your session has been saved, the
connections will be made automatically in this and other future
sessions.

### Checkboxes

The checkbox \"Swap Solo and Mute\" does exactly that. In Ardour and
Mixbus, these buttons are arranged exactly the other way round than in
Console1. Since this can be irritating, the assignment can be reversed
here.

*Work in Progress*\
The checkbox \"Create Plugin Mapping Stubs\" automatically creates
mapping files for external plugins - if they does not already exists.
See the last section \"External Plugins\" for further information.

## Harrison Mixbus & Mixbus 32c

A lot of functionality is developed to be used with Harrison Mixbus and
Harrison Mixbus32c, therefore the assignment of the controls might
sometimes feels a little arbitrary. However, in the future it might be
possible, to control plugins with this surface.\
**Controls only used by Harrison Mixbus (32c) are marked with
\[Mixbus\]**\
**Controls inside a Mixbus only section which are working in Ardour as
well marked with \[Ardour\]**\

## Using the Console1

The [Fine Adjust / Shift]{.kbd .button} button unfortunately does not
work in the generic MIDI mode. Therefore the [Preset / Save Preset]{.kbd
.button} button is used as a shift button. In the following this will be
simply referred to as the *Shift* button

### The controls

#### General

[On]{.kbd .button}

Is lit when a mixer strip is in solo mode and can disables all solo
modes.*Rude Solo*

[Mode]{.kbd .button}

Zooms to selection

[Page Up]{.kbd .button} / [Page Down]{.kbd .button}

Switches 20 mixer strips up or down. Only lit if there is another
page/bank

[1]{.kbd .button}\...[20]{.kbd .button}

Select the nth mixer strip of the current bank.*The Master channel is
always the last mixer strip*

[Track Group]{.kbd .button}/[Track Copy]{.kbd .button}

Unused

[Order]{.kbd .button}

\[Mixbus\]Switches between the compressor modes:
Leveler/Compressor/Limiter --- see Compressor section

[External Sidechain]{.kbd .button}

Switches between Edit, Cue and Mixer Screen

[Input]{.kbd .knob}

Trim

[Input Meter]{.kbd .fader}

Unused

[High Cut]{.kbd .knob}

\[Mixbus\]High Cut

[Low Cut]{.kbd .knob}

\[Mixbus\]Low Cut

[Filter to Compressor]{.kbd .button}

\[Mixbus\]Filters on/off

[Phase]{.kbd .button}

Switches the phase of all channels. If only one of more channels is
switched in the GUI, the LED blinks

[Preset]{.kbd .button}

The Global \'Shift\' button

[Pan]{.kbd .knob}

Pan

[Solo]{.kbd .button}

Solo button for the mixer strip

[Mute]{.kbd .button}

Mute button for the mixer strip, blinks, when the mixer strip is muted
due to another mixer strips Solo-Mode

[Volume Meter]{.kbd .fader}

Shows the mixer strip volume

[Volume]{.kbd .knob}

Sets the mixer strip volume

#### Shape-Section \[Mixbus\]

[Shape]{.kbd .button}

Switches the Gate section on or off

[Shape Meter]{.kbd .fader}

Shows the Gain reduction of the gate

[Gate]{.kbd .knob}

Threshold for the gate

[Gate Release]{.kbd .knob}

Release time for the gate

[Shift]{.kbd .knob}+[Gate Release]{.kbd .knob}

Hysteresis for the gate

[Sustain]{.kbd .knob}

Attack time for the gate

[Shift]{.kbd .knob}+[Sustain]{.kbd .knob}

Hold time for the gate

[Punch]{.kbd .knob}

Depth for the gate

[Shift]{.kbd .knob}+[Punch]{.kbd .knob}

Sidechain filter frequency

[Hard Gate]{.kbd .button}

Sidechain filter on / off

[Shift]{.kbd .knob}+[Hard Gate]{.kbd .button}

Sidechain filter listen

#### Equalizer Section \[Mixbus\]

All encoders in the EQ section are working as sends if the shift button
is activated. See the bus send section.

[Equalizer]{.kbd .button}

Switches the Equalizer section on or off

[Low Gain]{.kbd .knob}

The Gain (reduction or boost) of the semiparametric bass eq

[(Low) Frequency]{.kbd .knob}

The frequency of the semiparametric bass eq

[(Low) Cut / Bell / Shelf]{.kbd .button}

Switches between Cut/Boost or Shelf (this uses only two of the three
states

[Low Mid Gain]{.kbd .knob}

The Gain (reduction or boost) of the semiparametric low mid eq

[(Low Mid) Frequency]{.kbd .knob}

The frequency of the semiparametric low mid eq

[(Low Mid) Shape]{.kbd .knob}

\[Ardour\]The eleventh send of a mixer strip / Send to the eleventh
mixbus

[High Mid Gain]{.kbd .knob}

The Gain (reduction or boost) of the semiparametric high mid eq

[(High Mid) Frequency]{.kbd .knob}

The frequency of the semiparametric high mid eq

[(High Mid) Shape]{.kbd .knob}

\[Ardour\]The twelfth send of a mixer strip / Send to the twelfth mixbus
(see section Mixbusses)

[High Gain]{.kbd .knob}

The Gain (reduction or boost) of the semiparametric treble eq

[(High) Frequency]{.kbd .knob}

The frequency of the semiparametric treble eq

#### Compressor Section \[Mixbus\]

[Compressor]{.kbd .button}

Switches the Compressor on or off

[Compressor Meter]{.kbd .fader}

Shows the gain reduction of the leveler/compressor/limiter

[Order]{.kbd .button}

*Above this section* Switches between the compressor modes:
Leveler/Compressor/Limiter

[Ratio]{.kbd .knob}

Ratio of the compressor

[Parallel Dry/Wet]{.kbd .knob}

Makeup gain of the compressor

[Attack]{.kbd .knob}

Attack time of the compressor

[Release]{.kbd .button}

Release time of the compressor

[Threshold]{.kbd .knob}

Threshold of the compressor

#### Sends

::: well
All Encoders in the equalizer-section are working as sends when
\'shift\' is selected.\
Additionally the Low-Mid and High-Mid shape encoders are sends to the
mixbusses eleven and twelfe. The Idea behind this is to have some common
effects on this two mixbusses which are accessible without \'shift\'.
Currently, this is focused on Mixbus.\
The functionality will be extended to fit better with Ardour in a second
development phase. However, if a mixer strip in Ardour has sends to
busses, these are accessible with the send encoders as well. These are
numbered from top to bottom. The topmost send can be changed by the send
1 encoder [Shift]{.kbd .knob}+[(Low) Frequency]{.kbd .knob}, the next
send below by the send 2 encoder [Shift]{.kbd .knob}+[(Low Mid)
Frequency]{.kbd .knob} and so on.
:::

[Shift]{.kbd .knob}+[(Low) Frequency]{.kbd .knob}

Send 1

[Shift]{.kbd .knob}+[(Low Mid) Frequency]{.kbd .knob}

Send 2

[Shift]{.kbd .knob}+[(High Mid) Frequency]{.kbd .knob}

Send 3

[Shift]{.kbd .knob}+[(High) Frequency]{.kbd .knob}

Send 4

[Shift]{.kbd .knob}+[Low Gain]{.kbd .knob}

Send 5

[Shift]{.kbd .knob}+[Low Mid Gain]{.kbd .knob}

Send 6

[Shift]{.kbd .knob}+[High Mid Gain]{.kbd .knob}

Send 7

[Shift]{.kbd .knob}+[High Gain]{.kbd .knob}

Send 8

[Shift]{.kbd .knob}+[(Low Mid) Shape]{.kbd .knob}

Send 9

[Shift]{.kbd .knob}+[(High Mid) Shape]{.kbd .knob}

Send 10

[(Low Mid) Shape]{.kbd .knob}

Send 11

[(High Mid) Shape]{.kbd .knob}

Send 12

#### External Plugins

::: well
*This is work in progress. But things described here are already working
but might be unstable!*\
Pressing [Group]{.kbd .knob} will set Console1 into external plugin
mode. External plugins are all plugins in case of Ardour and in case of
Mixbus all plugins which are not a fixed part of the mixerstrips.
:::

[Group]{.kbd .knob}

Set or unset the Console 1 into \"External Plugin Mode\"

[1]{.kbd .knob}-[20]{.kbd .knob}

Select the plugin at position \[selected number\]. Pressing repeatedly
then shows or hides the plugin.The LED of the selected channel stay on
permanently, the channel LED of the plugin number stays in \'blinking
mode\'.

[Mute]{.kbd .knob}

Disables the plugin

All other assignements needs to be done with the mapping files. A stub
of such a mapping file can be automatically created when the checkbox
\"Create Plugin Mapping Stubs\" in the \"Control Protocol Settings\"
dialog is enabled.

The mapping files are created in a subdirectory \"c1mappings\" of the
Ardour/Mixbus settings directory

This is the example of a mapping file for the a-compressor. The file
name is created from the unique URL of the plugin. In this case its
**urn:ardour:a-comp.xml**

    <?xml version="1.0" encoding="UTF-8"?>
    <c1plugin-mapping 
            ID="urn:ardour:a-comp" 
            NAME="ACE Compressor">
            <param-mapping id="0">
                    <name>Attack</name>
                    <mapping shift="false">COMP_ATTACK</mapping>
            </param-mapping>

            <param-mapping id="1">
                    <name>Release</name>
                    <mapping shift="false">COMP_RELEASE</mapping>
            </param-mapping>

            <param-mapping id="2">
                    <name>Knee</name>
                    <mapping shift="false"></mapping>
            </param-mapping>

            <param-mapping id="3">
                    <name>Ratio</name>
                    <mapping shift="false">COMP_RATIO</mapping>
            </param-mapping>

            <param-mapping id="4">
                    <name>Threshold</name>
                    <mapping shift="false">COMP_THRESH</mapping>
            </param-mapping>

            <param-mapping id="5">
                    <name>Makeup</name>
                    <mapping shift="false">COMP_PAR</mapping>
            </param-mapping>

            <param-mapping id="6">
                    <name>Sidechain</name>
                    <mapping shift="false"></mapping>
            </param-mapping>
    </c1plugin-mapping>

It is planned to allow creating the mapping file for the plugins inside
the setup dialog. This, however, might take some time.
