# Other Toolbar Items
## Plugin Delay Compensation
{#latency-compensation-info}

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/latency-compensation-info.png"
alt="The Latency Compensation Info" />
<figcaption>Latency Compensation Info</figcaption>
</figure>

This section shows information about the latency compensation Ardour
sets to align all signals in time whatever their route (and processing
applied).

The only button [Disable PDC]{.kbd .menu} allows to enable/disable the
*P*lugin *D*elay *C*ompensation. Enabling it will make all signal
perfectly aligned, while disabling it will reduce the delay, at the
expense of slightly misaligned signals for tracks that have plugins
introducing latency.

The two infos are:

-   the maxium reported latency by a plugin chain (worst route latency)
-   the I/O latency, i.e. how long does it take for a signal arriving at
    any physical input to be played back again.

## The Cue Options
{#cue_options}

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/cue_options.png" alt="The Cue options" />
<figcaption>The cue options</figcaption>
</figure>

Those two buttons control how Ardour deals with cue markers:

-   [Rec Cues]{.dfn}: when enabled, every time you click on a cue in the
    Cue window during playback, Ardour will insert the correspinding cue
    marker at the current playhead position. Only use it when
    programming cue sequences to align with timeline content.
-   [Play Cues]{.dfn}: when enabled, Ardour will play the corresponding
    cue every time the playhead passes its cue marker. This option is
    useful to be on by default.

## The Master Level Meter
{#tb_master_level_meter}

![The Master Level Meter](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/master-level-meter.png)

The global meter shows the levels of the master\'s output. Its the same
meter that sits in the [Master\'s Mixer strip](@@master-bus-strip), and
also shows a peak indicator, that turns red when any level exceeds 0dB.
It can be reset by a [Left]{.kbd .mouse} click.

## The Monitor Section Info
{#monitor_section_info}

![Monitor Section Info](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/monitor-section-info.png)

This section is only useful and active if the session has a [Monitor
section](@@monitor-section). The three buttons are exactly linked to
their counterparts in the Monitor slice of the mixer, but as they sit in
the toolbar, remain visible even in Editor mode.

The three buttons are:

-   [Mono]{.dfn}: sums all of the paths to a single mono signal and
    applies it to all Monitor Section outputs.
-   [Dim All]{.dfn}: Reduces overall monitor level by the amount set
    with the Dim level control.
-   [Mute All]{.dfn}: Mutes all monitoring.

## The Status Indicators
{#status_indicators}

![The Status buttons](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/status_buttons.png)

The [Status]{.dfn} buttons show the current session state:

|          |                                                                                                                                                                                                                              |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Solo     | Blinks when one or more tracks are being soloed, see [Muting and Soloing](@@muting-and-soloing). Clicking this button disables any active explicit and implicit solo on all tracks and busses.                               |
| Audition | Blinks when some audio is auditioned, e.g. by using the import dialog, or using the [Audition]{.kbd .menu} context menu in the [Regions List](@@the-region-list). Clicking this button stops the auditioning.                |
| Feedback | Blinks when Ardour detects a [feedback loop]{.dfn}, which happens when the output of an audio signal chain is plugged back to its input. This is probably not wanted and can be dangerous for the hardware and the listener. |

## Script/Shortcut buttons
{#tb_script_buttons}

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/script-buttons.png" alt="The Script buttons" />
<figcaption>The script / shortcuts buttons</figcaption>
</figure>

The buttons in between the Mode Selector and the Master Level Meter are
script or shortcuts buttons, which are user-definable buttons to attach
any session [lua-script](@@lua-scripting) to, or any action shortcut
(e.g. for tasks that are used often and buried deep inside nested
menus).

The number of buttons (precisely, the number of columns of two buttons)
can be set in the
[Preferences](@@preferences#preferences-appearance-toolbar).

[Left]{.kbd .mouse}-clicking an affected button launches the script or
shortcut, while [right]{.kbd .mouse}-clicking or clicking an unaffected
button allows change the script/shortcut the button should execute.

## Pane controls
{#appbar-pane-controls}

![Pane controls](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/pane-controls.png)

These buttons control the visibility of panes in Ardour windows:

-   The right sidebar (Editor list) and the bottom pane in the Editor
    window
-   The bottom pane and the right sidebar (Cue list) in the Cue window
-   The left sidebar in the Mixer window

The Recorder window currrently has no panes to control.

## The Mode Selector
{#mode_selector}

![The Mode Selector](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/mode_selector.png)

The Mode Selector allows switching between the Editor, Mixer, Cue, and
Recording windows. If a window is detached, the corresponding button is
lit. Clicking the button switches the detached window visibility.
