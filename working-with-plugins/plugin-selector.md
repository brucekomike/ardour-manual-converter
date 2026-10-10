# Plugin Selector
The [Plugin Selector]{.dfn} serves two purposes. Primarily it is used to
control the display status of plugins. It can also be used to find and
insert plugins into the [Processor Box](@@processor-box). It is
displayed either by a double-click in the [Processor Box]{.dfn} or by
choosing [New Plugin \> Plugin Selector...]{.kbd .menu} from the
[Processor Box]{.dfn} context menu.

Displayed for each plugin is the status (favorite, hidden), name, tags,
creator (author), type, and the number of audio and MIDI connections.
The plugins can be sorted by clicking on a column header.

<figure class="center">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/plugin-selector.png"
alt="The Plugin Selector window" />
<figcaption>The Plugin Selector window.</figcaption>
</figure>

## Plugin Display Status

Clicking on a *Fav*(orite) or *Hide* radio button changes a plugin\'s
display status. Clicking on an already selected radio button will cancel
it, returning the plugin to the normal display status. Plugins marked as
a favorite show up in the [Processor Box]{.dfn} context menu under [New
Plugin \> Favorites]{.kbd .menu} and in the [Favorite Plugins
window](@@favorite-plugins-window). Setting the hide radio button on a
plugin will keep the plugin from showing in the [Processor Box]{.dfn}
context menus [New Plugin \> By Creator]{.kbd .menu} or [New Plugin \>
By Category]{.kbd .menu}.

## Filtering Listed Plugins

The bottom left part of the [Plugin Selector]{.dfn} is used to filter
the listed plugins.

The center [Filter]{.dfn} column allows to show only some of the
plugins, based on what they are, their properties, format, creator\...

Moreover, direct text search are available in the the Search text-field
on the bottom left. Only the plugins that match *all* the search terms
(space separated) will show up in the upper list.

This textual search can be matched against Name and/or Tags by checking
the relevant momentary buttons under the search field. [Ignore Filters
when searching]{.kbd .menu} displays all the matching plugins,
regardless of the active *Filters*.

## Tags

Tags are text labels that can be used to mark a plugin. They are totally
free in their content, allowing the user to mark a plugin with whatever
info is relevant to him, but cannot include spaces (as spaces are used
to separate tags) or special characters except dashes, colons and
underscores.

Adding or removing tags is as simple as editing the [Tags for Selected
Plugin]{.dfn} field while the targeted plugin is selected.

Ardour comes with a large selection of tags for provided or usual
plugins, that are used by default but can be modified at will. It is
possible to go back to this \"standard\" tagging for a plugin by
clicking the [Reset]{.kbd .menu} button.

## Inserting Plugins in the Processor Box

The bottom-right part of the Plugin Selector [Plugins to be
connected]{.dfn} shows plugins that have been selected for insertion
into the [Processor Box]{.dfn}. A plugin can be added by either double
clicking the plugin entry in the top part, or, if already selected in
top left part, by clicking the [Add]{.kbd .menu} button.

Plugins can be removed from the right part with a double click, or, if
already selected, by clicking [Remove]{.kbd .menu}.
