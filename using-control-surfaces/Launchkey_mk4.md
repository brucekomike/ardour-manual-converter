# Using the Novation Launchkey mk4
Novation Launchkey mk4 series was introduced in August 2024 and has been
supported in Ardour since v8.7, with the minor exception for Linux-based
distributions running any v6.x version of the kernel.

There are currently 6 devices in the series:

-   Launchkey Mini 25 and 37 have 16 pads, 8 encoders, no faders, and
    only 2 transport controls.
-   Launchkey 25 and 37 have 16 pads, 8 encoders, no faders, all
    transport controls.
-   Launchkey 49 and 61 have 16 pads, 8 encoders, 9 faders, 9 track
    buttons, all transport controls.

This documentation covers the full set of features that is only
available in Launchkey 49 and 61. It partially applies to junior models
in the series. Please refer to the Launchkey user manual for specifics
on operating your controller.

![Novation Launchkey mk4
61](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/novation-launchkey-mk4-61.svg){.invert-in-dark
style="width:75%;"}

## Configuration

All configuration of the devices is expected to be done in Novation
Components. Thus in Ardour, you can only select ports for incoming and
outgoing MIDI messages.

## General behavior

Ardour ships with a number of hardcoded mappings between hardware
controls and the DAW\'s features:

-   **Track selection**: you can press left-pointing and right-pointing
    buttons to select the previous or the next track.
-   **Faders**: 8 faders are mapped to the first 8 tracks, 1 fader (on
    the right) is mapped either to the monitor (if the monitor section
    exists) or to the master bus (if there is no monitor section).
-   **Basic transport controls**: rolling, stopping, toggling rec-mode.
-   **Workflow buttons**: Undo/Redo (Shift+Undo), Metronome toggle.
    Capture MIDI is not a function available in Ardour, thus there is no
    mapping for it.

## Encoder modes

Launchkey mk4 controllers come with 4 predefined encoder modes and 4
custom modes. To switch to a particular mode, press and hold the
[Shift]{.kbd .button} button and then press the corresponding pad.

|           |                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------|
| Plugin    | Encoders control plugin parameters.                                                                 |
| Mixer     | Encoders can be used for pan, the first 2 sends, and additional gain controls; pads do solo & mute. |
| Sends     | Encoders control 8 sends of the selected track.                                                     |
| Transport | Encoders control playhead, loop points, can be used to jump between markers, visual zoom.           |

## Pad modes

Launchkey mk4 controllers come with 4 predefined pad modes and 4 custom
modes. To switch to a particular mode, press and hold the [Shift]{.kbd
.button} button and then press the corresponding pad.

Ardour only requires predefined mappings for the DAW pad mode. In that
case pads function to control 2 scenes/cues of 8 tracks. See the [Cue
support](#cue-support) section below for more details.

Additional modes --- Drum, User Chord, Arp Patterns --- do not require
DAW involvement. All MIDI processing happens inside the box, the
keyboard only sends final MIDI events to the output.

## Cue support

In the DAW mode, the 2 by 8 pads matrix represents 2 cues in 8 tracks.
You can use arrow up/down buttons to scroll up and down the cues.
Pressing pads will toggle playback of individual clips in trigger slots.
The arrow-right button will trigger an entire cue.
