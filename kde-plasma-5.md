# KDE Plasma 5
Under [KDE Plasma 5]{.dfn}, plugin and various other windows will not
stay on top of any main window; therefore a workaround is required.

## Workaround for ancillary windows not staying on top in KDE Plasma 5
{#workaround}

In order to force ancillary windows in Ardour to stay on top, the
following steps are necessary:

1.  Launch the [System Settings]{.kbd .menu} application.
2.  Open [Workspace \> Window Management]{.kbd .menu}.
3.  Select [Window Rules]{.kbd .menu} in the left-hand sidebar. It
    should default to the [Window matching]{.kbd .menu} tab.
4.  Click on the [New...]{.kbd .menu} button.
5.  On the line that says [Window class (application)]{.kbd .menu}, set
    the combo box to [Substring Match]{.kbd .menu} and type
    [ardour]{.kbd .user} in the text entry field.
6.  In the list box that is labeled [Window types:]{.kbd .menu}, click
    on the option [Dialog Window]{.kbd .menu}, then press and hold
    [Ctrl]{.kbd} while clicking on the second option [Utility
    Window]{.kbd .menu}.
7.  Select the [Arrangement & Access]{.kbd .menu} tab.
8.  Check the box next to the [Keep above]{.kbd .menu} option. On the
    same line, select [Force]{.kbd .menu} from the combo box, then click
    on the [Yes]{.kbd .menu} radio button for that line.
9.  Click on the [OK]{.kbd .menu} button to dismiss the dialog.

At this point the [System Settings]{.kbd .menu} application can be
closed.

### Background Info
{#bg-info}

[According to one of the lead KDE
developers](https://bugs.kde.org/show_bug.cgi?id=172615#c26), they are
not willing to follow the ICCCM standard for utility windows. Apparently
they are alone in this understanding, as plugin windows on Ardour under
Linux work out of the box on every other WM out there.

Under KDE 4, there was a workaround in Ardour ([Preferences \> Theme \>
All floating windows are dialogs]{.kbd .menu}) that would \"trick\" KDE
into forcing certain window types to be on top of their parent windows,
but this no longer works under KDE Plasma 5.
