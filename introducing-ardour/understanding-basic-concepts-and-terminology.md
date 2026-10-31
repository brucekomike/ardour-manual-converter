# Understanding Basic Concepts and Terminology
In order to fully grasp the terms used in Ardour (and this manual), it
is necessary to understand what things like sessions, tracks, busses,
regions and so on---as used in Ardour---are.

## Sessions

An Ardour [session]{.dfn} is a container for an entire project. A
session may contain an arbitrary number of [tracks]{.dfn} and
[busses]{.dfn} consisting of audio and [MIDI]{.abbr
title="Musical Instrument Digital
  Interface"} data, along with information on processing those tracks, a
mix of levels, and everything else related to the project. A session
might typically contain a song, an entire album, or a complete live
recording.

Ardour sessions are kept in directories; these directories contain one
or more [session files]{.dfn}, some or all of the audio and MIDI data,
and a number of other state files that Ardour requires. The session file
describes the structure of the session, and holds automation data and
other details.

Ardour\'s session file is written in [XML]{.abbr
title="eXtensible Markup
  Language"} format, which is advantageous as it is *somewhat*
human-readable and human-editable in a crisis. Sound files are stored in
one of a number of optional formats, and MIDI files as [SMF]{.abbr
title="Standard MIDI
  File"}.

It is also possible for Ardour sessions to reference sound and MIDI
files outside the session directory, to conserve disk space and avoid
unnecessary copying if the data is available elsewhere on the disk.

Ardour has a single current session at all times; if Ardour is started
without specifying one, it will offer to load or create one.

More details can be found in the [Sessions](@@sessions) chapter.

## Tracks

A [track]{.dfn} is a concept common to most [DAWs]{.abbr
title="Digital Audio
  Workstation"}, and also used in Ardour. Tracks can record audio or
MIDI data to disk, and then replay it with processing. They also allow
the audio or MIDI data to be edited in a variety of different ways.

In a typical pop production, one track might be used for the kick drum,
another for the snare, more perhaps for the drum overheads and others
for bass, guitars and vocals.

Ardour can record to any number of tracks at one time, and then play
those tracks back. On playback, a track\'s recordings may be processed
by any number of plugins, panned, and/or its level altered to achieve a
suitable mix.

A track\'s type is really only related to the type of data that it
stores on disk. It is possible, for example, to have a MIDI track with a
synthesizer plugin which converts MIDI to audio. Even though the track
remains MIDI (in the sense that its on-disk recordings are MIDI), its
output may be audio-only.

More details can be found in the [Tracks](@@tracks) chapter.

## Busses

[Busses]{.dfn} are another common concept in both DAWs and hardware
mixers. They are similar in many ways to tracks; they process audio or
MIDI, and can run processing plugins. The only difference is that their
input is obtained from other tracks or busses, rather than from disk.

A bus might typically be used to collect together the outputs of related
tracks. Consider, for example, a three track recording of a drum kit;
given kick, snare and overhead tracks, it may be helpful to connect the
output of each to a bus called \"drums\", so that the drum kit\'s level
can be set as a unit, and processing (such as equalization or
compression) can be applied to the mix of all the tracks. Such busses
are also called [groups]{.dfn}.

## Regions

A track may contain many segments of audio or MIDI. Ardour contains
these segments in things called [regions]{.dfn}, which are
self-contained snippets of audio or MIDI data. Any recording pass, for
example, generates a region on each track that is enabled for recording.
Regions can be subjected to many editing operations; they may be moved
around, split, trimmed, copied, and so on.

More details can be found at [Working With
Regions](@@working-with-regions).

## Playlists

The details of what exactly each track should play back is described by
a [playlist]{.dfn}. A playlist is simply a list of regions; each track
always has an active playlist, and can have other playlists which can be
switched in and out as required.

More details can be found in the [Playlists](@@playlists) chapter.

## Plugins

Ardour allows processing audio and MIDI using any number of
[plugins]{.dfn}. These are external pieces of code, commonly seen as VST
plugins on Windows or AU plugins on Mac OS X. Ardour supports the
following plugin standards:

|  |  |
|----|----|
| [LADSPA]{.abbr title="Linux Audio Developers' Simple Plugin API"} | the first major plugin standard for Linux. Many LADSPA plugins are available, mostly free and open-source. |
| [LV2]{.abbr title="LADSPA Version 2"} | the successor to LADSPA. Lots of plugins have been ported from LADSPA to LV2, and also many new plugins written. |
| [VST]{.abbr title="Virtual Studio Technology"} | Ardour supports VST plugins that have been compiled for Linux. |
| [AU]{.abbr title="Audio Units"} | Mac OS X versions of Ardour support AudioUnit plugins. |

Ardour has some support for running Windows VST plugins on Linux, but
this is rather complicated, extremely difficult for the Ardour
developers to debug, and generally unreliable, as it requires running a
large amount of Windows code in an emulated environment. If it is at all
possible, it is strongly advisable to use native LADSPA, LV2 or Linux
VST plugins on Linux, or AU on Mac OS X.

More details can be found at [Working With
Plugins](@@working-with-plugins).
