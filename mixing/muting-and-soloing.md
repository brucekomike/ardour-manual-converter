# Muting and Soloing
Each track and bus has two buttons which have important implications for
signal flow: [mute]{.dfn} and [solo]{.dfn}. The behaviour of these
buttons is configurable in Ardour, to suit different studio set-ups.

## Without a monitor bus

When using Ardour without a monitor bus, there is only one way in which
mute and solo will work:

-   Mute on a track or bus will mute that track on the master bus, so
    that it will not be heard.
-   Solo on a track or bus will solo that track or bus and mute all
    others. Soloing a bus will also solo any tracks or busses which feed
    that bus.

The Solo status indicator button in the Toolbar blinks when one or more
tracks are being soloed. Clicking this button disables any active
explicit and implicit solo on all tracks and busses.

## With a monitor bus

For setups with a monitor bus, more options are available, mostly
governed by the setting of the [Solo controls are Listen controls]{.kbd
.option} option in [Edit \> Preferences \> Monitoring.]{.kbd .menu}

With [Solo controls are Listen controls]{.kbd .optoff} unticked,
behaviour is almost exactly the same as the situation without a monitor
bus. Mute and solo behave the same, and the monitor bus is fed from the
master bus, so it sees the same thing.

With [Solo controls are Listen controls]{.kbd .option} ticked, the
master and monitor busses behave differently. In this mode, solo
controls are more properly called [listen]{.dfn} controls, and Ardour\'s
solo buttons will change their legend from [S]{.kbd .menu} for Solo to
show the listening point, either [A]{.kbd .menu} for After fader or
[P]{.kbd .menu} for Pre fader.

Now, without any mute or listen, the monitor bus remains fed by the
master bus. Also:

-   Mute will mute the track or bus, so that it will not be heard
    anywhere (neither on the master nor monitor busses), much as before.
-   Listen will disconnect the monitor bus from the master bus, so that
    the monitor bus now only receives things that are \"listened to\".
    Listen will not perform any muting, and hence the master bus will
    not be affected by a listened track or bus.

When solo controls are listen controls, the listening point can be set
to either After-Fade Listen (AFL) or Pre-Fade Listen (PFL). The precise
point to get the signal from can further be configured using the [PFL
signals come from]{.kbd .menu} and [AFL signals come from]{.kbd .menu}
options.

The solo-mute arrangement with a monitor bus is shown below:

<figure class="center">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/solo-mute.png" alt="mute/solo signal flow" />
<figcaption>Mute/solo signal flow</figcaption>
</figure>

Here we have a number of tracks or busses (in orange). Each one has an
output which feeds the master bus. In addition, each has PFL and AFL
outputs; we have a choice of which to use. PFL/AFL from each track or
bus are mixed. Then, whenever anything is set to AFL/PFL, the monitor
out becomes just those AFL/PFL feeds; the rest of the time, the monitor
out is fed from the master bus.

In this scheme Solo has no effect other than to mute other non-soloed
tracks; with solo (rather than listen), the monitor out is fed from the
master bus.

## Other solo options

[Edit \> Preferences \> Monitoring]{.kbd .menu} has some more solo
options:

### Solo-in-place mute cut

When using solo-in-place (SiP), in other words when soloed tracks are
being listened to on the master bus, this fader specifies the gain that
will be applied to other tracks in order to mute them. Setting this
level to −∞ dB will mean that other tracks will not be heard at all;
setting to some higher value less than 0dB means that other non-soloed
tracks will be heard, just reduced in volume compared to the soloed
tracks. Using a value larger than −∞ dB is sometimes called
\"Solo-In-Front\" by other DAWs, because the listener has the sense that
soloed material is \"in front\" of other material. In Ardour, this is
not a distinct mode, but instead the mute cut control offers any level
of \"in-front-ness\" that is desired.

### Exclusive solo

If this is enabled, only one track or bus will ever be soloed at once;
soloing track B while track A is currently soloed will un-solo track A
before soloing track B.

### Show solo muting

If this is enabled, the mute button of tracks and busses will be drawn
outlined to indicate that the track or bus is muted because something
else is soloed. This is enabled by default, and it is recommended to
leave it that way unless extremely comfortable with Ardour\'s mute/solo
behaviour.

### Soloing overrides muting

If this is enabled, a track or bus that is both soloed and muted will
behave as if it is soloed.

### Mute affects...

These options dictate whether muting the track will affect various
routes out of the track; through the sends, through the control outputs
(to the monitor bus) and to the main outputs.
