# Channel Configuration
Ardour tracks can have any number of inputs and any number of outputs,
and the number of either can be changed at any time (subject to
restrictions caused by any plugins in a track). However it is useful to
not have to configure this sort of thing for the most common cases, and
so the [Add Tracks](@@adding-tracks-busses-and-vcas) dialog allows to
select \"Mono\", \"Stereo\" and few other typical multichannel presets

The name of the preset describes the number of [input channels]{.dfn} of
the track or bus.

If Ardour is configured to automatically connect new tracks and busses,
the number of outputs will be determined by the number of inputs of the
[master
[bus](@@understanding-basic-concepts-and-terminology#busses)]{.dfn}, to
which the track outputs will be connected.

For example, with a two-channel master bus, a Mono track has one input
and two outputs; a Stereo track has two inputs and two outputs.

If [Edit \> Preferences \> Signal Flow \> Track and Bus
Connections]{.kbd .menu} is set to [manual]{.kbd .menu}, then tracks
will be left disconnected by default and there will be as many outputs
as there are inputs. It is up to the user to connect them as desired.
This is not a particularly useful way to work unless something fairly
unusual is done with signal routing and processing. It is almost always
preferable to leave Ardour make connections automatically, even if some
changes are manually done later.
