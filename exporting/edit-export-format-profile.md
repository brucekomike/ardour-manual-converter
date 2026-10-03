# Export Format Profiles
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/edit-export-format-profile.png"
alt="The &#39;Edit Export Format Profile&#39; dialog" />
<figcaption aria-hidden="true">The 'Edit Export Format Profile'
dialog</figcaption>
</figure>

An Export Format Profile specifies the file format in which Ardour will
export audio files, and also other audio file export options.

Export Format Profiles are edited via the [Edit Export Format
Profile]{.kbd .menu} dialog.

## Label

The [Label]{.kbd .menu} field allows to choose the name which will be
shown for this format in the drop-down list of export formats in the
\'File Formats\' tab of the [Export dialog](@@export-dialog).

## Pre-Process

If enabled, levels of exported files will be normalized to the level
chosen here. The normalization can be either:

-   Peak, which adjusts the gain to bring the highest signal peak to the
    chosen level (in dBFS),
-   Loudness, which adjusts the gain to bring the average amplitude to
    the chosen level (in LUFS), without exceeding the chosen true-peak
    value (in dBTP). EBU R128 is only available for mono or stereo
    sounds while true-peak works for any channel layout.

### Trim silence at start/end
{#trim-silence-at-start-end}

These checkboxes allow to remove any part Ardour considers silent (\<
−90dB), at the beginning or/and end of each exported track.

### Add silence at start/end
{#add-silence-at-start-end}

These checkboxes allow to add silence at the beginning or/and end of
each exported track. The duration of the added silence can be manually
fixed in the adjacent \'timer\' input fields.

## Watermark

This section adds watermarks to the exported audio (e.g. for
limited/demo distribution), by overwriting part of the audio with white
noise in the exported file.

Both the [Mode]{.dfn} (how often and how long) and [Noise Level]{.dfn}
(how loud) can be set.

## Format

### Compatibility

Selecting an item in the \'Compatibility\' emphasizes the settings in
the other columns that are compatible with the selected standard, by
turning incompatible options red. When an incompatible
quality/format/sample rate is selected, the compatibility column
checkbox disappears.

### Quality

The appropriate item in the \'Quality\' column will be highlighted when
a file format is chosen. At the moment, selecting a Quality setting does
not show the compatible File formats.

### File format

This column contains a list of Ardour\'s supported export file types.
Selecting one updates the options underneath it.

Note: For MP3 export Ardour relies on libsndfile v1.1.0 and newer to
encode the file. For Opus support, Ardour requires a build of libsndfile
from git (or future 1.2.0 release). This comes bundled with official
Ardour binaries.

### Sample rate

A specific sample rate can be chosen for the exported files, or the
current session\'s sample rate (by choosing \'Session rate\'), without
sample rate conversion.

## Encoding

Options relevant to the chosen file format will appear just to the right
of the Compatibility/Quality/File format/Sample rate table.

### Sample rate conversion quality

In case the chosen sample rate does not match the current session\'s
sample rate, the sample rate conversion quality can be chosen here.
Better quality options are slower.

## Metadata

These options are presented whatever the chosen format is:

### Tag file with session\'s metadata

If the exported file format supports metadata (e.g. FLAC, Ogg Vorbis),
use data entered in the [Session Metadata](@@metadata) window to tag the
exported files.

### Create CUE/TOC/chapter mark file
{#create-toc-cue-chapter-mark-file}

As well as exporting an audio file, Ardour can create a file (in CUE,
TOC or MP4ch format respectively) containing CD track information, as
defined in the [Ranges & Marks List](@@the-ranges-and-marks-lists).
Those files can then be used to either burn a CD or DVD, or to create
\"chapters\" inside a compatible mp4 video container.

## Post Export

If this is not blank, it is considered as a command to be run after the
export of each file. Either the command must exist in \$PATH, or an
absolute path to an executable file can be specified here.

Certain sequences are allowed here to stand for the exported file name
and various parameters. Currently these are:

-   [%a]{.dfn}: Artist name
-   [%b]{.dfn}: File\'s base-name
-   [%c]{.dfn}: Copyright
-   [%d]{.dfn}: File\'s directory
-   [%f]{.dfn}: File\'s full absolute path
-   [%l]{.dfn}: Lyricist
-   [%n]{.dfn}: Session name
-   [%o]{.dfn}: Conductor
-   [%t]{.dfn}: Title
-   [%z]{.dfn}: Organization
-   [%A]{.dfn}: Album
-   [%C]{.dfn}: Comment
-   [%E]{.dfn}: Engineer
-   [%G]{.dfn}: Genre
-   [%L]{.dfn}: Total track count
-   [%M]{.dfn}: Mixer
-   [%N]{.dfn}: Timespan name
-   [%O]{.dfn}: Composer
-   [%P]{.dfn}: Producer
-   [%S]{.dfn}: Disc subtitle
-   [%T]{.dfn}: Track number
-   [%Y]{.dfn}: Year
-   [%Z]{.dfn}: Country

Any part of the command-line enclosed in double-quotes (\") will be used
as-is.

For example, exporting an mp3 file can be done by inserting
`lame -b320 %f` which will convert the exported audio file (\'%f\') to a
320 kbs mp3 using the lame encoder (provided lame is installed first on
the system).
