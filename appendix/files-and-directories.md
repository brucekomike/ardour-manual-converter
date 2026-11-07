# Files and Directories Ardour Knows About
## Configuration Directory

Ardour stores configuration files in two places. The system
configuration directory and the user configuration directory. The system
configuration directory is used for stock configuration files at install
time. The user configuration directory is used by Ardour to store
configuration changes made in the GUI as well as being a place the user
can add control surface device files, scripts etc.

Ardour tries to use standard places for these directories for the
platform it is running on.

### Linux

The user configuration directory will be somewhere inside the user\'s
home directory. The home directory on a linux system is normally
`/home/$USER/`, but should also be returned by `$HOME` or `~`. A normal
place to find this is `$HOME/.config/ardour*/` where `*` is the major
version. However this can be set by the system with the
`$XDG_CONFIG_HOME` environment variable to something else. If you cannot
find `$HOME/.config/` on your system try `echo ${XDG_CONFIG_HOME}` to
see if your distro is using something else. In any case Ardour appends
the `ardour*` directory to the result where `*` is the major version
number. For example, `ardour5` where the Ardour version is 5.6.

In Linux, all path names are lowercase and case-sensitive.

### macOS

The user configuration directory on macOS is
`$HOME/Library/Preferences/Ardour*/` where `*` is the major version
number. For example, `Ardour5` where the Ardour version is 5.6.

### Windows

Windows users are not expected to hand edit configuration files at all.
It is expected configuration options are changed with some sort of GUI
tool. For the most part all of Ardour\'s configuration is taken care of
by the GUI in preferences. However, there are devices that may need a
custom file and that would be in the users configuration directory.

Ardour asks the system for this directory and then appends `Ardour*` to
the path where `*` is the major version number. For example, `Ardour5`
where the Ardour version is 5.6. The official path would look like:
`%localappdata%\Ardour5\` Windows expands `%localappdata%` to a real
path.

An example of a configuration path in Window 10 would be:
`C:\<User>\AppData\Local\Ardour5\` The user in the path would be the
user\'s account name.

The above is only an example and may not even be true for all
installations of Windows 10.

## Plugins

Plugins will be installed in various places, some by standard and some
by developer whim. Some are installed incorrectly by distro policy.

### Linux

On Linux, there are 4 kinds of plugins Ardour can use: LADSPA, LV2
(LADSPA version 2), VST2, and VST3.

#### LADSPA

LADSPA plugins should be found in `/usr/lib/ladspa/`,
`/usr/local/lib/ladspa/` or in a directory mentioned in your LADSPA_PATH
environment variable. The most common mistake made by distro packagers,
is to use a path like `/usr/lib/$ARCH/ladspa/` and find that Ardour will
not find that by default. The user can either add a link from this
actual directory to the standard directory or add this path to
LADSPA_PATH.

#### LV2

LV2 plugins should be found in `/usr/lib/lv2/`, `/usr/local/lib/lv2/` or
in a directory mentioned in your LV2_PATH environment variable. The most
common mistake made by distro packagers, is to use a path like
`/usr/lib/$ARCH/lv2/`, `/usr/lib64/lv2` or `/usr/local/lib64/lv2` and
find that Ardour will not find that by default. The user can either add
a link from this actual directory to the standard directory or add this
path to LV2_PATH.

#### Linux VST or lxvst

They are typically installed in `/usr/lib/lxvst`, `/usr/local/lib/lxvst`
or a directory mentioned in your LXVST_PATH environment variable.
However, this is not a standard and the VST plugin developer may install
the plugin just about anywhere. Therefore Ardour allows the user to set
extra VST paths in the preferences GUI under Plugins\>VST.

### macOS

On the Mac, plugins are expected to be installed correctly Ardour uses
the system tool to scan for AU style plugins and LV2s should be in the
right place. LV2 should be in `$HOME/Library/Audio/Plug-Ins/LV2/`
`/Library/Audio/Plug-Ins/LV2/` `/usr/local/lib/lv2/` `/usr/lib/lv2/` If
an AU or LV2 plugin does not show up on a Mac it is probably a
development fault with the plugin and the plugin will not work with
anything. Ardour in Ardour 5.6 has support for native VST plugins. That
is VST plugins built for OSX. I am not sure if these have a standard
place to be, but as with other VSTs the search path can be edited at
Plugins\>VST.

### Windows

The most common plugins on Windows are VSTs. However, LADSPA and LV2
plugins are available for windows as well. In fact Ardour\'s built in
plugins are LV2s. The biggest advantage of LV2 plugins is that they are
the most likely to be cross platform and therefore allow the same Ardour
project to be worked on in Windows, OSX and Linux.

#### VST

As with other platforms, VSTs on Windows do not have a standard place to
reside. Ardour Preferences\>Plugins\>VST allows setting the VST path
from the GUI.

#### LV2

The LV2 standard for Windows is `%APPDATA%/LV2/` or
`%COMMONPROGRAMFILES%/LV2/` (On Windows 10:
`C:\<User>\AppData\Roaming\LV2\` or
`C:\Program Files\Common Files\LV2\`).

## Project Directory

Ardour places a project directory where the user tells it to. This
directory is chosen when creating a project. In most cases the user does
not need to know about the files inside of the project directory.
However there are a few sub-directories worth noting.

### export

This is the sub-directory where exported files end up.
