# Loudness Analyzer and Normalizer
The *Loudness Analyzer and Normalizer* tool is useful at the end of the
mixing process to make the final audio file comply with different specs
regarding loudness.

This is a rather advanced mode. When using the *Loudness Analyzer &
Normalizer* (or [LAN]{.dfn}), one has to make sure than normalization is
disabled when exporting.\
\
In general, it is recommended to just use [automatic export
normalization](@@export-format-profiles), in the [Export
dialog](@@export-dialog). This can also produce results for multiple
targets at the same time.

It is enabled by checking [Enable master-bus output gain control]{.kbd
.option} in the [Preferences](@@preferences#preferences-signal_flow).
The [Master Bus strip](@@master-bus-strip) then shows a [LAN]{.kbd
.menu} button to start the analysis, and a volume slider that is the
global gain that can be set either manually or by the loudness
normalizer.

The LAN can also be started from the [Session \> Loudness
assistant...]{.kbd .menu} menu. If the option above is not enabled,
Ardour will link to the relevant page of the Preferences.

Either method show the following window:

![The Loudness Analyzer realtime
selector](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/pre_loudness.png){width="50%"}

This window allows to start the loudness analysis. A choice is offered
between freewheeling (i.e. Ardour renders the session as fast as
possible to measure the loudness), by default, or Realtime, for cases
where freewheeling would not accurately render the session, e.g. if a
hardware or JACK effect is used in the session, by clicking on the
[Realtime]{.kbd .menu} toggle button.

After the analysis is over, the Loudness Analyzer and Normalizer is
shown:

![The Loudness Analyzer and
Normalizer](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/loudness_analyzer.png){width="75%"}

## The Loudness Graph
{#loudness-graph}

At the top of the window, a loudness graph visually represents the
analysis. The x-axis represents the time, and the y-axis represents the
perceived loudness in LUFS:

-   [Integrated loudness]{style="color:green;"} averaging the loudness
    on the whole session
-   [Short loudness]{style="color:red;"} using a sliding time window of
    3 seconds
-   [Momentary loudness]{style="color:blue;"} using a sliding time
    window of 400 ms.

## Normalization Parameters

As loudness is a perceived sonic energy, and depends on the level,
frequency, duration and nature of the sound, this window allows to base
the calculation of the loudness normalization on different parameters :

-   [Peak :]{.dfn} is the highest signal level value
-   [True Peak :]{.dfn} is the highest signal level value where the
    signal has been oversampled to figure out more in-between values
    between the samples (interpolation)
-   [Integrated Loudness :]{.dfn} is the loudness computed from the
    whole session or range
-   [Max Short Loudness :]{.dfn} is the maximum loudness computed on
    short time ranges (3 seconds)
-   [Max Momentary Loudness :]{.dfn} is the maximum momentary loudness

Any combination of these parameters can be taken into account when
determining the gain normalization, by checking its momentary button,
and setting a *Target* value.

Ardour shows both the *Measured* value of the parameters, and the
*Delta* value, i.e. the difference between the *Target* and *Measured*
values, hence the gain correction.

The maximum *Delta* value is the Gain correction to apply to fit all the
Target values.

Ardour shows, under the parameters, a summary of the calculation :

-   [Gain to normalize:]{.dfn} is the max *Delta* value
-   [Previous output gain:]{.dfn} is the current Master track gain
-   [Total Gain:]{.dfn} is the difference between these two values,
    hence the correction to apply

## Presets

A selection of presets is offered to simplify the normalization. These
presets apply the relevant parameters and their target values. Below is
a table of these presets:

| Parameter name: | dbFS  | dBTP  | LUFS  | short | mom.  | FS  | TP   | int | sht | mom | maxIntg | notes  |
|-----------------|-------|-------|-------|-------|-------|-----|------|-----|-----|-----|---------|--------|
| EBU R128        | false | true  | true  | false | false | 0   | -1.0 | -23 | 0   | 0   | -22.5   | -23.5  |
| EBU R128 S1     | false | true  | true  | true  | false | 0   | -1.0 | -23 | -18 | 0   | -22.5   | -23.5  |
| ATSC A/85       | false | true  | true  | true  | false | 0   | -2.0 | -24 | 0   | 0   | -22.0   | -26.0  |
| AES Streaming   | false | true  | true  | false | false | 0   | -1.0 | -18 | 0   | 0   | -16.0   | -20.0  |
| ASWG-R001 HOME  | false | true  | true  | true  | false | 0   | -1.0 | -24 | 0   | 0   | -22.0   | -26.0  |
| Digital Peak    | true  | false | false | false | false | 0   | 0.0  | 0   | 0   | 0   | 0.0     | -200.0 |
| CD/DVD          | true  | true  | true  | false | false | 0   | -0.1 | -9  | 0   | 0   | 0.0     | -200.0 |
| Amazon Music    | false | true  | true  | false | false | 0   | -2.0 | -14 | 0   | 0   | -9.0    | -19.0  |
| Apple Music     | false | true  | true  | false | false | 0   | -1.0 | -16 | 0   | 0   | -15.0   | -17.0  |
| Deezer          | false | true  | true  | false | false | 0   | -1.0 | -15 | 0   | 0   | -14.0   | -16.0  |
| Soundcloud      | false | true  | true  | false | false | 0   | -1.0 | -10 | 0   | 0   | -8.0    | -13.0  |
| Spotify         | false | true  | true  | false | false | 0   | -1.0 | -14 | 0   | 0   | -8.0    | -20.0  |
| Spotify Loud    | false | true  | true  | false | false | 0   | -2.0 | -11 | 0   | 0   | -5.0    | -17.0  |
| Youtube         | false | true  | true  | false | false | 0   | -1.0 | -14 | 0   | 0   | -13.0   | -15.0  |

New presets can be created at will and saved/removed using the
[Save]{.kbd} and [Remove]{.kbd} buttons next to the preset choice. The
Standard presets listed above can not be removed or edited.

The [Analysis Report]{.kbd} button allows to visually represent the
analysis with a graph in a very similar window to the one in the
Post-[Export](@@export-dialog) analysis.

![The loudness report](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/export-loudness-report.png){width="75%"}

## The Conformity Analysis Panel
{#conformity-analysis-panel}

At the lower right end of the window is a *Conformity Analysis* info
panel indicating, for each of the presets above, if the corrected gain
would fit the required values:

-   [✖]{style="color:red;"}: the signal is too loud
-   [✔]{style="color:orange;"}: the signal is too quiet, but satisfies
    the max. loudness spec
-   [✔]{style="color:green;"}: signal loudness is within the spec.

Lastly, the gain correction is, by default, applied after all the
processors of the master bus. This can also be changed, either by
checking the [Custom Amplifier Position]{.kbd} temporaty button in this
window, or in the Master strip, by [Right]{.kbd .mouse}-clicking the
gain slider and checking [Custom LAN Amp Position]{.kbd .option}. The
gain normalizer then becomes a processor in the processors box of the
Master strip, that can be moved as needed like any processor/effect.
