# Independent and Dependent MIDI Region Copies
When [copying a MIDI region]{.dfn}, Ardour has to decide whether to make
the copy refer to the same data as the original or not. If it does refer
to the same data, then editing either the copy or the original will
affect the both of them. If it refers to an independent copy of the data
then each one can be edited without affecting the other.

## Changing dependent/independent copying for the entire session

[Session \> Properties \> MIDI \> MIDI region copies are
independent]{.kbd .menu} can be used to control the default behaviour
when making a copy of a MIDI region.

When enabled, every new copy of a MIDI region results in a copy being
made of the MIDI data used by the region, and the new copy of the region
will refer to that data.

When disabled, every new copy of a MIDI region will refer to the same
MIDI data, and thus editing any copy will change the contents of all of
them.

Changing the status of this option has no effect on the existing
dependent/independent status of existing region copies.

## Making an existing copy of a MIDI region independent

[Right]{.kbd .mouse} clicking on the MIDI region to be independent then
selecting [MIDI \> Unlink From Other Copies]{.kbd .menu} makes it
independent: the copy is now using its own version of the data, and
edits to the copy will affect only the copy. Other copies will continue
to share data.

Note that the copied data only covers the extent of the region when the
copy is made. If the region was already trimmed and then a copy is made,
an independent copy will have no access to data that is earlier or later
than the bounds of the region it was copied from. Put differently,
making an independent copy of a trimmed MIDI region only retains the
visible part of it.
