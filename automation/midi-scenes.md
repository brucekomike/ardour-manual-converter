# MIDI Scene Automation
Ardour is capable of being used to both record and deliver MIDI
\"scene\" automation. These are MIDI messages typically used to switch
presets or \"scenes\" on a variety of external equipment (or software),
including lighting and other audio/video tools. A common use case is to
automatically change presets between songs or to change lighting
conditions based on a specific position on the timeline.

Each change from one scene to another is represented by a marker in the
\"Marker\" bar.

Typically, scene changes are delivered as a combination of bank and
program change MIDI messages. MIDI allows for 16384 banks, each with 128
programs.

## Recording Scene Changes

Ardour has a dedicated MIDI port named \"Scene In\". Recording scene
changes can be done by connecting this port to whatever source(s) of
MIDI scene (bank/program change) messages should be recorded.

Whenever the global record enable button is engaged and Ardour\'s
transport is rolling, a new marker will be created for each scene change
message received via the \"Scene In\" port. Markers created for MIDI
scene changes are automatically named as \"scene \[N\]\", where N is the
program number that Ardour captured.

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/midi-scene-change-ruler.png" style="width:100.0%"
alt="MIDI scene change marker on the ruler" />
<figcaption aria-hidden="true">MIDI scene change marker on the
ruler</figcaption>
</figure>

Ardour will also capture program change events as MIDI data and display
them inside MIDI regions.

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/pg-change-in-midi-region.png" style="width:100.0%"
alt="Program change marker inside a MIDI region" />
<figcaption aria-hidden="true">Program change marker inside a MIDI
region</figcaption>
</figure>

If two different scene changes are received within a certain time
period, only the later one will be recorded as a new marker. The default
threshold for this is 1 millisecond.

If a scene change message is received while the playhead is close to an
existing marker with an associated scene change, the recording process
will alter the scene change in the existing marker rather than adding a
new one. The default threshold for this \"proximity\" test is 1
millisecond.

## Manually Creating Scene Changes

All location markers carry MIDI scene change information, thus adding a
new location marker creates a scene change. Whether this information is
processed depends on what plugin, software, or hardware unit is
listening to the MIDI events that Ardour transmits.

## Playing Back Scene Changes

Ardour has a dedicated MIDI port named \"Scene Out\". Playing back scene
changes can be done by connecting this port to whatever target(s) of
MIDI scene (bank/program change) messages should be sent to.

When the global record enable button is *not* enabled, the relevant
message(s) will be sent via the \"Scene Out\" port as the playhead rolls
past each marker with a scene change associated with it.

## Editing Scene Changes

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/edit-midi-scene-change.png" class="mini"
alt="Edit MIDI scene change" />
<figcaption>Editing MIDI scene change</figcaption>
</figure>

To edit a MIDI scene change, double-click on a location marker and
change program number, bank number, and channel number as required, and
click [Edit]{.kbd .key} to confirm the changes.

To reset scene change to defaults (program number 1, bank number 1,
channel 1), double-click on a location marker, enable the [Clear scene
change]{.kbd .gui} checkbox, and click [Edit]{.kbd .key}.

## Disabling Scene Changes

This feature is not currently implemented. However, you can prevent MIDI
scene change data from being transmitted outside Ardour. To do that,
disconnect the Scene Out port from whatever port it is connected to.
