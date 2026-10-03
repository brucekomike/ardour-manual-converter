# Cleaning Up Sessions
Recording and editing any serious session might leave the session with
some unused or misplaced files here and there. Ardour can help deal with
this clutter thanks to the tools located in the [Session \>
Clean-up]{.kbd .menu} menu.

## Bring all media into session folder
{#bring_all_media_into_session_folder}

When [importing media files](@@adding-pre-existing-material), if the
[Copy files to session]{.kbd .option} has not been checked, Ardour uses
the source file from its original destination, which can help avoiding
file duplication. Nevertheless, when the session needs to be archived or
transferred to another computer, moving the session folder will not move
those *external* files as they are not in the folder, as seen in [Backup
and sharing of sessions](@@backup-and-sharing-of-sessions).

Using the [Bring all media into session folder]{.kbd .menu} menu ensures
that all media files used in the session are located inside the
session\'s folder, hence avoiding any missing files when copied.

## Reset Peak Files
{#reset_peak_files}

Ardour represents audio waveforms with peak files, that are graphical
images generated from the sound files. This generation can be time and
CPU consuming, so it uses a cache of the generated images to speed up
the display process. To watch for files modification, Ardour relies on
the file-modification time. If an external file is embedded in the
session and that file changes, but the system-clock is skewed or it is
stored on an external USB disk (VFAT), Ardour can\'t know the change
happened, and will still use its deprecated peak files.

Using the [Reset Peak Files]{.kbd .menu} menu allows to reset this
cache, which frees up disk space, and forces the re-creation of the peak
files used in the session. It can prove useful if some waveforms are not
used anymore, or if a graphical or time glitch happens.

## Clean-up Unused Sources...
{#clean_up_unused_sources}

Recording usually leaves a lot of unused takes behind, be it in midi or
audio form, that can clutter the Region List, and eat up a lot of hard
drive space. While its generally a good practice to keep as many things
as possible while recording, when transferring or archiving the session,
some clean up can help a lot in reducing the sessions clutter and size.

Selecting [Clean-up Unused Sources...]{.kbd .menu} will force Ardour to
detect those unused waveforms by looking for unused regions, and
(through a prompt) for unused playlists. The media files will not be
destroyed, though. At this stage, they are just copied in a particular
place of the session path (namely, in the `dead sounds/` sub-folder).

## Flush Wastebasket
{#flush_wastebasket}

Although Ardour is a *non-destructive* audio-editor, it allows for a
very careful destruction of unused media materials. This function is
closely linked to the previous one. When the unused sources have been
cleaned up and quarantined, the [Flush Wastebasket]{.kbd .menu} menu
will allow for their physical destruction.

As a safeguarding mechanism though, Flushing the wastebasket in
impossible in the same working session as the Cleaning up of unused
sources: the user needs to close the session and reload it before
flushing. It allows to test the playback of the session and ensure both
that Ardour did not commit any mistake (unlikely, but better safe than
sorry), and that the user is absolutely sure of what he does.

All media destroyed this way is not sent to the system\'s *trash can*
but permanently deleted. If a file is mistakenly destroyed this way, the
user will have to rely on data recovery techniques to try getting it
back.
