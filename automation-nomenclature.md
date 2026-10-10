# Automation Nomenclature
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/automation-fader1.png"
alt="An example of a fader automation lane (below) with its associated track (above)." />
<figcaption aria-hidden="true">An example of a fader automation lane
(below) with its associated track (above).</figcaption>
</figure>

Track automation occurs in one or more [lanes]{.dfn}. Each lane has a
control that allows setting the amount or position of a certain
[parameter]{.dfn} associated with the lane. Parameters are things that
can be controlled on a track\'s automation lane, such as volume,
panning, muting, trim, etc. [Automation curves]{.dfn} typically consist
of lines connected by [control points]{.dfn}, that live within the
confines of a lane; these tell Ardour how to change a given parameter
over time. [Automation modes]{.dfn} define how Ardour creates the values
in between the control points of a given automation curve, either by
connecting them with continuous lines or not. [Automation states]{.dfn}
govern how a given automation lane will behave during playback.
