# The Track and Bus Group List
This docks helps manage track/bus groups that exist in the session.
These groups allow related tracks to share various properties (such as
mute or record enable state). For full details, see the section called
[Track and Bus Groups](@@track-and-bus-groups).

## Columns
{#track-and-bus-group-list-columns}

The columns in this list are as follows:

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Col  | the colour that the group uses for its tab in the editor.          |
| Name | the group name.                                                    |
| V    | whether the tracks and busses in the group are visible.            |
| On   | whether the group is enabled.                                      |
| G    | ticked if the constituents of the group are sharing gain settings. |
| Rel  | ticked if shared gains are relative.                               |
| M    | ticked if the constituents share mute status.                      |
| S    | ticked if the constituents share solo status.                      |
| Rec  | ticked if the constituents share record-enable status.             |
| Mon  | whether the constituents share monitor settings.                   |
| Sel  | whether the constituents are selected together.                    |
| A    | whether the constituents share active status.                      |

## Buttons
{#track-and-bus-group-list-buttons}

The [+]{.kbd .menu} button under the list allows the creation of an
(empty) group, while the [−]{.kbd .menu} button deletes the selected
group (but not the tracks in this group).

## Right-click menu
{#track-and-bus-group-list-right-click-menu}

The context menu, reached by [right]{.kbd .mouse}-clicking a group,
allows for multiple mixing actions:

```{eval-rst}
+-----------------------------------+-----------------------------------+
| Create New Group From...          | Creates a new group based on some |
|                                   | track properties. The choice is:  |
|                                   |                                   |
|                                   | -   [Selection...]{.kbd .menu} to |
|                                   |     create a group of all         |
|                                   |     selected tracks               |
|                                   | -   [Record Enabled...]{.kbd      |
|                                   |     .menu} to create a group of   |
|                                   |     all the tracks that are       |
|                                   |     record enabled                |
|                                   | -   [Soloed...]{.kbd .menu} to    |
|                                   |     create a group of all the     |
|                                   |     soloed tracks                 |
+-----------------------------------+-----------------------------------+
| Create New Group with Master      | Acts exactly as the previous      |
| From...                           | choice, but also creates a        |
|                                   | Control Master tied to these      |
|                                   | tracks.                           |
+-----------------------------------+-----------------------------------+
| Assign Selection to Control       | Allows to link all the selected   |
| Master...                         | tracks to a chosen Control        |
|                                   | Master, whether or not they       |
|                                   | belong to a group.                |
+-----------------------------------+-----------------------------------+
| Assign Record Enabled to Control  | Allows to link all the record     |
| Master...                         | armed tracks to a chosen Control  |
|                                   | Master.                           |
+-----------------------------------+-----------------------------------+
| Assign Soloed to Control          | Allows to link all the soloed     |
| Master...                         | tracks to a chosen Control        |
|                                   | Master.                           |
+-----------------------------------+-----------------------------------+
| Enable All Groups                 | Enable all the groups, i.e. their |
|                                   | selected properties are           |
|                                   | synchronized.                     |
+-----------------------------------+-----------------------------------+
| Disable All Groups                | Disable all the groups, i.e.      |
|                                   | changing a property in a track    |
|                                   | won\'t affect the others.         |
+-----------------------------------+-----------------------------------+
```

When a group is selected, [right]{.kbd .mouse} clicking it adds the
following menu entries:

|                                      |                                                                                                                                                    |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Create New Group with Master From... | Acts exactly as the previous choice, but also creates a Control Master tied to these tracks.                                                       |
| Edit Group...                        | Shows the [Track/bus Group]{.kbd .menu} [window](@@the-track-and-bus-group-list).                                                                  |
| Collect Group                        | Rearranges the tracks/busses order to visually group together the tracks belonging to the same group.                                              |
| Remove Group                         | Deletes the group (but not the tracks/busses belonging to this group).                                                                             |
| Assign Group to Control Master...    | Allows to link all the tracks in the group to a chosen VCA.                                                                                        |
| Add/Remove Subgroup Bus              | Creates/removes a new bus connected to the Master, and send the output of all the tracks in the group to this new bus.                             |
| Add New Aux Bus (pre/post-fader)     | Creates a new bus connected to the Master, and create [Aux Sends](@@aux-sends) (pre or post-fader) in all the tracks in the group to this new bus. |
