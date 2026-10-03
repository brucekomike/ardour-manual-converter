# Automation
<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/automation-lane1.png" style="width:75.0%" />
<figcaption>A typical automation lane</figcaption>
</figure>

[Automation]{.dfn} is the ability to dynamically control various aspects
of a track\'s innate attributes and the attributes of any processors
attached to it. In Ardour, automation can be used to make dynamic
changes to a track\'s:

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/automation-menu1.png" height="211" />
<figcaption>The automation menu</figcaption>
</figure>

-   Fader (Volume)
-   Trim
-   Muting
-   Panning
-   Any attached processor\'s parameters

Any combination of these can be enabled on a single track; as such, it
offers a lot of power and flexibility over how a track will ultimately
sound when played back.

Activating automation for a track is done by clicking the [A]{.kbd
.menu} icon on the [track head](@@audio-track-controls) and checking the
type of automation needed. A new \"pseudo-track\" will appear, showing
the waveform in the background, called an \"automation lane\", where the
value of the parameter can be edited : the x axis is the time, and the y
axis is the value of the parameter.

If the [Edit \> Show Automation Lane on Touch]{.kbd .option} is checked,
clicking any parameter in a plugin window, a hardware controller,
etc\... will result in this parameter\'s automation lane being
temporarily shown, and clicking another parameter will hide this lane to
show the new one.

```{toctree}
/automation-nomenclature
/automation-states
/automation-lanes
/automation-curves
/automation-modes
/controlling-a-track-with-automation
/applying-effects-to-regions-separately
```
