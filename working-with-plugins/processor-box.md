# Processor Box
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/processor-box.png" alt="the Processor Box" />
<figcaption>Processor Box.</figcaption>
</figure>

In Ardour terminology, a [processor]{.dfn} is anything which treats the
signal in some way and gets plugged into a mixer strip. Ardour provides
several builtin processors such as the fader or panners. Processors can
also be [plugins]{.dfn} used for effects or as instruments, as well as
sends or inserts which affect [signal routing](@@signal-routing).

The arrangement of processors is arbitrary, and there is no limit to how
many there can be. The Processor Box will automagically add a scrollbar
to itself if there are more processors in it than can be shown in the
given space.

The main box in the top half of a mixer strip shows the [processor
box]{.dfn}. Processors are shown as colored rectangles, with a small LED
beside them that lights up when the processor is enabled. The color of
the processor depends on its location in the sequence; processors that
are [pre-fader]{.dfn} are colored in red, and [post-fader]{.dfn}
processors are colored green (in the default theme).

The [processor box]{.dfn} will always contain a blue [Fader]{.dfn}
processor. This indicates where in the processor chain the main channel
fader is located; this is the fader shown in the lower half of the
strip. It can be enabled and disabled like any other processor.

## Adding Processors

Processors can be added to the chain by [Right]{.kbd .mouse}-clicking in
the processor list, This does three things:

-   A gap is opened up to indicate the location of the click. The gap
    shows where any new processors will be inserted.
-   The processor under the click is selected.
-   An options menu is presented.

From the menu, new processors can be inserted.

Processors can also be dragged and dropped from the [[Favorite
Plugins]{.dfn} window](@@favorite-plugins-window) to an appropriate spot
in the Processor Box.

The [Favorite Plugins]{.dfn} window can be populated via the [Plugin
Selector](@@plugin-selector), or by dragging and dropping an existing
processor from the [processor box]{.dfn} to the [Favorite Plugins]{.dfn}
window.

## To Reorder (Move) Processors

Processors can be re-ordered using drag and drop. Dragging a processor
allows it to be moved around within the chain, or copied to another
processor list on another track or bus.

## To Enable/Disable a Processor

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/processor.png" alt="a typical processor" />
<figcaption>A typical processor.</figcaption>
</figure>

To the left of the name of each processor is a small LED symbol; if this
is lit-up, the processor is active. [Left]{.kbd .mouse}-clicking on the
LED symbol, or [Middle]{.kbd .mouse}-clicking anywhere on the processor
will deactivate the processor and effectively bypass it. Click again to
reactivate the processor.

Some processors have their own bypass controls that are independent of
the one that Ardour provides; this can make it appear that the plugin is
non-responsive when its independent bypass control is active.

## Selecting Processors

A processor in the [processor box]{.dfn} can be selected with a
[Left]{.kbd .mouse}-click on it; it will be highlighted in red. Other
processors can be selected at the same time by [Left]{.kbd
.mouse}-clicking on them while holding down the []{.kbd .mod1n} key, and
ranges can be selected by [Left]{.kbd .mouse}-clicking on them while
holding down the []{.kbd .mod3n} key.

## Renaming Processors

Context-click on the processor to be removed and select [Rename]{.kbd
.menu}. In the newly opened dialog set a new name and click \"Rename\".
The caption of the processor will be instantly changed in the mixer
strip.

To restore the original name which, for plugins, is typically the
plugin\'s name, open the same dialog and click the button to the right
of the text input box, then click \"Rename\".

## Removing Processors

Context-click on the processor to be removed, and select [Delete]{.kbd
.menu}; or []{.kbd .mod3n}[Right]{.kbd .mouse}-click on it; or
[Left]{.kbd .mouse}-click on it and press the [Delete]{.kbd} key. If
multiple processors are selected, they will all be deleted at the same
time.
