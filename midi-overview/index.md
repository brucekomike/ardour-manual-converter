# MIDI Overview
MIDI (or Musical Instrument Digital Interface) is a method of
representing musical concepts in a form suitable for use in computers.
MIDI defines 16 different [channels]{.dfn}, along which messages are
passed to instruments or synthesizers that understand the MIDI protocol;
notes are played by sending appropriately crafted [NoteOn]{.dfn}
messages that are followed by [NoteOff]{.dfn} messages. MIDI channels
can be manipulated with special [controller]{.dfn} messages to alter the
pitch of instruments, or their volume or timbre, and they can also tell
the instrument or synthesizer what sound to play using [Program
Change]{.dfn} and [Bank Select]{.dfn} messages.

Typically Program Change and Bank Select messages are collectively
referred to by the singular term [Patch Change]{.dfn}.

## Key features of Ardour MIDI handling

- MIDI, just like audio, exists in regions. MIDI regions behave like
  audio regions: they can be moved, trimmed, copied (cloned), or
  deleted. Ardour allows either editing MIDI (or audio) regions, or MIDI
  region content (the notes), but never both at the same time. The
  [e]{.kbd} key (by default) sets [Internal
  Edit](@@toolbox#edit-internal) Mode, which allows the editing of MIDI
  data in a given region.
- All MIDI I/O is handled by the audio/MIDI backend was chosen when
  starting Ardour. In general, all backends provide sample accurate
  timing and maximal efficiency when communicating with external
  software synthesizers.
- Every MIDI track has its own input port; it may have an arbitrary
  combination of audio and MIDI outputs, depending on the signal
  processing in the track; the full flexibility of Ardour patching &
  connectivity is present for MIDI just as it is for audio.
- Full automation for MIDI tracks, integrated with the handling of all
  MIDI [CC]{.abbr title="Continuous Controller"} data for each track.
- Controllers (CC data) can be set to discrete or continuous modes; the
  latter will linearly interpolate between control points and send
  additional data.

## Notable differences compared to other DAWs and sequencers

- Fader (volume) control currently operates on transmitted MIDI data,
  not by sending CC #7.
- All note/data editing is per-region. There are no cross-region
  operations at this time.
- By default, copying a MIDI region creates a [deep link]{.dfn}---both
  regions share the same data source, and edits to the contents of one
  will affect the other. Breaking this link is done by selecting [MIDI
  \> Unlink from other copies]{.kbd .menu} from the region context menu,
  after which the selected region(s) will have their own copies of
  *only* the data that they visually display on screen. The region will
  no longer be trimmable back to its original length after an Unlink
  operation, and the operation cannot be undone.

```{toctree}
/working-with-midi/create-midi-tracks
/working-with-midi/create-midi-regions
```
