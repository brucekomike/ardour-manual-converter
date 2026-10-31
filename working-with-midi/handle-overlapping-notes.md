# Handling Overlapping Notes
Every MIDI note consists of two messages, a NoteOn and a NoteOff. Each
one has a note number and a channel (also a velocity, but that isn\'t
relevant here). The MIDI standard stresses that it is invalid to send a
second NoteOn for the same note number on the same channel before a
NoteOff for the first NoteOn. It is more or less impossible to do this
with a physical MIDI controller such as a keyboard, but remarkably easy
to trigger when editing in a DAW---simply overlapping two instances of
the same note will do it.

Ardour offers many options for how to deal with instances where two
instances of the same note overlap. Which one to use is a per-session
property and can be modified from [Session \> Properties \> Misc \> MIDI
Options]{.kbd .menu}.

|  |  |
|----|----|
| never allow them | Edits that would create note overlaps are not allowed |
| don\'t do anything in particular | Ardour leaves overlapping notes alone---the behaviour of a MIDI receiver (plugin or hardware) is undefined |
| replace any overlapped existing note | When one note is moved to overlap another, remove the one that wasn\'t being moved |
| shorten the overlapped existing note | When one note is moved to overlap another, shorten the one that wasn\'t moved so that there is no overlap |
| shorten the overlapping new note | When one note is moved to overlap another, shorten the one that was moved so that there is no overlap |
| replace both overlapping notes with a single note | When one note is moved to overlap another, merge them both to form one (longer) note |

Changing the option in use will not retroactively make changes---it will
only affect new note overlaps created while the option remains chosen.

Ardour does not check for note overlaps across tracks or even across
regions. Dealing with the consequences is up to the user.
