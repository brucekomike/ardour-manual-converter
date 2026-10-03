# Tempo and Time Signature
Tempo and time signature belong together. Without both, there is no way
to know where a beat lies in time.

Tempo provides a musical pulse, which is divided into beats and bars by
a time signature. When tempo is changed or an audio-locked time
signature is moved, all objects on the timeline that are glued to bars
and beats (locations, regions) will move in sympathy.

When performing time signature or tempo operations, it is advisable to
use the BBT ruler (available by right-clicking an existing marker or
ruler name), and ensure that the constraint modifier is set ([]{.kbd
.mod3n} by default, may be changed in [Preferences \> Editor \>
Modifiers]{.kbd .menu}) so that no other modifiers share its key
combination. The constraint modifier is the \"Constrain drags using: \"
setting under the \"When Beginning a Drag\" heading. One viable setting
is []{.kbd .mod1n}[]{.kbd .mod3n}.

### Tempo

Tempo can be adjusted in several ways:

-   By double clicking on a tempo marker. This opens the tempo dialog
    which allows entering the tempo directly into an entry box.
-   By using the constraint modifier ([]{.kbd .mod3n} by default, may be
    changed in [Preferences \> Editor \> Modifiers]{.kbd .menu}) to drag
    the beat/bars in the BBT ruler or the tempo/time signature lines.
    This is the preferred way to match the tempo to previously recorded
    material.
-   by holding down the constraint modifier while dragging a tempo
    vertically. This is used for more complex tempo solving, as it
    allows changing of the position and tempo of a tempo marker in the
    same drag; it is, however, a useful way to adjust the first tempo
    for a quick result.

A tempo may be locked to audio or musical time. This can be changed by
[right]{.kbd .mouse}-clicking on a tempo. If a tempo is locked to music,
an entry will be available to lock it to audio. Similarly an
audio-locked tempo may be locked to music by [right]{.kbd
.mouse}-clicking it and selecting the \"Lock to Music\" entry.

Audio locked tempo marks stay in their frame position as their
neighbor\'s positions are altered. Their pulse (musical) position will
change as their neighbors move. Music locked tempo marks move their
frame position as their neighbors are moved, but keep their pulse
position (they will move as the music is moved).

A tempo may be constant or ramped:

-   A constant tempo will keep the session tempo constant until the next
    tempo section, at which time it will jump instantly to the next
    tempo. These are mostly useful abrupt changes, and is the way in
    which traditional DAWs deal with tempo changes (abrupt jumps in
    tempo).
-   A ramped tempo increases its tempo over time so that when the next
    tempo section has arrived, the session tempo is the same as the
    second one. This is useful for matching the session tempo to music
    which has been recorded without a metronome. Ramps may also be used
    as a compositional tool, but more on this later. Note that a ramp
    requires two points---a start and an end tempo. The first tempo in a
    new session is ramped, but appears to be constant as it has no tempo
    to ramp to. It is only when a new tempo is added and one of them is
    adjusted that a ramp will be heard. The same applies to the last
    tempo in the session---it will always appear to be constant until a
    new last tempo is added and changed.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/constant-tempo.png"
alt="A constant tempo displaying the tempo at the playhead in the audio clock" />
<figcaption>A series of constant tempo markers. The tempo at the
playhead position is the same as the previous tempo.</figcaption>
</figure>

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/ramped-tempo.png"
alt="A ramped tempo displaying the tempo at the playhead in the audio clock" />
<figcaption>A ramped tempo marker. The tempo at the playhead position is
approaching the second tempo. Because the playhead is equidistant (in
beats) between the two markers, the tempo at the playhead is the average
of the two.</figcaption>
</figure>

To add a new tempo, [right]{.kbd .mod1 .mouse}-click on the tempo line
at the desired position. The new tempo will be the same as the tempo at
the position of the mouse click (it will not change the shape of the
ramp).

To copy a tempo, use [right]{.kbd .mod1 .mouse} button to drag the tempo
to be copied.

### Time signature

Time signature positions beats using the musical pulse of a tempo, and
groups them into bars using its number of divisions per bar.

The first time signature in a new session may be moved freely. It has an
associated tempo which cannot be dragged by itself (although all others
can). It can be moved freely and is locked to audio.

New time signatures are locked to music. They may only occur on a bar
line if music locked.

An audio locked time signature provides a way to cope with musical
passages which have no time signature (rubato, pause), or to allow a
film composer to insert a break in music which cannot be counted in
beats.

If a time signature is audio-locked, its bar number is fixed from the
point at which it left the main score. That bar number cannot be
changed, nor can tempo motion allow the previous bar to overlap. If
another bar is needed, lock the time signature to music again
([right]{.kbd .mouse} \> [Lock to Music]{.kbd .menu}), drag the time
signature to the desired bar and re-lock to audio. The new bar can be
freely dragged again.

-   To change a time signature, double-click it. A dialog will appear.
-   To copy a time signature, hold down []{.kbd .mod1n} and drag it.
