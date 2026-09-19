# Keyboard Shortcuts
The [Keyboard Shortcuts]{.kbd .window} dialog allows easily redefining
existing keyboard shortcuts to operations and creating new ones.

![Keyboard
Shortcuts](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/keyboard-shortcuts-window.png){style="width:50%;"}

A thematic list of the default keyboard shortcuts in Ardour can be found
in the [Appendix](@@default-shortcuts), but the [Print Bindings (to your
web browser)]{.kbd} button show an up-to-date list of the current
keyboard bindings, with customization, nicely laid out by theme and
alphabetical.

## Contexts and Subcontexts
{#contexts-subcontexts}

The important concept to understand here is that the same shortcut can
be used for different operations in different contexts. E.g. in the
[Editor]{.dfn} context, the [T]{.kbd} key switches on the
[Stretch]{.dfn} mode to time-stretch clips on the canvas. However, in
the MIDI Step Entry context, [T]{.kbd} inserts an F-sharp note. The
contexts are represented by tabs in this dialog, e.g. Editor, MIDI,
Recorder, etc.

Inside every tab, features are grouped into [subcontexts]{.dfn} that can
be expanded or collapsed by clicking the triangular-shaped button to the
left of the name of each subcontext. E.g. the \'Snap\' subcontext lists
all snapping units, while the \'Region\' subcontext lists all actions
accessible via the right-click menu.

The [Search]{.dfn} function at the bottom of the dialog works within the
currently selected context/tab only. If a search returned zero results,
switching to a different context is a viable solution to locating the
action of interest.

## Setting New Shortcuts
{#setting-new}

Once an action of interest is located in the list, all it takes to set a
keybinding to it is selecting the action in the list, then pressing the
sequence of keys. The newly defined keybinding will immediately show up
in the [Shortcut]{.dfn} column.

## Redefining Existing Shortcuts
{#redefining-existing}

An existing shortcut to an action can easily be replaced with a
different one by selecting the action and pressing a new sequence of
keys. The newly defined keybinding will immediately show up in the
[Shortcut]{.dfn} column.

## Handling Collisions

Once a keybinding is assigned to an action, that keybinding is
considered taken. Attempting to assign that same keybinding to a
different action will result in a collision. Ardour will notify the user
that the keybinding is already taken (and by what action) and will ask
to either reconsider or force-set the keybinding to a new action.

![A keyboard shortcut
collision](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/keyboard-shortcuts-collision.png){style="width:50%;"}

Force-setting the keybinding of choice to a new action will remove the
keybinding from the action it was previously assigned to. A new
keybinding then can be assigned to that action.

## Removing Existing Shortcuts
{#removing-existing}

In some cases it is desirable to remove a shortcuts entirely. Selecting
an action of interest, then pressing the [Remove shortcut]{.kbd} button
at the bottom of the dialog will do just that. The keybinding will
immediately disappear from the [Shortcut]{.dfn} column.

## Reverting to Factory Settings
{#reverting-to-defaults}

If applied customizations to default keyboard shortcuts didn\'t work
out, it\'s possible to revert to \"factory settings\". Clicking [Reset
Bindings to Defaults]{.kbd} will remove all customizations and bring
back default keybindings. Important: Ardour will not ask for a
confirmation!

## Using Search Prefixes

The [Search]{.dfn} function supports the following prefixes:

-   [\"k:\"]{.dfn} search by shortcut name
-   [\"p:\"]{.dfn} search by action path (as displayed when hovering a
    shortcut in the list)
