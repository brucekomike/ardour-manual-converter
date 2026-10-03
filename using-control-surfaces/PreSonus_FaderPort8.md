# Using the PreSonus FaderPort 2/8/16
Ardour supports a variety of controllers in the [Presonus
FaderPort](https://www.presonus.com/products/Controllers){rel="external"}
product line. The documentation below is written with FaderPort™ 8 in
mind. However, it equally applies to FaderPort 2 and FaderPort 16 as the
main difference between these units is the amount of motorized faders.
For the documentation on using 1st generation FaderPort devices please
refer to [this chapter](@@using-the-presonus-faderport) instead.

## Connecting the FaderPort 8

The FaderPort 8 (FP8) comes with a USB socket on the back. Connect a
suitable USB cable from there to a USB port on your computer. The FP8
will be automatically recognized by your operating system, and will
appear in any of the lists of possible MIDI ports in both Ardour and
other similar software.

Ardour uses the FaderPort 8 in what PreSonus calls \"Studio One\" or
\"native\" mode. To use the FaderPort8 with Ardour\'s FP8 Control
Surface, make sure that the device is in \"Studio One\" mode. (If you
would like to change the mode at any point, power on the unit while
holding down the two leftmost Select buttons, see the FaderPort 8 manual
for further details. Also note that at least firmware version 1.01 is
required. NB. \"factory default\" resets the firmware, see the PreSonus
FaderPort8 Owner\'s manual chapter 9.4.)\
While the FaderPort provides a Mackie Control Universal (MCU) mode,
which works with Ardour\'s Mackie Control Surface, MCU does not support
various elements available on the FP8 (e.g. colored buttons, and the
custom mode scribble strips).

Normally, Ardour should be able to automatically detect a connected
Faderport 8 device and enable it. If it fails, open the Preferences
dialog, select \"Control Surfaces\" and enable \"PreSonus FaderPort 8\".
Then open the \"Protocol Settings\" dialog for the FP8. Which (among
other things) allows to select the the MIDI ports corresponding to the
FP8.

Once you select the input and output port, Ardour will initialize the
FP8 and it will be ready to use. You only need do this once: Once these
ports are connected and your session has been saved, the connections
will be made automatically in this and other future sessions.

<figure class="center">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/fp8_settings.png" width="621"
alt="FaderPort8 Control Surface Settings Dialog" />
<figcaption aria-hidden="true">FaderPort8 Control Surface Settings
Dialog</figcaption>
</figure>

## Using the FaderPort 8

The FaderPort\'s controls can be divided into five groups:

-   Transport buttons
-   Session Navigation controls
-   Fader modes
-   Mix management
-   Channel strip

In general the control mapping described in the FaderPort 8 Owner\'s
Manual for Studio One (chapter 2) applies to Ardour as well. There are
however subtle differences where the DAWs differ.

Buttons generally act on release (not press), with exception of
transport-control (since 6.0pre) and individual exceptions mentioned
below.

### Transport Buttons

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/fp8_transport.svg"
alt="FaderPort8 Transport Buttons" />
<figcaption aria-hidden="true">FaderPort8 Transport Buttons</figcaption>
</figure>

1.  [Stop]{.kbd .def}: Stops the transport. Press twice to return to
    session start.
2.  [Loop]{.kbd .def}: Toggles loop playback. A loop-range needs to be
    defined in the session for looping to be engaged.
3.  [Play/Pause]{.kbd .def}: Roll/Stop the transport (note that Ardour
    has no \"pause\" mode: Pause is equivalent to stop). During
    vari-speed playback, pressing \"play\" resets to 100% forward speed.
4.  [Rewind]{.kbd .def}: Rewind, roll backwards. Successive presses or
    holding the button incrementally changes the speed.
5.  [Fast Forward]{.kbd .def}: Roll forward. Successive presses or
    holding the button accumulate speed. Pressing ([Rewind]{.kbd} and
    [Fast Forward]{.kbd}) simultaneously stops playback and returns the
    playhead to zero.
6.  [Record]{.kbd .def}: Toggles the global record enable setting.

### Session Navigation
{#session-navigation .clear}

Session Navigation allows quick navigation and provides access to
session-wide controls. Each of the eight buttons alters the function of
the push-button encoder and the [Prev]{.kbd}, [Next]{.kbd} buttons. With
exception of [Click]{.kbd} the seven modes are exclusive (radio
buttons).

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/fp8_navigation.svg"
alt="FaderPort8 Navigation Buttons" />
<figcaption aria-hidden="true">FaderPort8 Navigation
Buttons</figcaption>
</figure>

1.  [Channel]{.kbd .def}: The [Prev]{.kbd} / [Next]{.kbd} buttons select
    the previous/next mixer-strip. If no strip is selected, [Next]{.kbd}
    selects the first, [Prev]{.kbd} the last mixer-strip in the session.
    Pressing the encoder knob moves the most recently selected
    mixer-strip into view on the FP8. The encoder scrolls the
    editor-canvas up/down.
2.  [Master]{.kbd .def}: The encoder controls the master-bus level. If a
    session includes a monitor-section, the encoder controls monitor-out
    by default. Hold the [Shift]{.kbd} button to control the master-bus
    level. Press the encoder knob to reset the gain to 0dB. The
    [Prev]{.kbd} / [Next]{.kbd} navigation buttons bank the visible
    strips on the FP8 by one track left/right.
3.  [Zoom]{.kbd .def}: The encoder controls horizontal zoom of the
    editor. Press the encoder to *zoom to fit* the session. [Prev]{.kbd}
    / [Next]{.kbd} navigation buttons zoom selected track(s) vertically
    (or all tracks if none are selected).
4.  [Click]{.kbd .def}: Toggle the metronome on/off. While holding the
    [Click]{.kbd} button, the encoder modifies the volume of the
    metronome click (press the encoder while holding [Click]{.kbd} to
    reset the metronome level to 0dBFS).
5.  [Scroll]{.kbd .def}: The encoder scrolls the timeline (hold
    [Shift]{.kbd} for finer steps). Pressing the encoder *zooms to fit*
    the session. The [Prev]{.kbd} / [Next]{.kbd} navigation buttons bank
    the visible strips on the FP8 by one track left/right.
6.  [Section]{.kbd .def}: The [Prev]{.kbd} / [Next]{.kbd} navigation
    buttons nudge the selected region by the time configured in the
    nudge-clock. If no region is selected the playhead position is
    nudged. The encoder always nudges the playhead position.
7.  [Bank]{.kbd .def}: Encoder and navigation buttons scroll through
    mixer-strips in banks of eight. Pressing the encoder moves the most
    recently selected mixer-strip into view on the FP8.
8.  [Marker]{.kbd .def}: The encoder scrolls the timeline (hold
    [Shift]{.kbd} for finer steps). The [Prev]{.kbd} / [Next]{.kbd}
    navigation buttons jump to prev/next markers. Press the encoder to
    drop a new marker.

When combined with [Shift]{.kbd}, the eight buttons will access custom
functions, which can be configured in the Preference Dialog. The buttons
will light up if an action has been assigned to a button.

The following tables shows a condensed overview of the
session-navigation modes:

|                              | [Prev]{.kbd} / [Next]{.kbd}         | Encoder knob                        | Encoder Press                      |
|------------------------------|-------------------------------------|-------------------------------------|------------------------------------|
| Channel                      | Select prev/next mixer-strip        | Scroll Editor up/down               | Bank to show selected strip on FP8 |
| Master                       | Bank visible strips on FP8 by 1     | Adjust master/monitor level         | Reset master/monitor to 0dB        |
| Zoom                         | Vertical zoom (editor track-height) | Horizontal timeline zoom (time)     | Horizontal zoom to session         |
| Scroll                       | Bank visible strips on FP8 by 1     | Scroll the timeline (move playhead) | Horizontal zoom to session         |
| Section                      | Nudge the selected region           | Nudge the playhead                  | \-                                 |
| Bank                         | Bank visible strips on FP8 by 8     | Bank visible strips on FP8 by 1     | Bank to show selected strip on FP8 |
| Marker                       | Move to prev/next marker            | Scroll the timeline (move playhead) | Drop a new marker                  |
| Press and hold [Click]{.kbd} | (mode dependent)                    | Adjust metronome Level              | Reset metronome level to 0dBFS     |

### Shift Button
{#shift-button .clear}

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/fp8_shift_large.svg"
alt="The FaderPort8 Shift Button" />
<figcaption aria-hidden="true">The FaderPort8 Shift Button</figcaption>
</figure>

The two [Shift]{.kbd} buttons are identical, they\'re copied to provide
convenient access to the modifiers. Pressing and holding the
[Shift]{.kbd} button updates the lights (and colors on RGB buttons) to
indicate the modified control.\
Pressing and holding the [Shift]{.kbd} button for one second without
pressing any other button enters shift-lock mode. Press [Shift]{.kbd}
again to reset. The [Shift]{.kbd} button engages directly on press.
Activating an action while the button is held will void the shift-lock
mode.

### Fader Modes
{#fader-modes .clear}

The eight faders on the FP8 can be assigned to various automatable
controls present in the current session. The four fader-mode buttons
change the behavior of the mixer-strip and scribble strip displays.
(Note: with the 1.01 firmware these buttons always act on press.)

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/fp8_fadermode.svg"
alt="FaderPort8 Fader Mode Buttons" />
<figcaption aria-hidden="true">FaderPort8 Fader Mode
Buttons</figcaption>
</figure>

1.  [Track]{.kbd .def}: In Track-mode, the motorized faders display and
    control a mixer-strip\'s signal level. The Pan/Param encoder
    modifies the azimuth of the panner (hold [Shift]{.kbd} to control
    the width, if the track\'s panner supports it). [Mute]{.kbd} and
    [Solo]{.kbd} affect the respective mixer-strip.
2.  [Edit Plugins]{.kbd .def}: When Edit Plug-ins mode is active, the
    motorized faders will control the parameter settings of a given
    plugin-insert.\
    Press the [Edit Plugins]{.kbd} button to view all available
    plugin-inserts on a strip. If no plugins are available, [Edit
    Plugins]{.kbd} will not engage and the FP8 automatically switches
    back to Track-mode.\
    **Select Plugin Mode**: Use the [Select]{.kbd} buttons under the
    scribble strip to pick a plugin to edit.\
    The [Select]{.kbd} button color indicates the bypass/enable state of
    the plugin (red: bypassed, green: enabled). Use [Shift]{.kbd} +
    [Select]{.kbd} to toggle the bypass state.\
    Selecting a plugin enters **Parameter Edit Mode**: The faders and
    the [Select]{.kbd} buttons will respectively control the parameters
    and toggle controls of the selected plugin (once a plugin has been
    selected, it stays in edit mode regardless of track selection). If
    there are more than eight parameters, the Pan/Param encoder allows
    to scroll through available control-parameters (hold [Shift]{.kbd}
    to bank by 8).\
    If the plugin has any presets, pressing the Pan/Param encoder
    switches to the **plugin-preset display**: Plugin preset names are
    displayed on the scribble-displays, the [Select]{.kbd} button below
    each loads the preset. The \"Pan/Param\" encoder can be used to
    scroll through presets if there are more than seven (right-most,
    8th, slot is reserved to unload/clear a loaded preset, hold
    [Shift]{.kbd} to bank by 7). The [Select]{.kbd} button color is used
    to indicate the currently loaded preset (if any) and blinks if a
    parameter has been modified since loading the preset. Loading a
    preset or pressing the Pan/Param encoder again switches back to the
    Plugin Parameter Edit Mode.\
    In Parameter Edit Mode, the \"Open\" ([Shift]{.kbd} + [Macro]{.kbd})
    allows to toggle the Plugin GUI visibility.\
    Press the [Edit Plugins]{.kbd} button again to return to the Select
    Plugin Mode.
3.  [Sends]{.kbd .def}: In Sends mode, each of the faders is mapped to
    the send-level of aux-sends of the selected track. If there are more
    than eight sends on a given track, the Pan/Param encoder can scroll
    through them. Send-mode follow the selection. If there are no sends
    on a given track, the FP8 automatically switches back to Track-mode.
4.  [Pan]{.kbd .def}: When Pan mode is active, the motorized faders will
    display and control the panner\'s azimuth. The Pan/Param controls
    the pan-width of the selected mixer-strip.

[Shift]{.kbd} + [Track]{.kbd} toggles timecode display on/off (middle
row of the scribble-strip). The timecode format can be configured in the
Control Surface Preference Dialog (Timecode, musical-time:
bar/beat/tick).

### Channel Strip
{#channel-strip .clear}

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/fp8_strip.svg" height="500"
alt="The FaderPort8 Channel Strip" />
<figcaption aria-hidden="true">The FaderPort8 Channel Strip</figcaption>
</figure>

-   **Touch-Sensitive Fader**: The fader can be used to control volume
    levels, aux send levels, panning, or plugin parameters, depending on
    the fader-mode (see above).
-   **Pan/Param**: The encoder controls panning in Track and Pan mode.
    In Plugin and Send fader-modes, the encoder banks parameters. See
    Fader modes above for details. When \"Link\" is engaged, the encoder
    can control any automatable parameter (see Miscellaneous below).
-   [Mute]{.kbd .def}: Toggle the mute-control of the corresponding
    mixer-strip. Mute engages on press, and disengages on release. Press
    and hold the button for at least 0.5sec for momentary.
-   [Solo]{.kbd .def}: Toggle the solo or listen (AFL,PFL) control of
    the corresponding mixer-strip. Solo engages on press, and disengages
    on release. Press and hold the button for at least 500ms for
    momentary.
-   [Select]{.kbd .def}: In Track and Sends and Pan mode the Select
    button select/de-select a given mixer-strip.\
    Since selection is not limited to a single mixer-strip, the button
    acts in tri-state. A mixer-strip light indicates selection:
    -   **Any Selected Track**: The select button is lit with the
        track\'s color.
    -   **Any Not Selected Track**: The select button is off (dimly
        showing the track\'s color).
    -   **Most Recently Selected Track**: Only one track at a time. The
        select button blinks with the track\'s color.

    Operations such as [Edit Plugins]{.kbd} or [Sends]{.kbd} use the
    most-recently-selected (focused) track. To modify the selection, the
    button\'s action depends on the current selection:
    1.  **[Select]{.kbd}**: The track is exclusively selected and also
        becomes the most-recently selected.
    2.  **[Shift]{.kbd} + [Select]{.kbd} any selected track**: Deselect
        the track.
    3.  **[Shift]{.kbd} + [Select]{.kbd} any unselected track**: Adds
        the given track to the selection and make it most-recently
        selected).

While holding the [ARM]{.kbd} button the [Select]{.kbd} button lights
change to red and the [Select]{.kbd} buttons controls the record-arm of
the given track. Mixer-strips that cannot be record-armed have a dim
white light.

[Shift]{.kbd} + [ARM]{.kbd} record-arms all tracks in the session.

### Mix Management
{#mix-management .clear}

These buttons allows to select which mixer-strips are spilled on the FP8
channel-strips.

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/fp8_mixmanage.svg"
alt="FaderPort8 Mix Management Buttons" />
<figcaption aria-hidden="true">FaderPort8 Mix Management
Buttons</figcaption>
</figure>

1.  [Audio]{.kbd .def}: View Audio Tracks only.
2.  [VI]{.kbd .def}: Show tracks with virtual instrument plugins.
3.  [Bus]{.kbd .def}: Display only Busses.
4.  [VCA]{.kbd .def}: Show VCAs.
5.  [All]{.kbd .def}: Display all Tracks, Busses (incl master-bus) and
    VCAs.

In combination with the [Shift]{.kbd} modifier ten total filters are
available:

-   [Shift]{.kbd} + [Audio]{.kbd .def} **Inputs**: shows all
    record-armed tracks (Audio and MIDI).
-   [Shift]{.kbd} + [VI]{.kbd .def} **MIDI**: View all MIDI tracks.
-   [Shift]{.kbd} + [Bus]{.kbd .def} **Outputs**: Show the Master and
    Monitor Bus.
-   [Shift]{.kbd} + [VCA]{.kbd .def} **FX**: Shows Aux-Busess.
-   [Shift]{.kbd} + [All]{.kbd .def} **User**: Display all currently
    selected mixer-strips only.

### Automation Controls
{#automation-controls .clear}

The Automation Controls provide access to the currently selected
mixer-strips. The automation enable lights indicates the mode of the
most recently selected mixer-strip (blinking selection button). The
action affects all selected mixer-strips. The automation controls are
currently only available in [Track]{.kbd} and [Pan]{.kbd} fader modes
where they affect the fader and pan automation modes respectively.

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/fp8_automation.svg"
alt="FaderPort8 Automation Buttons" />
<figcaption aria-hidden="true">FaderPort8 Automation
Buttons</figcaption>
</figure>

1.  [Latch]{.kbd .def}: Currently not available in Ardour.
2.  [Trim]{.kbd .def}: Currently not available in Ardour.
3.  [Off]{.kbd .def}: Select \"Manual\" automation mode.
4.  [Read]{.kbd .def}: Select \"Play\" automation mode.
5.  [Write]{.kbd .def}: Select \"Write\" automation mode (note at the
    end of a write pass, Ardour automatically puts the track into
    \"Touch\" mode.
6.  [Touch]{.kbd .def} Select \"Touch\" automation mode.

The Automation Controls also double as session state controls when
combined with [Shift]{.kbd}.

1.  [Shift]{.kbd} + [Latch]{.kbd .def} **Save**: Save the session. The
    button lights up red if the session is modified.
2.  [Shift]{.kbd} + [Trim]{.kbd .def} **Redo**: Redo a previously undone
    operation. The button lights up green if redo is possible.
3.  [Shift]{.kbd} + [Off]{.kbd .def} **Undo**: Undo the most recent
    operation. The button lights up green if undo is possible.

With [Shift]{.kbd}, the bottom row allows to bind three custom user
actions.

### Miscellaneous
{#miscellaneous .clear}

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/fp8_misc.svg" alt="FaderPort8 Misc Buttons" />
<figcaption aria-hidden="true">FaderPort8 Misc Buttons</figcaption>
</figure>

-   [Solo Clear]{.kbd .def}: Reset all solo controls in the session. If
    the FP8 was used to clear solo-state, pressing the button again will
    restore the previous state (unless solo state was modified manually
    since).
-   [Mute Clear]{.kbd .def}: Unmute all mixer-strips in the session. If
    the FP8 was used to clear mute-state, pressing the button again will
    restore the previous mute state (unless mute-state was changed
    manually since).
-   [Bypass]{.kbd .def}: The behavior depends on the edit-mode:
    -   **Track + Pan Mode**: A/B bypass toggle any plugins on all
        selected mixer-strips.
    -   **Edit Plugin Parameter**: Toggle bypass of of the plugin that
        is currently being edited. Bypass state is indicated by color:
        red for bypassed, green for enabled (not bypassed).
-   [Shift]{.kbd} + [Bypass]{.kbd .def} **Bypass All**: A/B bypass
    toggle any plugins on all selected mixer-strips.

```{=html}
<!-- -->
```
-   [Macro]{.kbd .def}: Toggle Editor and Mixer Windows/Tabs.
-   [Shift]{.kbd} + [Macro]{.kbd .def} **Open**: The behavior depends on
    the edit-mode:
    -   **Edit Plugin Parameter**: Toggle Plugin GUI visibility (if it
        has a GUI) of the plugin that is currently being edited.
    -   **all other modes**: Show the Import Audio Dialog.
-   [Link]{.kbd .def}: Activate Control-Link Mode (only available in
    Track and Pan modes).\
    The Pan/Param encoder controls the element over which the
    mouse-cursor hovers in the GUI. One can access any parameter which
    can be automated.\
    Pressing the Pan/Param encoder resets the control-parameter to the
    default value.\
    The buttons color is used to indicate the link-state:
    -   **orange**: Link is enabled, but the mouse-cursor is not over an
        element which can be controlled.
    -   **yellow**: Link is enabled, and the cursor is hovering over a
        controllable element.
    -   **green**: Link is locked to a given element (see below).
    -   **turquoise**: Link lock is possible (when pressing
        [Shift]{.kbd} while link-mode is enabled).
    -   **red**: Link-lock is not possible (only when pressing
        [Shift]{.kbd} while link-mode is enabled without a valid element
        to control.
-   [Shift]{.kbd} + [Link]{.kbd .def} **Lock**: When in Link-mode (see
    above), this allows to lock the current control to the Pan/Param
    encoder. Link will no longer follow the GUI mouse-cursor.\
    If Link-mode is not enabled, Lock, locks the GUI (alike Session \>
    Lock) to prevent accidental changes.

Link and Link-Lock mode will automatically disengage when entering
[Sends]{.kbd} or [Edit Plugins]{.kbd} mode.

### Harrison Mixbus
{#harrison-mixbus .clear}

The above also applies to Ardour-derivatives Harrison-Mixbus and Mixbus
32C with a few subtle differences:

-   Mix Management **Bus** shows Mixbusses only, while **FX** spills
    Aux-busses.
-   The Mixbus built-in EQ and Compressor are present on every track and
    bus and always available. They are displayed as special plugins on
    right-side in **Select Plugin Mode**. When editing those processors,
    the parameters follows track selection (for other plugins this is
    not possible since they may not be present).
-   Fader mode **Sends** shows mixbus-assigns first (before any optional
    aux-sends). The master-bus-assign is available on the \"S\"olo
    button of the right-most strip.
