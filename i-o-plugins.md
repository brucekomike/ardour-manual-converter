# I/O Plugins
I/O plugins are a way to process audio outside the normal Ardour session
or connect to sources typically unavailable in a DAW, such as outputs of
NDI devices. Pre-plugins run before Ardour does any processing,
post-plugins run after Ardour has done all processing.

A common use case is wet recording where a number of plugins are applied
directly to the physical input. The processed signal then can be routed
to any number of tracks or busses in Ardour. This is a lot like doing
some of the processing with a chain of guitar pedals, then feeding the
signal to an Aux In port on a mixing console or an input port on a
multi-effects digital pedalboard.

The rationale for pre-processing with I/O plugins is that it\'s a more
lightweight way to do it as compared to busses. Much of that is because
busses have automatable parameters such as fader and panner positions,
as well as plugins\' parameters. Evaluating parameter automation (even
when there\'s none) adds additional load to the CPU. However I/O plugins
are not automatable, so there\'s no evaluation happening. As far as
Ardour is concerned, they are almost like JACK audio server clients
running alongside Ardour.

Another use case would be loading an instance of the NDI Input plugin as
a pre-processing plugin to be able to capture and mix sources from NDI
devices, or loading an instance of the NDI Output plugin to send audio
from Ardour over IP to a receiver for broadcasting.

![NDI Input plugin loaded as a pre-processing I/O
plugin](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/io-plugins-ndi-input.png){.hdimage}

It\'s also possible to use the post-processing section to load plugins
for room correction or signal analysis (VU meters, spectrum analyzers
etc.).

## Adding I/O plugins

New I/O plugins can be added in the [I/O Plugins]{.kbd .title} dialog
([Window \> I/O Plugins]{.kbd .menu}).

![Empty slots in the I/O Plugins
dialog](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/io-plugins-empty-slots.png){.hdimage}

Right-clicking opens the same menu for plugin selection available for
mixer channel strips:

![Right-click menu in the I/O Plugins
dialog](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/io-plugins-right-click-menu.png){.hdimage}

Double-clicking opens the [Plugin Selector]{.kbd .title} dialog.

Once a plugin has been selected and added, it shows in either Pre- or
Post-process section depending on your choice.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/io-plugins-one-plugin-added.png" class="hdimage"
alt="ACE Compressor added to the pre- section" />
<figcaption>ACE Compressor added to the Pre-process section</figcaption>
</figure>

## Routing I/O plugins

I/O plugins have the same user interface for setting input and outputs
that is also available in mixer channel strips. The button above the
plugin name opens a drop-down menu for quickly choosing an input port.
The button below opens the drop-down menu for choosing the output port.

![Choosing output for an I/O
plugin](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/io-plugins-choose-output.png){.hdimage}

Additionally, new tracks automatically connected to an I/O plugin can be
easily created in the [Recorder]{.kbd .title} window by clicking the
[+]{.kbd .key} button and then setting a new for that track.

![New track connected to an I/O
plugin](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/io-plugins-new-track-from-io-plugin.png){.hdimage}

On the [Audio Connections]{.kbd .window} dialog, the ports of pre- and
post-process plugins are listed on dedicated tabs ([I/O Pre]{.kbd .tab}
and [I/O Post]{.kbd .tab}), separately from all other ports.

![I/O Plugins in the Audio Connections
dialog](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/io-plugins-in-audio-connections.png){.hdimage}
