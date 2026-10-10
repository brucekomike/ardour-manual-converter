# Region Properties
## Region properties

![The Region Properties window](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/region-properties.png)

The [Region properties]{.dfn} window brings information about the
selected regions, and allows to fine tune its sequencing. It is accessed
through the [Region \> Properties...]{.kbd .menu} menu, or by
[right]{.kbd .mouse} clicking the region, [*Name_of_the_Region* \>
Properties...]{.kbd .menu}.

This window also allows to manually set the different values.

| Field                            | Meaning                                                                                                                                                                                                                                                               | Editable |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| Name:                            | The [name of the region](@@region-naming) in the editor                                                                                                                                                                                                               | X        |
| [Audition]{.kbd .menu}           | This button allows to listen to the region and only the region, dry (with no effects, regardless of the processors applied to the track). For MIDI, the default MIDI synth, set in the [Preferences](@@preferences#preferences-midi), is used to audition the region. |          |
| Position:                        | Position in time of the left-hand side of the region                                                                                                                                                                                                                  | X        |
| End:                             | Position in time of the right-hand side of the region                                                                                                                                                                                                                 | X        |
| Length:                          | Duration of the region (=End−Position)                                                                                                                                                                                                                                | X        |
| Sync point (relative to region): | Position in time of the [Sync Point](@@grid-controls), relative to the beginning of the region. No manual sync point means the sync point is the beginning of the region (=Position), so will show as \"0\" in time and `001|01|0000` in Bars:Beats notation.         | X        |
| Sync point (absolute):           | Position in time of the [Sync Point](@@grid-controls), relative to the beginning of the session. No manual sync point means the sync point is the beginning of the region, and will be equal to the Position.                                                         | X        |
| File start:                      | Position in time of the beginning of the region relative to the source file start. If the region has not been trimmed on the left, then the regions start is the file start and this value is 0.                                                                      |          |
| Source:                          | Name of the source audio/MIDI file the region is extracted from. A region can be a part of or a whole audio/MIDI file, and multiple regions can be based on the same source file.                                                                                     | X        |
| Region gain:                     | *(Audio files only)* Manual gain, in dB, applied constantly to the whole region, regardless of the global track\'s gain, automation, etc...                                                                                                                           | X        |
| Peak amplitude:                  | *(Audio files only)* Maximum level the signal reaches inside the region. Expressed in dBFS (Full Scale), where 0 is the numeric maximum a signal can reach.                                                                                                           |          |

All the fields marked as \"editable\" in the table above allow the user
to manually enter a value in the field, to manually set this value.

[Right]{.kbd .mouse}-clicking on a field allow to switch between the
different [clock modes](@@editing-clocks).

The context menu that pops up also allows the relevant fields (Position,
End, and both Sync points) to be set from the playhead location, which
can be used to e.g. trim a region to the playhead or place a sync point
exactly on a beat.
