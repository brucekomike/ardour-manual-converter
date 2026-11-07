# Performance Meters
The [Performance Meters]{.dfn} window provides low-level metering of the
digital signal processing taking place inside Ardour. One of the
scenarios where this is useful is when you need to determine whether
Ardour is in charge for excessive xruns.

<figure class="center">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/performance-meters.png" class="hdimage"
alt="The Performance Meters window" />
<figcaption aria-hidden="true">The Performance Meters
window</figcaption>
</figure>

This window displays worst case scenario measurements that do not
necessarily match the DSP meter in the top right corner of the window.
To see average and standard deviation values, hover either the Engine or
the Session values with the mouse pointer to see the tooltip.
