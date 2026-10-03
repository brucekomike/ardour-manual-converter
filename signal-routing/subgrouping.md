# Subgrouping
[Subgrouping]{.dfn} (sometimes known as \"Grouping\" or \"Audio
Grouping\") is a way to collect related signals together to apply some
common treatment, before sending them on to the main mix. One standard
application is to group several tracks belonging to the same instrument
or section (such as a drum kit or horn section), to be able to adjust
their volume with a single fader, after their inner balance has been set
using the track faders.

Ardour supports both audio and MIDI subgroup busses, so it\'s possible
to collect MIDI events from multiple tracks and send them to a
multi-voice software synth or sampler.

Ardour also provides [VCAs](@@control-masters-mixer-strips) that is a
very flexible way to adjust the volume of a group of tracks/busses when
no additional processing is needed.

Create a subgroup from an existing Track/Bus group is done by
[right]{.kbd .mouse}-clicking on the relevant [group
tab](@@the-track-and-bus-group-list), and choosing [Add New Subgroup
Bus]{.kbd .menu}. A new bus will be created and every member of the
track group will have its outputs disconnected from other destinations
and then connected to the new bus inputs. The bus outputs will feed the
master bus unless manual connections have been selected in the session
preferences. The bus will be named after the track group name.

Alternatively, a group can be created manually, by first adding a new
bus, then, for each track to be fed in the subgroup bus, disconnecting
its outputs from the master and connecting it to the inputs of the
subgroup bus instead. This can be done in the global audio patchbay or
on a track by track basis via the output button of each track\'s channel
strip.

Remove a subgroup (bus) is done by [right ]{.kbd .mouse}-clicking on the
track group tab, and selecting [Remove subgroup bus]{.kbd .menu}. Simply
deleting the bus itself will **not** restore signal routing to the way
it was before the addition of the subgroup bus ---tracks that had been
subgrouped will be left with their main outputs disconnected.
