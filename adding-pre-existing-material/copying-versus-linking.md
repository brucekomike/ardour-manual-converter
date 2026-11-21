# Copying Versus Linking
[Copying]{.dfn} and [linking]{.dfn} are two different methods of using
existing audio files on the computer (or network file system) within a
session. They differ in one key aspect:

## Copying

An existing media file is copied to the session\'s audio folder, and if
necessary converted into the session\'s native format.

For audio files, the format can be chosen (e.g. WAVE or Broadcast WAVE).
Audio files will also be converted to the session sample rate if
necessary (which can take several minutes for larger files).

MIDI files will already be in SMF format, and are simply copied into the
session\'s MIDI folder.

## Linking

A link to an existing media file somewhere on the disk is used as the
source for a region, but the data is **not copied or modified** in any
way.

While linking is handy to conserve disk space, it means that the session
is [no longer self-contained]{.dfn}. If the external file moves, it will
become unavailable, and any changes to it from elsewhere will affect the
session. A backup of the session directory will miss linked files.

The [Copy file to session]{.kbd .option} option in the Import dialog
window allows to choose to copy or link files into the session:

|  |  |
|----|----|
| [Copy file to session]{.kbd .option} | This file will be imported in the audio/MIDI folder of the session. |
| [Copy file to session]{.kbd .optoff} | This file won\'t be copied. |

There is a global preference [Edit \> Preferences \> General \> Session
\> Always copy imported files]{.kbd .menu}. If it is enabled, linking a
file will not be possible.
