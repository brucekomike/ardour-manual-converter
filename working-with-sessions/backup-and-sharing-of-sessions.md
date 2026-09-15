# Backup and Sharing of Sessions
An Ardour session is stored in a single folder on the computer\'s
filesystem. This makes [backup]{.dfn} very easy: any tool capable of
backing up a folder can be used to backup a session. The location of a
session is picked when it is created ---by default it will be in the
default session location, which can be altered via [Edit \> Preferences
\> General \> Session]{.kbd .menu}.

The single folder approach also makes sharing a project easy. Simply
copy the session folder (onto a storage device, or across a network) and
another Ardour user (on any platform) will be able to use it.

There is one complication in both cases: a session may reference media
files that are stored outside of the session folder, if the user has
opted not to select [Session \> Import \> Copy to Session]{.kbd .optoff}
during import. Backing up a session with embedded files will not create
a copy of the session containing those files. To bring those external
files to the session folder, the [[Session \> Clean-up \> Bring all
media into session folder]{.kbd .menu} menu](@@cleaning-up-sessions) can
be used.

## Using the dedicated Zip/Archive Current Session tool

![The Zip/Archive Current Session window](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/archive-session.png)

The [Zip/Archive Current Session]{.kbd .menu} tool is located in the [
File \> Archive...]{.kbd .menu} menu.

It allows to create a single file containing everything useful in the
session, to share it or back it up, conveniently compressed to a
session-archive which is a zip-file (tar.xz to be specific) containing
all the audio, MIDI, plugin-settings,\... and the currently active
session. Ardour can also extract those bundles ([Session \>
Open...]{.kbd .menu}).

As opposed to zipping the entire session-folder manually,

1.  the session-archive only contains the current session-snapshot and
    only files which are used
2.  externally referenced files are included in the archive.

The window shows the following options:

|                                      |                                                                                                                                   |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [Archive Name]{.dfn}                 | The name of the archive file, defaulting to the name of the session followed by the date and time                                 |
| a dropdown extension selector        | allowing to choose between different kind or compressed archive file types                                                        |
| [Target directory/folder]{.dfn}      | defining where in the filesystem the archive file will be generated                                                               |
| [Audio Compression]{.dfn}            | a dropdown menu allowing to compress the audio files themselves by using an audio-tailored compression format, more on that below |
| [Exclude unused audio sources]{.dfn} | a checkbox to drop every audio that is in the session, but not actually used in the editor                                        |

The [Audio Compression]{.kbd .menu} selection accepts any of:

-   None
-   FLAC 16bit
-   FLAC 24bit

Encoding the audio sources to FLAC allows for a good size reduction of
the session. It should be noted though that FLAC is a fixed-point
format, meaning that if the audio in the session is in a floating-point
format, this conversion will lose some information on the samples values
that are rounded, though usually, this lost information cannot be
perceived. Choosing \"*None*\" for Audio Compression does not compress
the audio to FLAC, hence preserving the floating-point data at the cost
of a bigger file size. Notice also that converting to FLAC automatically
normalizes the audio.

Using the [Exclude unused audio sources]{.kbd .option} option allows to
only keep the files actually used in the session, which can be useful to
leave any unused take or reference material out of the backup, reducing
the archive\'s global file size.
