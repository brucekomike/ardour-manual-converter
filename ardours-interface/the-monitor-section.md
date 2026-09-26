# Monitor Section
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/monitoring-strip.png" alt="The Monitoring strip" />
<figcaption aria-hidden="true">The Monitoring strip</figcaption>
</figure>

The [Monitor section]{.dfn} is an optional feature that provides Control
Room/Monitor Speaker outputs. It can be activated for the current
session in the [[Session \> Properties]{.kbd .menu}
window](@@session-properties#properties-monitoring) by enabling the [Use
monitor section in this session]{.kbd .option} option in the
[Monitoring]{.kbd .menu} tab. By default the Monitor Section is fed with
audio from the Master Bus, but depending on solo mode and other
functions such as Auditioning, other audio sources may be temporarily
heard instead.

When you click the \"Mon\" button on the Master bus, the Monitor section
appears on the right hand side. It comprises:

1.  Detach/attach control. This separates the Monitor section into its
    own floating window
2.  Status indicators for important functions
3.  Solo behaviour selection
4.  Show, hide and status of the Monitor Sections inline processors
5.  Level controls for solo functionality
6.  Level control for Monitor Dim
7.  Individual monitor path controls
8.  Mute, Dim and Mono functions for the monitor outputs
9.  Monitor level control
10. Monitor output routing

## Status Indicators

The Status indicators, two of which also appear in [the Transport tool
bar](@@about-ardours-interface), flash to indicate when that function is
in operation:

-   [Soloing]{.dfn}: This indicates when one or more tracks or busses
    are currently being soloed. See [Muting and
    Soloing](@@muting-and-soloing). Clicking on this indicator cancels
    all currently soloed channels or busses
-   [Auditioning]{.dfn}: This indicates when an audio file is being
    listened to directly, e.g. when using the import dialogue, or using
    the [Audition]{.kbd .menu} context menu in the [Regions
    List](@@the-region-list). Clicking this indicator cancels the
    current audition
-   [Isolated]{.dfn}: This indicates when one or more tracks or busses
    are solo isolated. See [Muting and Soloing](@@muting-and-soloing).
    Clicking on this indicator cancels any current isolation.

## Solo behaviour selection

The SiP, PFL and AFL controls inter-cancel with each other and select
the desired Solo mode. Excl. Solo and Solo Mute then modify the modes
behaviour. See [Muting and Soloing](@@muting-and-soloing). The current
mode is indicated by the illuminated \'LED\' on the button.

|             |                                                                                          |
|-------------|------------------------------------------------------------------------------------------|
| SiP         | This selects *Solo In Place* as the current solo mode and cancels the previous mode.     |
| PFL         | This selects *Pre Fade Listen* as the current solo mode and cancels the previous mode.   |
| AFL         | This selects *After Fade Listen* as the current solo mode and cancels the previous mode. |
| Excl. Solo  | This enables or disables the *Exclusive Solo* option.                                    |
| Solo » Mute | This enables or disables the *Solo Mute* option.                                         |

Changing the solo mode (SiP, PFL or AFL) will update the labels on the
mixer strips\' solo controls accordingly.

## The Processors button

Clicking the [Processors]{.dfn} button show or hides the Monitor
Sections processor box. This is used in the same way as processor boxes
present in [tracks](@@audiomidi-mixer-strips) and
[busses](@@audiomidi-busses-mixer-strips). It can be used to insert
plugins, e.g. a room correction EQ or a specific metering type.

As this processing is local to the Monitor Section it is only applied to
audio that is ultimately available at the monitor outputs.

## Solo level controls

These controls set the level of the audio when a channel or bus solo is
engaged.

|            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Solo Boost | This is the level that will be added to the current main monitor level when a track or bus is soloed, providing a convenient boost in level for the isolated signal. The rotary control has a range of 0dB to +10dB and can be set at any point between these two values. A drop down menu with pre-defined values is also provided for convenience.                                                                                                                                        |
| SiP Cut    | Only relevant to Solo in Place mode. This sets the level that all muted tracks or busses will be muted by. By default it is −∞ i.e. the non soloed tracks are totally inaudible. The level can be raised to make the other tracks audible, though dimmed. This is also sometimes referred to *Solo in Front*. The rotary control has a range of −∞ to +0dB and can be set at any point between these two values. A drop down menu with pre-defined values is also provided for convenience. |

## Dim level control

The Dim level control sets the amount by which the monitoring will be
reduced when a Dim button is engaged. The rotary control has a range of
-20dB to 0dB and can be set at any point between these two values. A
drop down menu with pre-defined values is also provided for convenience.

## Monitor path controls

Each of the individual paths through the Monitor Section, (e.g. [L]{.kbd
.menu} and [R]{.kbd .menu} for stereo), can be controlled individually.
Four functions are available:

|      |                                                                                 |
|------|---------------------------------------------------------------------------------|
| Mute | Mutes the selected path(s)                                                      |
| Dim  | Reduces the selected path(s) level by the amount set with the Dim level control |
| Solo | Solos the selected channel(s)                                                   |
| Inv  | Inverts the selected channel(s) polarity                                        |

## Global Monitor controls

Those buttons directly affect the output of the monitoring section:

-   [Mono]{.dfn}: sums all of the paths to a single mono signal and
    applies it to all Monitor Section outputs.
-   [Dim]{.dfn}: Reduces overall monitor level by the amount set with
    the Dim level control.
-   [Mute]{.dfn}: Mutes all monitoring.

## Global Monitor level

This control sets the level for Monitor Section output. The rotary
control has a range of −∞ to +6dB and can be set at any point between
these two values. A drop down menu with pre-defined values is also
provided for convenience.

## Monitoring Output routing

Clicking on this button shows a menu that allows quick and convenient
routing of the Monitor Section\'s outputs to audio hardware outputs,
e.g. to feed control room monitors. It also has an option to open
Ardour\'s routing matrix, where more detailed connectivity is available
if routing to something other than hardware is required.
