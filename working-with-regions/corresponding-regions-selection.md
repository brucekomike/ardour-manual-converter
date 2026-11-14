# Corresponding Regions Selection
[Track Groups](@@the-track-and-bus-group-list) have a property titled
[Select]{.kbd .option} which, if enabled, cause Ardour to propagate a
region selection in one track of a group to the [corresponding
regions]{.dfn} of the other tracks in that group.

This can be particularly useful when an instrument has been recorded
using multiple microphones (e.g. a drum kit): by enabling the
[Select]{.kbd .option} property for the group, selecting a region in one
of the tracks, Ardour will select the corresponding region in every
other track of the group, which in turn means that a subsequent edit
operation will affect all the tracks together.

## How Ardour Decides Which Regions are \"Corresponding\"

Regions in different tracks are considered to be corresponding for the
purposes of sharing [selection]{.dfn} if they satisfy *all* the
following criteria:

1.  each region starts at the [same offset]{.dfn} within its source
    file,
2.  each region is located at the [same position]{.dfn} on the timeline,
    and
3.  each region has the [same length]{.dfn}.

## Overlap Correspondence

Sometimes, the rules outlined above are too strict to get Ardour to
consider regions as corresponding. Regions may have been trimmed to
slightly different lengths, or positioned slightly differently, and this
will cause Ardour to not select regions in other grouped tracks.

In this case, changing [Edit \> Preferences \> Editor \> Regions in
active edit groups are edited together:]{.kbd .menu} to [whenever they
overlap in time]{.kbd .menu} will allow regions in different tracks to
be considered equivalent for the purposes of selection if they
[overlap]{.dfn}. This is much more flexible and will cover almost all of
the cases that the fixed rules above might make cumbersome.
