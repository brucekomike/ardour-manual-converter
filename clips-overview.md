# Clips Overview
The [Clips]{.dfn} browser provides a way to easily reuse little pieces
of music across sessions. You can also drop audio and MIDI clips on a
timeline in the [Editor window](@@clips-in-the-editor) or use them in
trigger slots in the [Cue window](@@clips-in-the-cue-window).

## Clips Browser Interface

In the Editor window, the Clips browser is part of the Editor sidebar
and thus can be hidden from the main window. In the Cue window, the
Clips browser is an essential part of the workflow and is always
visible.

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/clips-browser.png" width="400"
alt="The Clips browser" />
<figcaption aria-hidden="true">The Clips browser</figcaption>
</figure>

The Clips browser has three main parts:

1.  Selector of clip library locations
2.  List of clips, with a treeview where necessary
3.  Preview options

## Library Locations

The [Clips]{.dfn} browser is capable of handling multiple locations of
clips and loops. There are several types of locations supported by the
browser:

1.  [Ardour Bundled Content]{.dfn}: these are all the audio and MIDI
    files shipped along with an official Ardour build.
2.  [FreeSound]{.dfn}: all clips previously downloaded from
    FreeSound.org.
3.  [Custom folder]{.dfn}: it\'s a single user-defined location on a
    local or remote disk that you can write to. The folder is defined on
    the [Triggering]{.kbd .menu} page of the [Preferences]{.kbd .menu}
    dialog and is preserved across sessions.
4.  [Additional locations]{.dfn}: typically those are locations where
    you store existing clips/loops libraries acquired elsewhere. You can
    have as many as you like, please see [Adding 3rd Party Clip
    Libraries](@@adding-3rd-party-clip-libraries) chapter for more info.
    These locations are also preserved across sessions.
5.  [Other locations]{.dfn}: this is a one-off access to a location
    where clips and loops are stored. This location is not preserved
    across sessions.

## List of Clips

The Clips browser will provide access to all supported media file types
available in a selected location. Typically those would be, WAV, FLAC,
and MID files.

If there are subfolders in the clip library\'s folder, the Clips browser
will display them using as a tree view. The browser will also lazy-load
subfolders: instead of loading the entire list of all supported files in
the library location, it will only display top-level folders and load
their content when you start expanding subfolders you are interested in.

## Preview Options

The preview section has simple playback controls, a volume control, as
well as an option to automatically play back a clip when you click it in
the list. For MIDI clips, you can also select a virtual instrument
(Ardour defaults to ACE Reasonable Synth).

When playing a clip, Ardour will automatically pause the transport and
resume playback when the clip playback is done. Ardour will also use the
audition channel for playback, so you can control the preview volume
using the monitor level control in the [Monitor](@@monitor-section)
section of the [Mixer]{.dfn}.
