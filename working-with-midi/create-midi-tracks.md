# Creating MIDI Tracks
A [MIDI track]{.dfn} is created much like any other track (see [Adding
Tracks, Busses and VCAs](@@adding-tracks-busses-and-vcas)). However,
there are a few things that are unique to creating MIDI tracks.

When adding a MIDI track using the [Add Track/Bus/VCA]{.kbd .menu}
dialog, the [MIDI Tracks]{.kbd .menu} item should be highlighted in the
[Template/Type]{.kbd .menu} list on the left. This will enable the
[Instrument]{.kbd .menu} combobox while disabling the
[Configuration]{.kbd .menu} and [Record Mode]{.kbd .menu} comboboxes.

The [Instrument]{.kbd .menu} combobox allows the selection of a plugin
for the track to be created that will generate audio in response to MIDI
data; if the track is intended to drive an external device then
[-none-]{.kbd .menu} should be selected instead.
