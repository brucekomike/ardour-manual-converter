# About Ardour's documentation
## Conventions Used In This Manual
{#conventions}

This section covers some of the typographical and language conventions
used in this manual.

### Keyboards and Modifiers

[Keyboard bindings]{.dfn} are shown like this: [s]{.kbd} or [x]{.kbd
.mod1}.

[x]{.kbd .mod1} means \"press the []{.kbd .mod1n} key, keep it pressed
and then also press the [x]{.kbd} key\".

Combinations such as [e]{.kbd .mod12} may be seen, which means \"hold
down the []{.kbd .mod1n} key *and* the []{.kbd .mod2n} key, and then,
while keeping them both down, press the [e]{.kbd} key\".

Different platforms have different conventions for which modifier key
(Control or Command) to use as the primary or most common modifier. When
viewing this manual from a machine identifying itself as running OS X,
[Cmd]{.kbd} will be seen where appropriate (for instance in the first
example above). On other machines [Ctrl]{.kbd} will be seen instead.

### Mouse Buttons

[Mouse buttons](@@mouse) are referred to as [Left]{.kbd .mouse},
[Middle]{.kbd .mouse} and [Right]{.kbd .mouse}. Ardour can use
additional buttons, but they have no default behaviour in the program.

#### Mouse Click Modifiers

Many editing functions are performed by clicking the mouse while holding
a modifier key, for example [Left]{.kbd .mouse .mod1}.

#### Mouse Wheel

Some GUI elements can optionally be controlled with the mouse wheel when
the pointer is hovering over them. The notation for mouse wheel action
is [⇑]{.kbd .mouse} [⇐]{.kbd .mouse} [⇓]{.kbd .mouse} [⇒]{.kbd .mouse}.

#### Context-click

The term [context-click]{.dfn} is used to indicate a [Right]{.kbd
.mouse}-click on a particular element of the graphical user interface.
Although right-click is the common, default way to do this, there are
other ways to accomplish the same thing---this term refers to any of
them, and the result is always that a menu specific to the item clicked
on will be displayed.

#### \"The Pointer\"

When the manual refers to the \"pointer\", it means the on-screen
representation of the mouse position or the location of a touch action
if touch interface is being used.

### Other User Input

Ardour supports hardware controllers, such as banks of [faders]{.kbd
.fader}, [knobs]{.kbd .knob}, or [buttons]{.kbd .button}.

### Menu Items

Menu items are indicated like this: [Top \> Next \> Deeper]{.kbd .menu}.
Each \"\>\"-separated item indicates one level of a nested menu or
sub-menu.

### OSC Messages

OSC messages, whether sent or received, are displayed like this:
[/transport_stop]{.kbd .osc}.

### Preference/Dialog Options
{#dialog-options}

Choices in various dialogs, notably the Preferences and Properties
dialog, are indicated thus:

[Edit \> Preferences \> Audio \> Some Option]{.kbd .option}.

Each successive item indicates either a menu, sub-menu, or a tabbed
dialog navigation. The final item is the one to choose or select.

If an option is deselected, it will look like this:

[Edit \> Preferences \> Audio \> Some other Option]{.kbd .optoff}.

### User Input
{#user=input}

Some dialogs or features may require the user to input data [such as
this]{.kbd .input}. In rare cases, certain operations will be required
to be performed at the command line of the operating system:

[cat /proc/cpuinfo]{.kbd .cmd .lin} [sleep 3600]{.kbd .cmd .mac} [ping
www.google.com]{.kbd .cmd .win}

### Program Output

Important messages from Ardour or other programs will be displayed
`like this`{.sample}.

### Notes

Important notes about things that might not otherwise be obvious are
shown in this format.

### Warnings

Hairy issues that might cause things to go wrong, lose data, impair
sound quality, or eat your proverbial goldfish, are displayed in this
way.
