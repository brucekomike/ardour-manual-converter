# Cue Markers
[Cue markers]{.dfn} allow bridging linear and non-linear approaches to
composing music. The idea is that a user can set up entire cues, then
place a cue marker on the timeline to launch a cue of choice at a
particular point in time. The workflow is explained in more details in
the [Mixing Linear and Non-Linear
Workflows](@@mixing-linear-nonlinear-workflows) section.

Cue markers are displayed in the Location Markers ruler.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/cue-markers-ruler-example.png" style="width:75%;"
alt="Cue Markers Ruler" />
<figcaption>Cue Markers on the Location Markers ruler</figcaption>
</figure>

## Adding Cue Markers
{#adding-cure-markers}

To add a cue marker, right-click on the Location Markers ruler, then
selecting [Add \> Cue Marker]{.kbd .menu}, and then selecting a marker
between A and P in the submenu.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/cue-marker-ruler-right-click-menu.png" class="hdimage"
alt="Right-click menu for the Cue Markers ruler" />
<figcaption>Right-click menu for creating a cue marker</figcaption>
</figure>

## Moving Cue Markers
{#moving-cure-markers}

[Left]{.kbd .mouse}-clicking and dragging moves a single marker to a new
location on the timeline.

It is possible to move multiple markers by the same distance.
[Left]{.kbd .mouse .mod1}-clicking each marker creates a selection of
markers that can be dragged left or right together.

## Single marker
{#moving-single-marker}

[Left]{.kbd .mouse}-clicking and dragging moves a single marker to a new
location on the timeline.

## Multiple markers
{#moving--multiple-markers}

It is possible to move multiple markers by the same distance.
[Left]{.kbd .mouse .mod1}-clicking each discrete marker, or [Left]{.kbd
.mouse .mod3}-clicking the first and last markers of a range of markers
selects them, then dragging one to a new location will move all selected
markers together.

## Stopping All Cues

Ardour has a special kind of a marker that immediately stops all playing
cues. This marker ([Stop All Cues]{.kbd .menu}) can be added via the
right-click menu on the Cue Markers ruler.

## Removing Cue Markers
{#removing-cure-markers}

Right-clicking on an existing cue marker opens the context menu with a
number of options. Choosing [Remove]{.kbd .menu} will delete the cue
marker of choice.

When all existing cue markers have to be removed, the best option is to
right-click on the Cue Markers ruler (any place except an existing
marker) and choose [Clear All Cues]{.kbd .menu}. This will delete all
cue markers in the session.

## More Options

The context menu for existing markers provides several more options:

|                       |                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------|
| Set Cue:              | Picking a cue from the list here will replace the selected marker with a marker for a different cue. |
| Locate to Here        | This will move the playhead to the cue marker\'s position.                                           |
| Play from Here        | This will move the playhead to the cue marker\'s position and start playback.                        |
| Move Mark to Playhead | This will move the selected cue marker to the current position of the Playhead.                      |
