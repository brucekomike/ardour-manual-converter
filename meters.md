# Metering in Ardour
## Introduction

An engineer reading and using audio level meters compares to a musician
reading or writing sheet-music. Just like there are virtuoso musicians
who can\'t read a single note, there are great sound-engineers who just
go by their ears and produce great mixes and masters without ever
looking at a single meter.

Yet, in order to work in or with the broadcast industry, it is usually
unavoidable to use meters.

Audio level meters are very powerful tools that are useful in every part
of the entire production chain:

-   When tracking, meters are used to ensure that the input signal does
    not [overload]{.dfn} and maintains reasonable [headroom]{.dfn}.
-   Meters offer a [quick visual indication]{.dfn} of an activity when
    working with a large number of tracks.
-   During mixing, meters provide an rough estimate of the
    [loudness]{.dfn} of each track.
-   At the mastering stage, meters are used to check compliance with
    upstream [level]{.dfn} and [loudness standards]{.dfn} and to
    optimize the [loudness range]{.dfn} for a given medium.

## Meter Types

A general treatise on metering is beyond the scope of this manual. It is
a complex subject with a history... For background information and
further reading we recommend:

-   [How To Make Better Recordings in the 21st Century---An Integrated
    Approach to Metering, Monitoring, and Leveling
    Practices](http://www.digido.com/how-to-make-better-recordings-part-2.html)
    by Bob Katz. Has a good historic overview of meters and motivates
    the K-meter
-   [Wikipedia: Peak programme
    meter](https://en.wikipedia.org/wiki/Peak_programme_meter#Table_of_characteristics)---overview
    of meter types.
-   \"Audio Metering: Measurements, Standards and Practice\", by Eddy
    Brixen. ISBN: 0240814673
-   \"Art of Digital Audio\", by John Watkinson. ISBN: 0240515870

There are different metering standards, most of which are available in
Ardour. In short:

```{eval-rst}
+-----------------------------------+-----------------------------------+
| Digital peak-meter                | A [Digital Peak Meter]{.dfn}      |
|                                   | displays the absolute maximum     |
|                                   | signal of the raw audio PCM       |
|                                   | signal (for a given time). It is  |
|                                   | commonly used when tracking to    |
|                                   | make sure the recorded audio      |
|                                   | never clips. To that end, DPMs    |
|                                   | are always calibrated to 0 dBFS,  |
|                                   | or the maximum level that can be  |
|                                   | represented digitally in a given  |
|                                   | system. This value has no musical |
|                                   | reason whatsoever and depends     |
|                                   | only on the properties of the     |
|                                   | signal chain or target medium.    |
|                                   | There are conventions for         |
|                                   | [fall-off-time]{.dfn} and         |
|                                   | [peak-hold]{.dfn}, but no exact   |
|                                   | specifications.                   |
|                                   |                                   |
|                                   | Various conventions for DPM       |
|                                   | fall-off times and dBFS line-up   |
|                                   | level can be chosen in [Edit \>   |
|                                   | Preferences \> Metering]{.kbd     |
|                                   | .menu}.                           |
+-----------------------------------+-----------------------------------+
| RMS meters                        | An [RMS-type meter]{.dfn} is an   |
|                                   | averaging meter that looks at the |
|                                   | energy in the signal. It provides |
|                                   | a general indication of loudness  |
|                                   | as perceived by humans. Ardour    |
|                                   | features three RMS meters, all of |
|                                   | which offer additional peak       |
|                                   | indication.                       |
|                                   |                                   |
|                                   | -   [K20]{.dfn}: A meter          |
|                                   |     according to the K-system     |
|                                   |     introduced by Bob Katz, scale |
|                                   |     aligned to -20 dBFS,          |
|                                   |     rise/fall times and color     |
|                                   |     schema according to spec.     |
|                                   | -   [K14]{.dfn}: Same as K20 with |
|                                   |     scale aligned to -14 dBFS.    |
|                                   | -   [K12]{.dfn}: Same as K20 with |
|                                   |     scale aligned to -12 dBFS     |
|                                   |     (since 3.5.143).              |
|                                   | -   [Peak + RMS]{.dfn}: standard  |
|                                   |     RMS, customizable via [Edit   |
|                                   |     \> Preferences \>             |
|                                   |     Metering]{.kbd .menu}         |
+-----------------------------------+-----------------------------------+
| IEC PPMs                          | [IEC-type PPMs]{.dfn} are a mix   |
|                                   | between DPMs and RMS meters,      |
|                                   | created mainly for the purpose of |
|                                   | interoperability. Many national   |
|                                   | and institutional varieties exist |
|                                   | (EBU, BBC, DIN).                  |
|                                   |                                   |
|                                   | These loudness and metering       |
|                                   | standards provide a common point  |
|                                   | of reference which is used by     |
|                                   | broadcasters in particular so     |
|                                   | that the interchange of material  |
|                                   | is uniform across their sphere of |
|                                   | influence, regardless of the      |
|                                   | equipment used to play it back.   |
|                                   |                                   |
|                                   | For home recording, there is no   |
|                                   | real need for this level of       |
|                                   | interoperability, and these       |
|                                   | meters are only strictly required |
|                                   | when working in or with the       |
|                                   | broadcast industry. However,      |
|                                   | IEC-type meters have certain      |
|                                   | characteristics (rise-time,       |
|                                   | ballistics) that make them useful |
|                                   | outside the context of broadcast. |
|                                   |                                   |
|                                   | Their specification is very       |
|                                   | exact, and consequently, there    |
|                                   | are no customizable parameters.   |
+-----------------------------------+-----------------------------------+
| VU meters                         | [VU meters]{.dfn} are the         |
|                                   | dinosaurs (1939) amongst the      |
|                                   | meters. They react very slowly,   |
|                                   | averaging out peaks. Their        |
|                                   | specification is very strict      |
|                                   | (300ms rise-time, 1--1.5%         |
|                                   | overshoot, flat frequency         |
|                                   | response). Ardour\'s VU meter     |
|                                   | adheres to that spec, but for     |
|                                   | visual consistency it is          |
|                                   | displayed as a bar-graph rather   |
|                                   | than needle-style (more below).   |
+-----------------------------------+-----------------------------------+
```

## Ardour Specifics

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/mixer-meter-context-menu.png"
alt="mixer strip meter context menu" />
<figcaption>Mixer strip meter context menu</figcaption>
</figure>

Meters are available in various places in Ardour:

-   The mixer window features fixed height meters for each [channel
    strip]{.dfn}.
-   There are small (narrow) meters on each [track-header]{.dfn} in the
    editor window.
-   There are variable height meters in the [meterbridge window]{.dfn}.
-   Optionally, a fixed-size [master meter]{.dfn} can be displayed in
    the main toolbar.
-   Various other locations ([file import]{.dfn}, [sends]{.dfn}) have
    level-meters.

They all share the same configuration and color-theme which is available
in preferences and the theme-manager. Settings for the Peak and RMS+Peak
meters as well as VU meter standards are found in [Edit \> Preferences
\> Metering]{.kbd .menu}.

The type of meter and the [metering point]{.dfn} (the place in the
signal chain where the meter taps the signal) are configurable in the
context menu of each meter. Depending on the [Edit \> Preferences \>
Mixer]{.kbd .menu} settings, the metering point is also accessible via a
button in each Mixer strip.

Regardless of meter type and standard the meter display will highlight
red if the signal on the given channel exceeds the configured peak
threshold.

[Left]{.kbd .mouse} clicking on the peak-indicator button resets the
[peak-hold indicator]{.dfn} of a single channel.\
[Left]{.kbd .mod1 .mouse} clicking resets a whole [group]{.dfn}, and\
[Left]{.kbd .mod13 .mouse} clicking resets all meters.

## Overview of meter types

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/meter-types-18.png" class="mini"
alt="Bar-graph meters in Ardour" />
<figcaption aria-hidden="true">Bar-graph meters in Ardour</figcaption>
</figure>

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/needle-meters-18.png" class="mini"
alt="Needle-style meters as external LV2 plugins" />
<figcaption aria-hidden="true">Needle-style meters as external LV2
plugins</figcaption>
</figure>

The figure on the left shows all available meter-types in Ardour when
fed with a -18 dBFS 1 kHz sine wave.

Due to layout concerns and consistent look and feel all meters available
in Ardour itself are bar-graph type meters. Corresponding needle-style
meters---which take up more visual screen space---are available as LV2
plugins (see image on the right):
[meters.lv2](https://github.com/x42/meters.lv2/).
