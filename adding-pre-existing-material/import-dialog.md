# Import Dialog
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/import-window.png" style="width:75.0%"
alt="The import window" />
<figcaption>The import window.</figcaption>
</figure>

Many sessions will require the use of [existing material]{.dfn}, whether
it consists of audio and/or MIDI data. Using existing samples, loops and
riffs from files stored on the system can be the basis for a new
session, or a way to deepen and improve one that is already underway.

Importing audio and MIDI data into the session is done with the [Add
Existing Media]{.dfn} dialog, accessed either by the [ Session \>
Import]{.kbd .menu} menu or, if any tracks have already been added, by
right-clicking on the canvas of the [Editor]{.dfn} window and choosing
[Insert Existing Media]{.kbd .menu}.

## The Soundfile Information Box

This box will display information about the currently selected file:

-   number of channels,
-   sample rate,
-   file format,
-   length,
-   embedded timestamp (applies to some professional formats such as
    Broadcast WAVE), and
-   [tags](@@searching-for-files-using-tags) (attached metadata to help
    categorize files in a library).

If the sample rate differs from the current session rate, it is
displayed in red, which indicates that the file must be resampled before
importing.

Resampling is controlled by the [Conversion quality]{.kbd .menu} option
described below.

## Auditioner

Files can be auditioned before importing. The slider under the play and
stop buttons allows to scrub around, a fader on the right side allows to
control the playback volume.

Auditioning MIDI files requires a MIDI instrument to be chosen in the [
Instrument]{.kbd .menu} dropdown list.

## Importing options

Through the [Add files...]{.kbd .menu} option, imported files can be
inserted in the session:

|                    |                                                                                                              |
|--------------------|--------------------------------------------------------------------------------------------------------------|
| as new tracks      | automatically creates new tracks and import the files in it                                                  |
| to region list     | adds the files to the [region list](@@the-region-list), from where then can be manually dragged into a track |
| as new tape tracks | adds the files as [Tape tracks.](@@track-types)                                                              |

The [Insert at]{.kbd .menu} option chooses where in time the file will
be imported, amongst:

-   the [file timestamp]{.dfn} (if available, zero by default)
-   at the [[edit point]{.dfn}](@@edit-point-control)
-   at the [playhead]{.dfn}
-   at the [session start]{.dfn}.

The Channel [Mapping]{.kbd .menu} option is only available for
multi-channel files (i.e. all but mono ones). It is either

|                              |                                                                                                     |
|------------------------------|-----------------------------------------------------------------------------------------------------|
| one track/region per file    | Creates a multi channel track for each imported file                                                |
| one track/region per channel | Creates only mono channels, as many as there are channels in the imported files                     |
| sequence files               | If multiple files are imported, they can be sequenced into a single track in the order of selection |

The [Conversion quality]{.kbd .menu} drop-down controls the quality of
the resampling process, if the sampling rate of the source file differs
from the session rate.

There are three MIDI-specific options as well. First off, you can set a
track naming scheme:

|                    |                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| by track number    | will automatically assign every track a name that consists of the imported file name and a track number          |
| by track name      | will automatically assign every track a name that consists of the imported track\'s name and number              |
| by instrument name | will automatically assign every track a name that consists of the imported instrument\'s name and a track number |

You can also optionally import a tempo map from a MIDI file. The [Use
MIDI Tempo Map]{.kbd .menu} option appears when a MIDI file is selected
in the file selection dialog.

The last MIDI-specific option is [Import MIDI Markers]{.kbd .menu}. If
those are present in a MIDI file, they will be rendered right above MIDI
clips on the canvas. Editing the MIDI markers is currently unavailable.
If MIDI lyrics is available in the file, it was also be imported as
region markers (that can be later promoted to location markers).

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/imported-midi-markers.png" style="width:75.0%"
alt="MIDI markers imported from a .mid file" />
<figcaption aria-hidden="true">MIDI markers imported from a .mid
file</figcaption>
</figure>

Finally, and most importantly, the files can be linked or copied to the
session with the [Copy files to session]{.kbd .option} checkbox. Please
read [Copying versus Linking](@@copying-versus-linking) for details.

## Importing from FreeSound.org

Ardour can import sounds from the public library at FreeSound.org. This
feature requires an account with the online service.

Sound clips on FreeSound.org typically have metadata in form of tags
that give a general idea what sound is recorded in a clip. Ardour will
use that metadata to find sound clips that match your request.

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/freesound-clips-list.png" style="width:75.0%"
alt="List of sound clips found on FreeSound.org" />
<figcaption aria-hidden="true">List of sound clips found on
FreeSound.org</figcaption>
</figure>

There are two more options for the search:

1.  [Sort]{.dfn}: allows sorting all sound clips that match your request
    in a particular order. Changing the type of sorting requires running
    the search again.
2.  [License]{.dfn}: allows limiting your search by choosing a
    particular license depending on how you license your own work.

Ardour will list all sounds clips that match your request right in the
window. If there are a lot of option, click the [More]{.kbd .button}
button to load the next page with results.

When you click on any sound clip in the list for the first time, a
FreeSound.org login page will open in your preferred web browser.

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/freesound-login.png" style="width:75.0%"
alt="Log into FreeSound.org" />
<figcaption aria-hidden="true">Log into FreeSound.org</figcaption>
</figure>

You will then be asked to grant access to Ardour.

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/freesound-grant-access.png" style="width:75.0%"
alt="Grant access to Ardour" />
<figcaption aria-hidden="true">Grant access to Ardour</figcaption>
</figure>

Once you do that, FreeSound.org will generate authorization code that
you need to select and copy to the clipboard.

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/freesound-auth-code.png" style="width:75.0%"
alt="Authorization token" />
<figcaption>Authorization code</figcaption>
</figure>

Finally, insert the code into the entry box here and click [OK]{.kbd
.button}.

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/freesound-code-insert.png" style="width:75.0%"
alt="Insert authorization token" />
<figcaption>Insert authorization code</figcaption>
</figure>

After that, Ardour will be able to download clips for preview in a
folder for temporary files that you can select in the [Preferences]{.kbd
.window} dialog on the [General]{.kbd .windows} page.

You can preview and insert clips from FreeSound.org like any other sound
files.

Please note that authorization code only works as long as Ardour is
running. The next time you start Ardour, you will need to authorize it
again. This is implementation specifics of FreeSound.org.
