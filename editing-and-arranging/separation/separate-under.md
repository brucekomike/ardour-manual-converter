# Separate Under
## Separate Under

When one region is over another, and the lower region has to be cut so
that it directly adjoins both ends of the overlapping one, with no
overlaps, the [ Separate Under]{.dfn} tool can be a very efficient
time-saver. With the upper region selected, the [Edit \> Separate \>
Separate Under]{.kbd .menu} menu will split the lower region so that it
no longer overlaps the upper region at all.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/before-separate-under.png"
alt="region arrangement before separate under" /> <img
src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/after-separate-under.png"
alt="region arrangement after separate under" />
<figcaption>Region arrangement before and after 'Separate
Under'</figcaption>
</figure>

If the upper region covers only one end of the lower region, then this
operation is equivalent to [Trim to Next or Trim to
Previous](@@trimming-regions), depending on which end is covered.

## Separate Using Range

A loop or punch range can also be used to slice a region. By using the
[Edit \> Separate \> Separate Using Loop/Punch Range]{.kbd .menu}, any
selected regions that are covered by the range at both ends of the
range, or just one if the range only covers part of the region. This
makes it easy to generate regions that correspond precisely to a range.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/before-separate-loop.png"
alt="region arrangement before separate using loop range" /> <img
src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/after-separate-loop.png"
alt="region arrangement after separate using loop range" />
<figcaption>Region arrangement before and after 'Separate Using Loop
Range'</figcaption>
</figure>
