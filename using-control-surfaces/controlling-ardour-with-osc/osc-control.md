# Basics
[OSC]{.dfn} lets synthesizers and other devices communicate with Ardour.
OSC devices can send commands relating to playback (such as play or
stop), performance (such as volume, play, stop), and almost any other
function (such as Edit, or Undo).

*Note:* OSC control has changed dramatically since Ardour 4.7. The Path
structure has been completely redone, Banking has been introduced, The
controller is now able to tell Ardour what kind of feedback it can work
with (including bank size) and the gain controls have new math
calculations.

-   [Control Surface Set](#osc_set-up)
-   [Master or Global messages](#osc_global)
-   [Transport Control](#osc_transport)
-   [Recording control](#osc_recording)
-   [Transport Information](#osc_information)
-   [Editing-related](#osc_editing)
-   [Master and Monitor strip control](#osc_Master-strip)
-   [Track specific operations](#osc_strips)
-   [Selected Strip Operations](#osc_select)
-   [Selected Plugin Operations](#osc_plugins)
-   [Menu actions](#osc_menu)

Ardour is probably one of the most OSC-controllable audio applications
around, but as with all OSC-controllable apps, you can\'t do much
without knowing what [messages]{.dfn} can be sent. This document
describes the various categories of messages that Ardour understands. It
is subject to change, particularly the \"Actions\" part below, since
this relates to the GTK GUI for Ardour rather than the backend.

## Connecting to Ardour via OSC

OSC support is not enabled by default, but can be turned on via [Edit \>
Preferences \> Control Surfaces]{.kbd .menu}. Once enabled, Ardour will
listen on port `3819` by default. This port number can be changed by
editing `$ARDOUR_CONFIG` and adding this line within the `<Config>`
section:

[\<Option name=\"osc-port\" value=\"*Your choice here*\"/\>]{.kbd
.input}

Ardour sends any feedback to the port and address that sent any feedback
request or to a port set manually in the setup dialog. The port does not
have to match Ardour\'s port. In fact it is better not to. This means
that Ardour can deal with more than one controller at a time. The two
controllers can bank independently and even use different math for
faders. This could be used to allow talent to adjust their own monitor
mix using a tablet or phone that can run an OSC controller. For a full
explanation of how Ardour\'s feedback works please read [OSC feedback In
Ardour.](@@osc58-feedback)

## Control Surface Set Up
{#osc_set-up}

Control surface set up allows the controller to tell Ardour about its
capabilities. The surface can tell Ardour how many control strips it has
for banking, if it is capable of setting its faders or buttons to values
set by Ardour\'s GUI or automation, What kind of math the faders use and
more.

Any time the */set_surface* command is sent, the current bank is
recalculated and if feedback is turned on, the values of each strip\'s
controls are sent (or refreshed) as well. This will also refresh the
Master feedback setup.

As of Ardour 5.1, There is now a GUI setup in response to those using
tablets with applications such as touchOSC or AndrOSC who need to be
able to set a port for Ardour to send to. It can also change the default
setting for set_surface. For more information about Ardour\'s OSC
configuration GUI please read [Ardour\'s Setup
Dialog.](@@osc58-using-the-setup-dialog)

If /set_surface is not sent, the default values are used:

-   *Bank Size*: 0 --- No banking (or infinite bank size).
-   *Strip Types*: 159 --- All strip types except hidden and special.
-   *Feedback*: 0 --- All off.
-   *Fader Mode*: 0 --- gain in dB (not relevant with feedback off)
-   *Send Page Size*: 0 --- No Send Paging.
-   *Plugin Page Size*: 0 --- No Plugin (parameter) Paging.
-   *reply port*: 8000 --- control surface will receive feedback on port
    8000
-   *Link set*: 0 --- no linking for this control surface
-   *Link ID*: 0 --- no link ID

These values give the same behaviour as prior versions of Ardour. (or
the closest possible)

[/set_surface *bank_size* *strip_types* *feedback* *fadermode*
*send_page_size* *plugin_page_size* *port* *linkset* *linkid*]{.kbd
.osc}

See below for an explanation of each parameter.

The /set_surface message may have all values except the last in-line.
For example: `/set_surface/8/31/8403/0/8 i 16` would be valid. Do be
careful of switches which send a 0 on release, it may be necessary to
set the value as the release value rather than the press value.

The /set_surface message may have less than the full set of parameters.
those left out will remain as they were before the /set_surface message
was sent. All parameters included must be valid. For example, setting
send page size would require also setting bank_size, strip_types,
feedback and gain mode. using only two parameters will set bank_size and
strip_types. Sending /set_surface with no parameters will result in
Ardour returning a /set_surface message with the current settings.
Surfaces using /set_surface iiii b st fb gm as was the case in versions
of Ardour older than 5.10 will continue to work.

### bank_size

Bank Size is the number of channel strips the controller supports
without banking. Setting this to 0 turns banking off by setting the bank
size to infinite.

Bank size can also be set with */set_surface/bank_size size.*

### strip_types

strip_types is an integer made up of bits. The easy way to deal with
this is to think of strip_types items being worth a number and then
adding all those numbers together for a value to send. Strip Types will
determine what kind of strips will be included in bank. This would
include: Audio, MIDI, busses, VCAs, Master, Monitor and hidden or
selected strips.

Aside from setting the track types for the main mix assignments, using
/set_surface/strip_types with more than one surface button will allow
switching between modes for example: inputs only, busses only, selected
only, hidden only, by having the buttons send values of: 3, 12, 256,
512. A full mix button might have a value 31.

While Master and Monitor are listed as possibilities, most surfaces will
not use them. Using /master and /monitor makes more sense. However, in
the case where there are no master or monitor fader strips on the
surface, it may be necessary to include them in the banked strips.

Please see: [Calculating Feedback and Strip-types
Values.](@@osc58-feedback-and-strip-types-values)

Strip types can also be set with */set_surface/strip_types types.*

### feedback

Feedback is an integer made up of bits. The easy way to deal with this
is to think of feedback items being worth a number and then adding all
those numbers together for a value to send.

Please see: [Calculating Feedback and Strip-types
Values.](@@osc58-feedback-and-strip-types-values#feedback)

Feedback can also be set with */set_surface/feedback feedback.*

### gainmode

Gainmode is an int:

-   *0:* dB value as a float from -193 to +6. Sent as [/strip/gain SSID
    value]{.kbd .osc}. (-193 or below are the same as −∞)
-   *1:* A positional fader based on the same math as Ardour\'s GUI. A
    Float from 0 to 1. Sent as [/strip/fader SSID value]{.kbd .osc}. At
    the same time the gain value in dB is sent to the channel name as
    text. The name will be restored after a short timeout.
-   *2:* A positional fader based on the same math as Ardour\'s GUI. A
    Float from 0 to 1. Sent as [/strip/fader SSID value]{.kbd .osc}. At
    the same time the gain value in dB is sent as [/strip/gain SSID
    value]{.kbd .osc}.
-   *3:* A positional fader based on the same math as Ardour\'s GUI. A
    Float from 0 to 1. Sent as [/strip/fader SSID value]{.kbd .osc}.

Gainmode applies only to feedback values. The controller can choose
which gain math to use by choosing to use the /\*/gain or /\*/fader path
to send to Ardour. This makes sure a controller that doesn\'t set up
Ardour\'s OSC can still use either math. The gainmode for feedback also
determines the path Ardour uses for feedback so that the feedback
messages match the control messages.

Gain mode can also be set with */set_surface/gainmode gainmode.*

### send_page_size

Send_page_size is an int for the number of send channels that can be
controlled at one time. Each channel has a name, level and enable
control. (added in Ardour 5.10)

Send page size can also be set with */set_surface/send_page_size
send_page_size.*

### plugin_page_size

plugin_page_size is an int for the number of plugin controls that can be
controlled at one time. Each control has a name and level. As each
plugin is different (as is each parameter), the surface should expect to
control the plugin parameters with a variable control (pot or slider)
with a float value from 0 to 1 (even on/off switches). (added in Ardour
5.10)

Plugin page size can also be set with */set_surface/plugin_page_size
plugin_page_size.*

### port

The port the controller would like to receive it\'s feedback on.
Starting with Ardour 6.0, the surface can directly set the manual port
or set it\'s host to `auto` port mode.

The value for `port` can be 0 for `auto` port mode or any port value
above 1024. It is suggested not to use Ardour\'s port number of 3819 as
controllers on the same machine that try to use the same port will fail.

If the surface does not tell Ardour which port to use, the default is
8000 or the setting set up in the OSC setup GUI. There can only be one
port setting per host. If that setting is `auto`, than more than one
controller can be run on that host, but if a manual port is set there
can only be one. In the case of `auto` mode, the control surface must
set it\'s receive port to be the same as it\'s send port. If that is not
possible, then manual port mode must be used. This allows a smart
controller to use a number of ports on the same ip while a smartphone
set up as a personal monitor control can use the default manual port.

The host\'s port can also be set with */set_surface/port port.*

Changing the port will remove feedback from a device on the same host
using a different port.

### Link set and Link ID

Please see [Linking Surfaces](@@osc58-linking-surfaces) For more
information.

## Querying Ardour for information

The control Surface may wish to control the type a frequency of updates
it receives. It can do this with querying commands. See: [Querying
Ardour with OSC.](@@osc58-querying-ardour)

## Using more than one surface

Ardour can use more than one surface at a time that both control the
same controls in Ardour. It is also possible to use two surfaces in
concert with each other. See: [Linking
Surfaces](@@osc58-linking-surfaces) for more information.

## List of OSC messages

Parameter types show how the value will be used. However, they may be
sent as a different type if needed, see: [Parameter Types in
OSC.](@@osc58-parameter-types)

This list shows all messages that can be sent to Ardour to control it.
Most of these messages are also sent back as feedback when the
corresponding value changes. There exist additional feedback-only
messages, see: [Feedback](@@osc58-feedback) for more information.

### Master or Global messages
{#osc_global}

#### Transport Control
{#osc_transport}

|                                           |                                                                                                                                                                                                                                                 |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [/transport_stop]{.kbd .osc}              | Stops a rolling transport                                                                                                                                                                                                                       |
| [/transport_play]{.kbd .osc}              | Puts transport in play mode                                                                                                                                                                                                                     |
| [/toggle_roll]{.kbd .osc}                 | Toggles between play and stop                                                                                                                                                                                                                   |
| [/stop_forget]{.kbd .osc}                 | Stop transport and delete/forget last take                                                                                                                                                                                                      |
| [/set_transport_speed *speed*]{.kbd .osc} | where *speed* is a float ranging from -8.0f to 8.0f                                                                                                                                                                                             |
| [/ffwd]{.kbd .osc}                        | Adds 1.5 times to transport speed to maximum +8 times normal speed                                                                                                                                                                              |
| [/rewind]{.kbd .osc}                      | Adds -1.5 times to transport speed to maximum -8 times normal speed                                                                                                                                                                             |
| [/goto_start]{.kbd .osc}                  | Move playhead to start of session                                                                                                                                                                                                               |
| [/goto_end]{.kbd .osc}                    | Move playhead to end of session                                                                                                                                                                                                                 |
| [/jump_bars *bars*]{.kbd .osc}            | Where *bars* is a float (+/-) of the number of bars to jump                                                                                                                                                                                     |
| [/jump_seconds *seconds*]{.kbd .osc}      | Where *seconds* is a float (+/-) of the number of seconds to jump                                                                                                                                                                               |
| [/toggle_click]{.kbd .osc}                | Toggle metronome click on and off                                                                                                                                                                                                               |
| [/marker *marker*]{.kbd .osc}             | Where *marker* may be a float or int of the nth marker or a string with the marker name to locate to (new Ardour 6.0). If the playhead is at a marker and the *marker* is unique, the marker at the playhead will be renamed to the string sent |
| [/add_marker]{.kbd .osc}                  | (adds marker to the current transport position)                                                                                                                                                                                                 |
| [/remove_marker]{.kbd .osc}               | Removes marker at the current transport position (if there is one)                                                                                                                                                                              |
| [/next_marker]{.kbd .osc}                 | Move playhead to next marker                                                                                                                                                                                                                    |
| [/prev_marker]{.kbd .osc}                 | Move playhead to previous marker                                                                                                                                                                                                                |
| [/locate *spos* *roll*]{.kbd .osc}        | where *spos* is the target position in samples and *roll* is a bool/integer defining whether you want transport to be kept rolling or not                                                                                                       |
| [/loop_toggle]{.kbd .osc}                 | Toggle loop mode on and off                                                                                                                                                                                                                     |
| [/loop_location *start* *end*]{.kbd .osc} | *start* is the beginning of a loop and *end* is the end of a loop both are integer frame positions.                                                                                                                                             |
| [/midi_panic]{.kbd .osc}                  | Ardour will send an all notes off to all midi tracks                                                                                                                                                                                            |
| [/cancel_all_solos]{.kbd .osc}            | Cancel All Solos/PFLs/AFLs                                                                                                                                                                                                                      |

New for Ardour 5.9.

|                               |                                                                                                                        |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [/scrub *delta*]{.kbd .osc}   | Where *delta* is a float indicating forward or reverse movement. See [OSC Scrub Modes](@@osc58-jog-modes#scrub)        |
| [/jog *delta*]{.kbd .osc}     | Where *delta* is a float indicating forward or reverse movement                                                        |
| [/jog/mode *mode*]{.kbd .osc} | Where *mode* is an int from 0 to 7 indicating what the */jog* command controls. See [OSC Jog Modes](@@osc58-jog-modes) |

#### Recording control
{#osc_recording}

|                                 |                              |
|---------------------------------|------------------------------|
| [/toggle_punch_in]{.kbd .osc}   |                              |
| [/toggle_punch_out]{.kbd .osc}  |                              |
| [/rec_enable_toggle]{.kbd .osc} | Toggles master record enable |

#### Transport Information
{#osc_information}

|                               |                                                    |
|-------------------------------|----------------------------------------------------|
| [/transport_frame]{.kbd .osc} | Ardour sends /transport_frame *current_frame*      |
| [/transport_speed]{.kbd .osc} | Ardour sends /transport_speed *speed*              |
| [/record_enabled]{.kbd .osc}  | Ardour sends /record_enabled *recordenable_status* |

#### Editing-related
{#osc_editing}

|                                       |                                                                  |
|---------------------------------------|------------------------------------------------------------------|
| [/undo]{.kbd .osc}                    |                                                                  |
| [/redo]{.kbd .osc}                    |                                                                  |
| [/save_state]{.kbd .osc}              | (this is the regular [Session \> Save]{.kbd .menu} operation)    |
| [/session_name *new_name*]{.kbd .osc} | Set session name to *new_name* (if new_name is legal and unique) |

#### Master and Monitor strip control
{#osc_Master-strip}

|                                                     |                                                                                                                        |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [/master/gain *dB*]{.kbd .osc}                      | dB is a float indicating the desired gain in dB                                                                        |
| [/master/fader *position*]{.kbd .osc}               | position is a float between 0 and 1 setting the desired position of the fader                                          |
| [/master/db_delta *delta*]{.kbd .osc}               | where *delta* is a float that will increase or decrease the gain of master by the amount of the delta. (Ardour 5.11+)  |
| [/master/trimdB *dB*]{.kbd .osc}                    | dB is a float from -20 to +20 representing the desired trim gain in dB                                                 |
| [/master/pan_stereo_position *position*]{.kbd .osc} | position is a float from 0 to 1 representing the desired pan position                                                  |
| [/master/mute *key*]{.kbd .osc}                     | key is an optional float 1 representing a master bus select                                                            |
| [/master/select *state*]{.kbd .osc}                 | state is an int of o or 1 representing the desired mute state                                                          |
| [/monitor/gain *dB*]{.kbd .osc}                     | dB is a float indicating the desired gain in dB                                                                        |
| [/monitor/fader *position*]{.kbd .osc}              | position is a float between 0 and 1 setting the desired position of the fader                                          |
| [/monitor/db_delta *delta*]{.kbd .osc}              | where *delta* is a float that will increase or decrease the gain of monitor by the amount of the delta. (Ardour 5.11+) |
| [/monitor/mute *state*]{.kbd .osc}                  | state is an int of 0 or 1 where 1 is muted                                                                             |
| [/monitor/dim *state*]{.kbd .osc}                   | state is an int of 0 or 1 where 1 is dimmed                                                                            |
| [/monitor/mono *state*]{.kbd .osc}                  | state is an int of 0 or 1 where 1 is mono mode                                                                         |

### Track specific operations
{#osc_strips}

For each of the following, *ssid* is the Surface Strip ID for the track

As of Ardour 6.0, the user may use a subset all available strips. See:
[Making a user selected strip list.](@@osc58-custom-strips)

SSID has a different meaning than RID in Ardour version 4.7 and before.
Effectively, banking is always being used and the SSID is generated on
the fly. The SSID is the position of the strip within bank as an int 1
to bank size. There are no gaps as there have been in the past.
Depending on the value of strip_types sent to Ardour, Master and
Monitor, may be included in the list of SSIDs or not as set in
*/set_surface*.

Some Surfaces (many Android applets) are not able to deal with more than
one parameter in a command. However, the two parameter commands below
can also be sent as /strip/command/ssid param. In this case the param
should be a float even if an int is required below.

|                                                                    |                                                                                                                                                                                          |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [/bank_up]{.kbd .osc}                                              | Change bank to the next higher bank.                                                                                                                                                     |
| [/bank_up *delta*]{.kbd .osc}                                      | Where *delta* is a float of 1 to bank up and -1 is bank down for use with an encoder (Ardour 5.11+)                                                                                      |
| [/bank_down ]{.kbd .osc}                                           | Change bank to the next lower bank.                                                                                                                                                      |
| [/use_group *state*]{.kbd .osc}                                    | Where *state* is a float of 1 to use group or 0 to not use group. [more info on use_group](@@osc58-feedback-and-strip-types-values#use-group)                                            |
| [/strip/spill *ssid*]{.kbd .osc}                                   | Use strips this strip is grouped with or those that feed this bus (if this strip is a bus) or that this vca (if this is a VCA) controls. See [Spill Strips](#osc_spill) for more details |
| [/strip/hide *ssid* *y/n*]{.kbd .osc}                              | Where *y/n* = 1 hide this strip, 0 for show this track. [Hiding strips.](@@osc58-feedback-and-strip-types-values#hidden)                                                                 |
| [/strip/name *ssid* *strip_name*]{.kbd .osc}                       | where *strip_name* is a string representing the desired name for the strip                                                                                                               |
| [/strip/group *ssid* *group_name*]{.kbd .osc}                      | where *group_name* is a string representing the name of the group desired. See [groups](#osc_groups) for more details                                                                    |
| [/strip/mute *ssid* *mute_st*]{.kbd .osc}                          | where *mute_st* is a bool/int representing the desired mute state of the track                                                                                                           |
| [/strip/solo *ssid* *solo_st*]{.kbd .osc}                          | where *solo_st* is a bool/int representing the desired solo state of the track                                                                                                           |
| [/strip/solo_iso *ssid* *state*]{.kbd .osc}                        | where *state* is a bool/int representing the desired solo isolate state of the track                                                                                                     |
| [/strip/solo_safe *ssid* *state*]{.kbd .osc}                       | where *state* is a bool/int representing the desired solo safe/lock state of the track                                                                                                   |
| [/strip/monitor_input *ssid* *monitor_st*]{.kbd .osc}              | where *monitor_st* is a bool/int where 1 is forced input monitoring.                                                                                                                     |
| [/strip/monitor_disk *ssid* *monitor_st*]{.kbd .osc}               | where *monitor_st* is a bool/int where 1 is forced disk monitoring. When input and disk are both off, Auto monitoring is enabled.                                                        |
| [/strip/recenable *ssid* *rec_st*]{.kbd .osc}                      | where *rec_st* is a bool/int representing the desired rec state of the track                                                                                                             |
| [/strip/record_safe *ssid* *rec_st*]{.kbd .osc}                    | where *rec_st* is a bool/int representing the desired record safe state of the track                                                                                                     |
| [/strip/polarity *ssid* *invert*]{.kbd .osc}                       | where *invert* is a bool/int representing the desired polarity of the track                                                                                                              |
| [/strip/gain *ssid* *gain*]{.kbd .osc}                             | where *gain* is a float ranging from -193 to 6 representing the desired gain of the track in dB.                                                                                         |
| [/strip/fader *ssid* *position*]{.kbd .osc}                        | where *position* is a float ranging from 0 to 1 representing the fader control position.                                                                                                 |
| [/strip/db_delta *ssid* *delta*]{.kbd .osc}                        | where *delta* is a float that will increase or decrease the gain of a track by the amount of the delta. (Ardour 5.11+)                                                                   |
| [/strip/\*/automation *ssid* *mode*]{.kbd .osc}                    | where *mode* is an int ranging from 0 to 3 representing the desired automation mode for the control. [See OSC Automation.](@@osc58-automation)                                           |
| [/strip/\*/touch *ssid* *state*]{.kbd .osc}                        | where *state* is an int of 1 for touched and 0 for released. [See OSC Automation.](@@osc58-automation)                                                                                   |
| [/strip/trimdB *ssid* *trim_db*]{.kbd .osc}                        | where *trim_db* is a float ranging from -20 to 20 representing the desired trim of the track in dB.                                                                                      |
| [/strip/pan_stereo_position *ssid* *position*]{.kbd .osc}          | where *position* is a float ranging from 0 to 1 representing the desired pan position of the track                                                                                       |
| [/strip/pan_stereo_width *ssid* *width*]{.kbd .osc}                | where *width* is a float ranging from 0 to 1 representing the desired pan width of the track                                                                                             |
| [/strip/send/gain *ssid* *sendid* *send_gain*]{.kbd .osc}          | where *sendid* = nth_send, *send_gain* is a float ranging from -193 to +6 representing the desired gain in dB for the send                                                               |
| [/strip/send/fader *ssid* *sendid* *send_gain*]{.kbd .osc}         | where *sendid* = nth_send, *send_gain* is a float ranging from 0 to 1 representing the desired position for the send as a fader                                                          |
| [/strip/send/enable *ssid* *sendid* *state*]{.kbd .osc}            | where *sendid* = nth_send, *state* is 1 for enabled and 0 for disabled                                                                                                                   |
| [/strip/list ]{.kbd .osc}                                          | see: [Querying Ardour with OSC.](@@osc58-querying-ardour)                                                                                                                                |
| [/strip/sends *ssid*]{.kbd .osc}                                   | see: [Querying Ardour with OSC.](@@osc58-querying-ardour)                                                                                                                                |
| [/strip/receives *ssid*]{.kbd .osc}                                | see: [Querying Ardour with OSC.](@@osc58-querying-ardour)                                                                                                                                |
| [/strip/plugin/list *ssid*]{.kbd .osc}                             | see: [Querying Ardour with OSC.](@@osc58-querying-ardour)                                                                                                                                |
| [/strip/plugin/descriptor *ssid*]{.kbd .osc}                       | see: [Querying Ardour with OSC.](@@osc58-querying-ardour)                                                                                                                                |
| [/strip/plugin/reset *ssid* *piid* ]{.kbd .osc}                    | where *piid* = nth Plugin, will reset all values to the plugin\'s original values                                                                                                        |
| [/strip/plugin/activate *ssid* *piid* ]{.kbd .osc}                 | where *piid* = nth Plugin, will set the plugin\'s state to active                                                                                                                        |
| [/strip/plugin/deactivate *ssid* *piid* ]{.kbd .osc}               | where *piid* = nth Plugin, will set the plugin\'s state to inactive                                                                                                                      |
| [/strip/plugin/parameter *ssid* *piid* *param* *value*]{.kbd .osc} | where *piid* = nth Plugin, *param* = nth param, *value* is a float ranging from 0 to 1 representing the desired parameter value                                                          |
| [/strip/name *ssid* *name*]{.kbd .osc}                             | where *name* is a string for the desired name of the track                                                                                                                               |

### Selected Strip Operations
{#osc_select}

New for Ardour 5, A whole set of operations that work on the selected or
expanded strip.

Selected strip operations are complex enough for their own page. Please
read: [Selection Considerations in
OSC.](@@osc58-selection-and-expansion-considerations) This is most
important if more than one OSC surface is being used with Ardour.

There are two kinds of selection in OSC. GUI selection and local
expansion. By default expansion follows selection.

-   GUI selection: Use */strip/select* to set. Selecting a strip in the
    GUI will set OSC surface select and the surface will set GUI
    selection as well.
-   Local expansion: Use */strip/expand* to expand a strip without
    changing overall selection. When /strip/expand is set to 0 or false,
    the select channel will go back to using the strip selected by the
    GUI. While expand is turned on, selecting a strip on the GUI does
    not select the OSC strip. Sending a /strip/select message will
    override the expand as if it had been set to false. Good for more
    than one OSC controller at a time.

|                                                        |                                                                                                                                                                    |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [/strip/select *ssid* *y/n*]{.kbd .osc}                | Where *y/n* = 1 for select. Sets both GUI select and strip to expanded mode. (0 is ignored)                                                                        |
| [/strip/expand *ssid* *y/n*]{.kbd .osc}                | Where *y/n* = 1 for expanded mode. Sets only local strip to Expanded. Setting to 0 resets the expansion to follow selection.                                       |
| [/select/expand *y/n*]{.kbd .osc}                      | Where *y/n* = 1 for expanded mode, 0 for Select mode.                                                                                                              |
| [/select/hide *y/n*]{.kbd .osc}                        | Where *y/n* = 1 hide this strip, 0 for show this track. [Hiding strips.](@@osc58-feedback-and-strip-types-values#hidden)                                           |
| [/select/name *strip_name*]{.kbd .osc}                 | where *strip_name* is a string representing the desired name for the strip                                                                                         |
| [/select/comment *comment*]{.kbd .osc}                 | where *comment* is a string representing the desired comment for the strip                                                                                         |
| [/select/group *group_name*]{.kbd .osc}                | where *group_name* is a string representing the name of the group desired. See [groups](#osc_groups) for more details                                              |
| [/select/group/enable *state*]{.kbd .osc}              | where *state* is an int representing the desired enable state of the group the selected strip is a part of                                                         |
| [/select/group/gain *state*]{.kbd .osc}                | where *state* is an int which sets the gain sharing of the group the strip belongs to. See [Track and Bus Groups](@@track-and-bus-groups) for more details         |
| [/select/group/relative *state*]{.kbd .osc}            | where *state* is an int which sets relative state of thew group the strip belongs to. See [Track and Bus Groups](@@track-and-bus-groups) for more details          |
| [/select/group/mute *state*]{.kbd .osc}                | where *state* is an int which sets the mute sharing of the group the strip belongs to. See [Track and Bus Groups](@@track-and-bus-groups) for more details         |
| [/select/group/solo *state*]{.kbd .osc}                | where *state* is an int which sets the solo sharing of the group the strip belongs to. See [Track and Bus Groups](@@track-and-bus-groups) for more details         |
| [/select/group/recenable *state*]{.kbd .osc}           | where *state* is an int which sets the recenable sharing of the group the strip belongs to. See [Track and Bus Groups](@@track-and-bus-groups) for more details    |
| [/select/group/select *state*]{.kbd .osc}              | where *state* is an int which sets the select sharing of the group the strip belongs to. See [Track and Bus Groups](@@track-and-bus-groups) for more details       |
| [/select/group/active *state*]{.kbd .osc}              | where *state* is an int which sets the route active sharing of the group the strip belongs to. See [Track and Bus Groups](@@track-and-bus-groups) for more details |
| [/select/group/color *state*]{.kbd .osc}               | where *state* is an int which sets the color sharing of the group the strip belongs to. See [Track and Bus Groups](@@track-and-bus-groups) for more details        |
| [/select/group/monitoring *state*]{.kbd .osc}          | where *state* is an int which sets the monitoring sharing of the group the strip belongs to. See [Track and Bus Groups](@@track-and-bus-groups) for more details   |
| [/select/recenable *y/n*]{.kbd .osc}                   | Where *y/n* is 1 for enabled and 0 for disabled                                                                                                                    |
| [/select/record_safe *y/n*]{.kbd .osc}                 | Where *y/n* is 1 for safe and 0 for unlocked                                                                                                                       |
| [/select/mute *y/n*]{.kbd .osc}                        | Where *y/n* is 1 for enabled and 0 for disabled                                                                                                                    |
| [/select/solo *y/n*]{.kbd .osc}                        | Where *y/n* is 1 for enabled and 0 for disabled                                                                                                                    |
| [/select/solo_iso *state*]{.kbd .osc}                  | where *state* is a bool/int representing the desired solo isolate state of the track                                                                               |
| [/select/solo_safe *state*]{.kbd .osc}                 | where *state* is a bool/int representing the desired solo safe/lock state of the track                                                                             |
| [/select/monitor_input *y/n*]{.kbd .osc}               | Where *y/n* is 1 for monitor from input and 0 for auto                                                                                                             |
| [/select/monitor_disk *y/n*]{.kbd .osc}                | Where *y/n* is 1 for monitor from disk and 0 for auto                                                                                                              |
| [/select/polarity *invert*]{.kbd .osc}                 | where *invert* is a bool/int representing the desired polarity of the track                                                                                        |
| [/select/gain *gain*]{.kbd .osc}                       | Where *gain* is a float ranging from -193 to 6 representing the desired gain of the track in dB.                                                                   |
| [/select/fader *position*]{.kbd .osc}                  | Where *position* is an float ranging from 0 to 1 representing the fader control position.                                                                          |
| [/select/db_delta *delta*]{.kbd .osc}                  | where *delta* is a float that will increase or decrease the gain of the selected track by the amount of the delta. (Ardour 5.11+)                                  |
| [/select/vca *name* *state*]{.kbd .osc}                | where *name* is a string with the name of the VCA, and *state* is an int that determines if the named VCA will control this strip. (Ardour 6.0)                    |
| [/select/vca/toggle *name*]{.kbd .osc}                 | where *name* is a string with the name of the VCA. This toggles the use of the named vca with this strip. Any trailing \"\[\_\]\" will be ignored. (Ardour 6.0)    |
| [/select/spill]{.kbd .osc}                             | show only strips this strip is grouped with or those that feed this bus or that this vca controls. See [Spill Strips](#osc_spill) for more details                 |
| [/select/\*/automation *mode*]{.kbd .osc}              | where *mode* is an int ranging from 0 to 3 representing the desired automation mode for the control. [See OSC Automation.](@@osc58-automation)                     |
| [/select/\*/touch *state*]{.kbd .osc}                  | where *state* is an int of 1 for touched and 0 for released. [See OSC Automation.](@@osc58-automation)                                                             |
| [/select/trimdB *trim_db*]{.kbd .osc}                  | where *trim_db* is a float ranging from -20 to 20 representing the desired trim of the track in dB.                                                                |
| [/select/pan_stereo_position *position*]{.kbd .osc}    | where *position* is a float ranging from 0 to 1 representing the desired pan position of the track                                                                 |
| [/select/pan_stereo_width *width*]{.kbd .osc}          | where *width* is a float ranging from 0 to 1 representing the desired pan width of the track                                                                       |
| [/select/pan_elevation_position *position*]{.kbd .osc} | where *position* is a float ranging from 0 to 1 representing the desired pan elevation of the track                                                                |
| [/select/pan_frontback_position *position*]{.kbd .osc} | where *position* is a float ranging from 0 to 1 representing the desired front to back position of the track                                                       |
| [/select/pan_lfe_control *value*]{.kbd .osc}           | where *value* is a float ranging from 0 to 1 representing the desired LFE control value for the track                                                              |
| [/select/send_gain *sendid* *send_gain*]{.kbd .osc}    | where *sendid* = nth_send, *send_gain* is a float ranging from -193 to +6 representing the desired gain in dB for the send                                         |
| [/select/send_fader *sendid* *send_gain*]{.kbd .osc}   | where *sendid* = nth_send, *send_gain* is a float ranging from 0 to 1 representing the desired position for the send as a fader                                    |
| [/select/send_enable *sendid* *state*]{.kbd .osc}      | where *sendid* = nth_send, *state* is 1 for enabled and 0 for disabled                                                                                             |
| [/select/send_page *delta*]{.kbd .osc}                 | where *delta* is an int or float selecting another send as a delta from the current send.                                                                          |

`/select/send_page` and `/select/plugin_page` may be used with a page up
and page down switch by using a switch with a value of `1` for page up
and a switch with a value of `-1` for page down. An encoder can be used
as well. (these commands were added in Ardour version 5.10)

### Selected Plugin Operations
{#osc_plugins}

These operations control the selected plugin on the selected strip.
Plugins and parameters are specified by their position in the list of
plugins and controllable parameters. Parameters are paged to allow
accessing all parameters on a surface with limited inputs, the plugin
(parameter) page size is configured with [/set_surface]{.kbd .osc}.

When the selected strip is changed, the plugin in the same position in
the newly selected strip is made the selected plugin (even if it is a
different type of plugin). If the new strip has fewer plugins, the last
plugin is selected. If the new strip has no plugins, no plugin is
selected.

```{eval-rst}
+-----------------------------------+-----------------------------------+
| [/select/plugin *delta*]{.kbd     | where *delta* is an int or float  |
| .osc}                             | selecting another plugin as a     |
|                                   | delta from the currently selected |
|                                   | plugin index.                     |
+-----------------------------------+-----------------------------------+
| [/select/plug_page                | where *up_or_down* is 1 for page  |
| *up_or_down*]{.kbd .osc}          | up or -1 for page down (0 is      |
|                                   | ignored).                         |
+-----------------------------------+-----------------------------------+
| [/select/plugin/activate          | where *y/n* is 1 for activating   |
| *y/n*]{.kbd .osc}                 | and 0 for deactivating the        |
|                                   | selected plugin. (new Ardour 6.0) |
+-----------------------------------+-----------------------------------+
| [/select/plugin/parameter *piid*  | where *piid* = nth plugin, *paid* |
| *paid* *value*]{.kbd .osc}\       | = nth parameter and *value* is a  |
| [/select/plugin/parameter *paid*  | float from 0 to 1. If *piid* is   |
| *value*]{.kbd .osc}\              | omitted, the currently selected   |
| [/sele                            | plugin is used. Otherwise, the    |
| ct/plugin/parameter/*piid*/*paid* | specified plugin is made the      |
| *value*]{.kbd .osc}\              | selected plugin and its parameter |
| [/select/plugin/parameter/*paid*  | modified.\                        |
| *value*]{.kbd .osc}               | Feedback messages omit the *piid* |
|                                   | argument. The *paid* is normally  |
|                                   | passed as an argument (second     |
|                                   | form) but can be put in the path  |
|                                   | (last form) using the             |
|                                   | /set_surface/feedback state       |
|                                   | command. See [Calculating         |
|                                   | Feedback and Strip-types          |
|                                   | Values.](@@osc58-feedback         |
|                                   | -and-strip-types-values#feedback) |
+-----------------------------------+-----------------------------------+
```

The *paid* argument is specified as a 1-based index into the list of
*controllable* parameters only (as specified by the controllable flag in
the [[/strip/plugin/descriptor]{.kbd .osc} query
message](@@osc58-querying-ardour), skipping non-controllable-only
parameters).

#### Using groups with strip and select (new for Ardour 6.0)
{#osc_groups}

No grouping will occur unless `use_group` is set either by using
[/set_surface/strip_types]{.kbd .osc} with the use groups bit set or by
using [/use_group i 1]{.kbd .osc}.

The result for [/strip/group]{.kbd .osc} or [/select/group]{.kbd .osc}
is determined by the parameter passed in the command and the current
group and available list of groups. The group name the control surface
sends may be:

-   \"none\", \"\" or \" \" will remove this strip from this group. If
    this was the only strip in this group, the group is deleted. Some
    OSC controllers have trouble sending an empty string and a list of
    groups contains \"none\" as well so a dropdown can just send a text
    item and work.
-   The name of a group this strip does not belong to will remove this
    strip from it\'s current group and add it to the named group. If
    this strip was the only strip in the group it was removed from, that
    group will be deleted.
-   An unused name when this strip is not part of a group will create a
    new group with the group name sent and add this strip to that group
-   An unused name when this strip is already a part of a group will
    rename this group to the name sent.

To create a new group from a strip that is already joined to a group,
the strip must first remove itself from the current group.

#### Spill Strips
{#osc_spill}

[/select/spill]{.kbd .osc} or [/strip/spill]{.kbd .osc} will:

-   set the current set of strips in use to include only the strips that
    are a part of the group the strip is a part of so long as that strip
    is a track.
-   set the current set of strips to the set of strips that feed this
    strip if it is a bus. In the case where this strip is being fed by
    sends rather than strip outputs, the strips that feed this bus will
    have their names set to the name of the strip with *-send* appended
    to it and the fader, pan and mute will control the send rather than
    the strip. The other strip controls will be disabled in this mode.
    This only happens when the strip that calls spill is a bus. In the
    case where a strip that is part of a group is chosen as above where
    the group all sends to a common bus this will not happen. This can
    be useful for a group that uses \"Add New Aux Bus\" to switch from
    sends to faders.
-   set the current set of strips to the set of strips that are
    controlled by the VCA if this strip is a VCA.

spill/group, spill/bus or spill/vca can also be used to force the type
of spilling that is done. This may be useful if the strip is a bus that
is a part of a group and the group variation is required.

In all cases, if there is a bus or VCA attached to the group of strips
it will be included as well.

What is less obvious, is how to return to the normal set of strips.
There are a number of ways of doing so depending on the operator\'s
wishes. The most obvious way is to use [/set_surface/strip_types]{.kbd
.osc} to set the strip list as desired. It is expected that a control
surface may have more than one strip types button in any case to see
only inputs or only busses etc and of course one to give a full mix.
Another option is to reselect the custom set of strips with
[/strip/custom/mode *mode*]{.kbd .osc}.

#### Controlling plugins
{#osc_plugins_details}

### Menu actions
{#osc_menu}

Every single menu item in Ardour\'s GUI is accessible via OSC. There is
a single common syntax to trigger the action as if it was selected with
the mouse (or keyboard):

[/access_action *action_name*]{.kbd .osc}

As of Ardour 5.9, *access_action* can be inlined for control surfaces
that are unable to send string parameters. The *action_name* is composed
of a group and an action in the form of *Group/action* which fits very
well as an OSC path extension:

[/access_action/*Group/action* *key_pressed*]{.kbd .osc}

The key_pressed is optional, but if present is a float 1 or 0 where the
command is ignored if key_pressed is 0.

Some of the Menu Actions duplicate other OSC commands. In all cases it
is better to use the OSC commands rather than the Menu Actions if
possible as the OSC commands are more direct.

The [list of actions](@@list-of-menu-actions) shows all available values
of *action-name* for Ardour.
