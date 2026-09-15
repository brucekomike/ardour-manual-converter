# Monitor Signal Flow
There are three basic ways to approach monitoring:

### External Monitoring

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/external-monitoring.png" class="invert-in-dark"
alt="External monitoring" />
<figcaption aria-hidden="true">External monitoring</figcaption>
</figure>

When using [external monitoring]{.dfn}, Ardour plays no role in
monitoring at all. Perhaps the recording set-up has an external mixer
which can be used to set up monitor mixes, or perhaps the sound-card
being used has a \"listen to the input\" feature. This approach yields
zero or near-zero latency. On the other hand it requires external
hardware, and the monitoring settings are less flexible and not saved
with the session.

### Audio driver Hardware Monitoring
{#audio-driver-hardware-monitoring .clear}

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/jack-monitoring.png" class="invert-in-dark"
alt="Hardware Monitoring" />
<figcaption aria-hidden="true">Hardware Monitoring</figcaption>
</figure>

Some sound cards have the ability to mix signals from their inputs to
their outputs with very low or even zero latency, a feature called
[hardware monitoring]{.dfn}. Furthermore, on some cards this function
can be controlled by Ardour. This is a nice arrangement, if the sound
card supports it, as it combines the convenience of having the
monitoring controlled by Ardour with the low latency operation of doing
it externally.

### Software Monitoring
{#software-monitoring .clear}

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/ardour-monitoring.png" class="invert-in-dark"
alt="Software Monitoring" />
<figcaption aria-hidden="true">Software Monitoring</figcaption>
</figure>

With the [software monitoring]{.dfn} approach, all monitoring is
performed by Ardour---it makes track inputs available at track outputs,
governed by various controls. This approach will almost always have more
routing flexibility than JACK-based monitoring. The disadvantage is that
there will be some latency between the input and the output, which
depends for the most part on the buffer size that is being used.
