# Session Metadata
## Session Metadata

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/edit-session-metadata.png"
alt="The session metadata editor" />
<figcaption aria-hidden="true">The session metadata editor</figcaption>
</figure>

Sessions can have various items of metadata attached to them, and saved
in the session file. These metadata are filled by the user via [Session
\> Metadata \> Edit Metadata...]{.kbd .menu}.

These metadata will be exported as tags in the audio and video files
that support it, as long as the right option is chosen at the
[export](@@export-dialog) stage. All the video format can retain a
subset of the metadata if the [Include Session Metadata]{.kbd .option}
is checked in the [export video](@@workflow-amp-operations#export)
window, while only the Ogg-Vorbis (tagged) and FLAC (tagged) audio
format will be exported with the metadata (as Vorbis comment).

Ardour can also reuse the metadata from another session file in the
current session, with [Session \> Metadata \> Import Metadata...]{.kbd
.menu}. This menu brings up a file selector, asking for the source
ardour session file to extract the data from. This can be handy when
reusing a lot of information (Author, Artist Name, etc...) or working on
multiple tracks of the same media.
