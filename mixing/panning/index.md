# Panning
[Panning]{.dfn} is the process of distributing one or more signals
across a series of outputs so that the listener will have the experience
of them coming from a particular point or area of the overall listening
field.

It is used to create a sense of space and/or a sense of motion in an
audio mix. Different signals can be spread out across the space, and
moved over time.

## Types of Panners

The way a panner works depends a great deal on how many signals it is
going to process and how many outputs it will send them to. The simplest
case is distributing a single signal to 2 outputs, which is the common
case when using a \"mono\" track and a stereo speaker setup.

But panning in Ardour could theoretically involve distributing any
number of signals to any number of outputs. In reality, Ardour does not
have specific panners for each different situation. Currently, it has
dedicated panners for the following situations:

- 1 signal distributed to 2 outputs (the [mono panner](@@mono-panner))
- 2 signals distributed to 2 outputs (the [stereo
  panner](@@stereo-panner))
- N signals distributed to M outputs (the [VBAP panner](@@vbap-panner))

Even for each of these cases, there are many different ways to implement
panning. Ardour currently offers just one solution to each of these
situations, but in the future will offer more.

In addition to the panners, Ardour has a balance control for subtle
corrections to existing stereo images.

```{toctree}
/mixing/panning/mono_panner
/mixing/panning/balance_control
/mixing/panning/stereo_panner
/mixing/panning/vbap_panner
/mixing/mixer-scenes
/mixing/saving-importing-mixer-strips
/loudness-analyzer-and-normalizer
/realtime-perceptual-analyzer
```
