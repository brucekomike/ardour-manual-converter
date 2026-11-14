# Understanding Playlists
A [playlist]{.dfn} is a list of regions ordered in time. It defines
which parts of which source files should be played and when. Playlists
are a fairly advanced topic, and can be safely ignored for many types of
audio production. However, the use of playlists allows the audio
engineer more flexibility for tasks like multiple takes of a single
instrument, alternate edits of a given recording, parallel effects such
as reverb or compression, and other tasks.

Each audio [track]{.dfn} in Ardour is really just a mechanism for taking
a playlist and generating the audio stream that it represents. As a
result, editing a track really means modifying its playlist in some way.
Since a playlist is a list of regions, most of the modifications involve
manipulating regions: their position, length and so forth. This is
covered in the chapter [Working With Regions](@@working-with-regions).

This page covers some of the things that can be done with playlists as
objects in their own right.

## Tracks are not Playlists

It is important to understand that a track *is not* a playlist. A track
*has* a playlist. A track is a mechanism for generating the audio stream
represented by the playlist and passing it through a signal processing
pathway. At any point in time, a track has a single playlist associated
with it. When the track is used to record, that playlist will have one
or more new regions added to it. When the track is used for playback,
the contents of the playlist will be heard. The playlist associated with
a track can be changed at (almost) any time, and tracks can even share
playlists.

Some other [DAW]{.abbr title="Digital Audio Workstation"}s use the term
[\"virtual track\"]{.dfn} to define a track that isn\'t actually playing
or doing anything, but can be mapped/assigned to a real track. This
concept is functionally identical to Ardour\'s playlists. We just like
to be little more clear about what is actually happening rather than
mixing old and new terminology (\"virtual\" and \"track\"), which might
be confusing.

## Playlists are Cheap

One thing to bear in mind is that playlists are cheap. They do not cost
anything in terms of CPU consumption, and they have very minimal efforts
on memory use. So generating new playlists whenever needed is
recommended. They are not equivalent to tracks, which require extra CPU
time and significant memory space, or audio files, which use disk space,
or plugins that require extra CPU time. If a playlist is not in use, it
occupies a small amount of memory, and nothing more.
