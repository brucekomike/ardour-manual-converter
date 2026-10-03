# Starting Ardour
## How to Launch Ardour
{#how-to-start}

There are several ways of [starting Ardour]{.dfn}, which may vary
depending on which platform it is being used on:

-   by double-clicking the Ardour icon in the platform\'s file manager
    (e.g. Nautilus on Linux, Finder on OS X)
-   by double-clicking on an Ardour session file in the platform\'s file
    manager
-   on Linux, Ardour can also be started via the command line (see
    below)

When Ardour is run for the very first time, a special dialog is
displayed that will ask several questions about the system\'s setup. The
questions will not be asked again, but the choices thus made can always
be modified via the [Edit \> Preferences]{.kbd .menu} dialog.

If JACK is needed, in general, it is sensible to start it *before*
Ardour is run. Though this is not strictly necessary, it will provide
more control and options over JACK\'s operation. JACK can be started
through the CLI of a terminal, or by using a GUI program, like
[QjackCtl](https://qjackctl.sourceforge.io/) or
[Cadence](http://kxstudio.linuxaudio.org/Applications:Cadence).

If Ardour is opened without specifying an existing session, it will
display the [Session \> New...]{.kbd .menu} dialog and the [Audio/MIDI
Setup]{.kbd .menu} dialog. See [New/Open Session
Dialog](@@newopen-session-dialog) for a description of those dialogs.

## Starting Ardour From the Command Line (Linux)
{#from-cli}

Like (almost) any other program on Linux, Ardour can be started on the
command line. Type the following command in a terminal window, adjust
the path for your version of the program:

[/opt/Ardour-8.6.0/bin/ardour8]{.kbd .cmd .lin}

To start Ardour with an existing session, use:

[/opt/Ardour-8.6.0/bin/ardour8 */path/to/session*]{.kbd .cmd .lin}

Replace /path/to/session with the actual path of the session. Either the
session folder or any session file inside the folder can be specified,
including snapshots.

To start Ardour with a new, named session, use:

[/opt/Ardour-8.6.0/bin/ardour8 -N */path/to/session*]{.kbd .cmd .lin}
