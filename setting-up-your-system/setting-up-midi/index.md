# Configuring MIDI
[[MIDI]{.abbr title="Musical Instrument Digital Interface"}]{.dfn} is a
way to describe musical performances and to control music hardware and
software.

Ardour can import and record MIDI data, and perform a variety of editing
operations on it. Furthermore, MIDI can be used to control various
functions of Ardour.

## MIDI-handling Frameworks

MIDI input and output for Ardour are handled internally by the same
\"engine\" that handles audio input and output. However, Ardour can use
as many MIDI devices as the system can see as there are no syncing
difficulties as there would be with audio.

|  |  |
|----|----|
| OS X | [CoreMIDI]{.dfn} is the standard MIDI framework on OSX systems. |
| Linux | [[ALSA]{.abbr title="Advanced Linux Sound API"} MIDI]{.dfn} is the standard MIDI framework on Linux systems. |
| Windows | [[MME]{.abbr title="Microsoft Multimedia Environment"}]{.dfn} is the standard MIDI framework on Windows systems. |

[[JACK]{.abbr title="JACK Audio Connection Kit"}]{.dfn} is an alternate
audio system which Ardour can utilize for both audio and MIDI. JACK is
used to route audio between independent applications, and is now
considered an advanced use case which is not recommended for most users.
Users with a need to use JACK for audio routing should consult the
latest documentation at the [JACK website](https://jackaudio.org/).

```{toctree}
/setting-up-your-system/setting-up-midi/midi-on-linux
/setting-up-your-system/setting-up-midi/midi-on-os-x
/setting-up-your-system/keyboard-shortcuts
```
