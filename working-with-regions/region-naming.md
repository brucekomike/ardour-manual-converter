# Region Naming
[Region names]{.dfn} are initially derived from either:

- the name of the track for which they were recorded, or
- the name of the embedded/imported file they represent.

## Whole File Region Names

These are not audio files, but regions that represent the full extent of
an audio file. Every time a new recording is done, or a new file is
imported to the session, a new region is created that represents the
[entire audio file]{.dfn}. This region will have the name of the
track/playlist/original file, followed by a \"-\", then a number plus a
dot and then a number.

For [recorded regions]{.dfn}, the number will increase each time a new
recording is made. So, for example, if there is a track called
`Didgeridoo`{.sample}, the first recorded whole file region for that
playlist will be called `Didgeridoo-1`{.sample}. The next one will be
`Didgeridoo-2`{.sample} and so on.

For [imported regions]{.dfn}, the region name will be based on the
original file name, but with any final suffix (e.g. \".wav\" or
\".aiff\") removed.

Normally, whole file regions are not inserted into tracks or playlists,
but regions derived from them are. The whole-file versions live in the
[Editor\'s region list](@@the-region-list) where they act as an
organizing mechanism for regions that are derived from them.

## Normal Region Names

When a region is inserted into a track and playlist, its initial name
will end in a [version number]{.dfn}, such as `.1`{.sample}. For a
recorded region, if the whole file region was `Hang drum-1`{.sample},
then the region in the track will appear with the name
`Hang drum-1.1`{.sample}. For an imported region, if the whole file
region was `Bach:Invention3`{.sample}, then the region in the track will
appear with the name `Bach:Invention3.1`{.sample}.

## Copied Region Names

Duplicating or splitting a region creates new region(s) that are based
on the same original files. Hence, they share the same base name (in the
example above, `Hang drum-1`{.sample}), but their version number will be
incremented each time. Duplicating `Hang drum-1.4`{.sample} by
[left]{.kbd .mod1 .mouse} dragging it will create a new region called
`Hang drum-1.5`{.sample}. Splitting `Hang drum-1.5`{.sample} by hitting
the [S]{.kbd} key will remove the `Hang drum-1.5`{.sample} region and
create two shorter regions named `Hang drum-1.6`{.sample} and
`Hang drum-1.7`{.sample}.

## Renaming Regions

Regions can be renamed at any time using the region context menu : [
[right]{.kbd .mouse} click \> *name_of_the_region* \> Rename\... ]{.kbd
.menu}. The new name does not need to have a version number in it (in
fact, it probably should not). Ardour will add a version number in the
future if needed (e.g. if the region is copied or sliced).
