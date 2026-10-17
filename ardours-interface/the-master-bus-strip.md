# Master Bus Strip
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/master-strip.png"
alt="The Master strip in the mixer" />
<figcaption aria-hidden="true">The Master strip in the
mixer</figcaption>
</figure>

The [Master strip]{.dfn} in Ardour is very similar to the other [busses
mixer strips](@@audiomidi-busses-mixer-strips). There are nevertheless a
few differences due to the nature of the Master strip, that is being the
last point of treatment before the output or rendering:

-   There is no color affected to the master strip
-   There is exactly one and only one Master Bus Strip for a session, so
    it cannot be saved as a template, duplicated or removed in the
    context menu, although it can be renamed.
-   The master strip cannot be hidden or disabled, so there is not
    [X]{.kbd} in the top right, nor an [Active]{.kbd .option} checkbox
    in the context menu.
-   It is by definition always solo, so there is no [Solo]{.kbd} button,
    and [Iso]{.kbd} and [Lock]{.kbd} are disabled.
-   If the [Master bus output gain control](@@loudness-analyzer) is
    enabled, two controls are visible:
    -   a [LAN]{.kbd} button, to start the Loudness Analyzer &
        Normalizer,
    -   a volume slider to that can be controlled manually or set by the
        Normalizer.
-   If the session has a [Monitoring
    section](@@session-properties#properties-monitoring), two buttons
    are visible:
    -   [Mute]{.kbd} to mute the Master bus while the monitoring is
        still active,
    -   [Mon]{.kbd} to show/hide the monitoring section in the Mixer
        view.
-   It cannot belong to a mix group, so the [Grp]{.kbd} button is
    missing.

The Master bus strip is *always* fixed, at the right end of the mixer,
regardless of the scrolling position.
