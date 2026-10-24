# Changing Note Properties
All details about selected notes can be viewed by context-clicking on
them. The dialog that pops up also allows for the modification of all
properties of the selected notes. Individual properties can also be
modified more efficiently using the techniques described below:

```{eval-rst}
+-----------------------------------+-----------------------------------+
| Moving notes                      | [←]{.kbd} and [→]{.kbd} move      |
|                                   | selected notes earlier and later  |
|                                   | in time.                          |
+-----------------------------------+-----------------------------------+
| Changing pitch values             | [↑]{.kbd} raises the pitch of the |
|                                   | selected notes.\                  |
|                                   | [↓]{.kbd} lowers the pitch of the |
|                                   | selected notes.\                  |
|                                   | If any of the selected notes are  |
|                                   | already at their minimum or       |
|                                   | maximum values, no changes will   |
|                                   | be made to them, to preserve      |
|                                   | their relative pitches. This can  |
|                                   | be overridden with [ ]{.kbd       |
|                                   | .mod2}. The default shift         |
|                                   | distance is one semitone. [       |
|                                   | ]{.kbd .mod3} alters this to one  |
|                                   | octave.                           |
+-----------------------------------+-----------------------------------+
| Changing velocity values          | [↑]{.kbd .mod1} increases the     |
|                                   | velocity of the selected notes.\  |
|                                   | [↓]{.kbd .mod1} reduces the       |
|                                   | velocity of the selected notes.\  |
|                                   | If any of the selected notes are  |
|                                   | already at their minimum or       |
|                                   | maximum values, no changes will   |
|                                   | be made to them, to preserve      |
|                                   | their relative velocities. This   |
|                                   | can be overridden with [ ]{.kbd   |
|                                   | .mod2}. Also, pressing [v]{.kbd}  |
|                                   | pops up a dialog that allows      |
|                                   | setting the absolute velocity     |
|                                   | value of all selected notes.      |
|                                   | Finally, the scroll wheel         |
|                                   | [⇑]{.kbd .mouse} [⇓]{.kbd .mouse} |
|                                   | will also adjust notes in the     |
|                                   | same way as the arrow keys (note  |
|                                   | that, like the arrow keys, it     |
|                                   | only affects selected notes---not |
|                                   | the note the pointer is over).    |
+-----------------------------------+-----------------------------------+
| Changing channel                  | Pressing [c]{.kbd} brings up a    |
|                                   | dialog that allows viewing and/or |
|                                   | altering the MIDI channel of the  |
|                                   | selected notes. If the selected   |
|                                   | notes use different channels,     |
|                                   | they will all be forced to the    |
|                                   | newly selected channel.           |
+-----------------------------------+-----------------------------------+
| Changing start/end/duration       | To make the note longer,          |
|                                   | [,]{.kbd} (comma) will alter the  |
|                                   | start time of the note.\          |
|                                   | [.]{.kbd} (period) will alter the |
|                                   | end time of the note. To make the |
|                                   | note shorter (move the start      |
|                                   | later, or end earlier), [,]{.kbd  |
|                                   | .mod1}/[.]{.kbd .mod1} can be     |
|                                   | used. Whether shortening or       |
|                                   | lengthening the note, its length  |
|                                   | will be altered by the current    |
|                                   | grid setting. To change the       |
|                                   | start/end positions by 1/128th of |
|                                   | a beat, the [ ]{.kbd .mod2}       |
|                                   | modifier must be added to these   |
|                                   | shortcuts.                        |
+-----------------------------------+-----------------------------------+
| Quantization                      | [q]{.kbd} will display the        |
|                                   | Quantize dialog to allow editing  |
|                                   | the current quantize settings,    |
|                                   | and then will quantize the        |
|                                   | selected notes. The default       |
|                                   | quantize settings are: quantize   |
|                                   | note starts to the current grid   |
|                                   | setting, no swing, no threshold,  |
|                                   | full strength.                    |
+-----------------------------------+-----------------------------------+
| Step Entry, Quantize, etc.        | Refer to the [Step                |
|                                   | Entry](@@step-entry), [Quantizing |
|                                   | MIDI](@@quantize-midi), etc.      |
|                                   | specific pages.                   |
+-----------------------------------+-----------------------------------+
```
