# Using the Novation Launch Control XL
Novation Launch Control XL is a compact control surface with 8 faders,
24 encoders, and various keys like track selection, muting, soloing, and
arming a track for recording.

![Novation Launch Control
XL](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/novation-launch-control-xl.svg){.invert-in-dark
style="width:75%;"}

Please refer to the Launch Control XL user manual for specifics on
operating your controller.

## Connecting the Launch Control XL

Plug the USB cable from the Launch Control XL into a USB2 or USB3 port
on your computer. The device will be automatically recognized by your
operating system and will appear in any of the lists of possible MIDI
ports in Ardour.

To connect the Launch Control XL to Ardour, open the [Preferences]{.kbd
.window} dialog, and then click [Control Surfaces]{.kbd}. Tick the
[Enable]{.kbd .option} checkbox opposite to \"Novation Launch Control
XL\" to activate Ardour\'s Launch Control XL support.

Once the device is activated, click [Show Protocol Settings]{.kbd} and
in the newly opened window select the device in the drop-down lists for
incoming and outgoing MIDI events.

Once you select the input and output port, the Launch Control XL will be
ready to use. You only need do this once: once these ports are connected
and your session has been saved, the connections will be made
automatically in this and other future sessions.

## Behavior and Configuration

The Launch Control XL was designed for use with Ableton Live, so it has
a Mix mode for controlling the mixer and a Device mode for controlling
various devices. Therefore, For Ardour, only a subset of features is
available out of the box. The vast majority of supported features are
not configurable, the user interface exposes only one setting: making
the 8th fader control the master bus.

Features supported out of the box are:

|                             |                                                                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Faders                      | Control faders of 8 tracks at the same time                                                                                                   |
| Track selection             | In the Mix mode, these buttons shifts the track focus by one track allowing to control e.g. track 2..9 or 3..10 rather than the default 1..8. |
| [Mute]{.kbd .button} button | Switches the Track Control row of buttons to toggle the *mute* status of tracks                                                               |
| [Solo]{.kbd .button} button | Switches the Track Control row of buttons to toggle the *solo* status of tracks                                                               |
| [Arm]{.kbd .button} button  | Switches the Track Control row of buttons to toggle the *record-arm* status of tracks                                                         |
