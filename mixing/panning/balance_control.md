# Balance Control
For stereo tracks, it is possible to switch between the default stereo
panner and a traditional [balance control]{.dfn} by right-clicking on
the panner widget.

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/stereo-balance.png" alt="Stereo Balance control" />
<figcaption aria-hidden="true">Stereo Balance control</figcaption>
</figure>

When the balance is centered, the incoming signals will be unaffected.
Moving it to one side will linearly attenuate the signal of the opposite
side.

While the balance control is considerably less flexible than the stereo
panner, it works with arbitrary content without danger of introducing
comb filter artefacts.
