# Stretching
The Stretch Mode tool can be switched to by selecting it in the
[Toolbox](@@toolbox), or simply by hitting the [T]{.kbd .menu} key.

It allows to extend or reduce the duration of a region, optionally
maintaining its pitch. This is one of the few operations in Ardour that
affect the underlying audio data from a region, even if the original
audio is kept safely---no data is lost in the process.

This operation is usually used to fit an audio sequence with a different
rhythm into a session, but can be used in a wide area of cases, due to
its ability to maintain or alter the pitch.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/before-stretch.png"
alt="region arrangement before the stretch" /> <img
src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/while-stretch.png"
alt="region arrangement while stretching" /> <img
src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/after-stretch.png"
alt="region arrangement after the stretch" />
<figcaption>Using the Stretch Mode tool. Before stretching, while
stretching, and after a stretch</figcaption>
</figure>

The Stretch Mode tool is very similar in use to doing a trim in grab
mode: the boundary (start or end) is [left]{.kbd .mouse}-clicked and
dragged to its wanted position. Notice a timer appearing, showing the
new duration of the region using the same [clock mode](@@editing-clocks)
as in the [primary transport clock](@@transport-clocks).

Stretching is a complex operation (phase vocoding), involving
resampling, frequency analysis and synthesis. The parameters used to
transform the audio data are user tweakable, and exposed to the user as
the [ left]{.kbd .mouse} mouse button is released:

![The Time Stretch Audio window](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/time-stretch-audio.png)

The Time Stretch Audio window is made of:

|                                  |                                                                                                                                                                              |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Duration]{.dfn}                 | The target duration of the region, expressed using the primary transport clock\'s mode                                                                                       |
| [Percent]{.dfn}                  | The target duration of the region, expressed as a percentage of the region\'s original length. Can be either higher than 100% (to expand the region) or lower (to shrink it) |
| [Contents]{.dfn}                 | The type of audio the region is made of. Ardour will fine-tune its algorithm based on this content, see below                                                                |
| [Minimize time distortion]{.dfn} | Tries to reduce the smearing of the audio created by the phase vocoding process                                                                                              |
| a [Progress]{.dfn} bar           | showing the operation in progress.                                                                                                                                           |

The *Contents* should be selected to best fit the actual content of the
region. The \"Any\" option is a general purpose option that uses the
StaffPad algorithm. The other options use the Rubber Band algorithm in
the following configurations:

|                                                   |                                               |                                                |                                           |                                                     |                               |
|---------------------------------------------------|-----------------------------------------------|------------------------------------------------|-------------------------------------------|-----------------------------------------------------|-------------------------------|
| Content                                           | Disable phase resynchronisation at transients | Band-limit phase resync to extreme frequencies | Disable phase locking to peak frequencies | Use longer processing window (actual size may vary) | Use shorter processing window |
| [Mushy]{.dfn}                                     | X                                             |                                                | X                                         | X                                                   |                               |
| [Smooth]{.dfn}                                    | X                                             |                                                | X                                         |                                                     |                               |
| [Balanced multitimbral mixture]{.dfn}             | X                                             |                                                |                                           |                                                     |                               |
| [Unpitched percussion with stable notes]{.dfn}    |                                               | X                                              |                                           |                                                     |                               |
| [Crisp monophonic instrumental]{.dfn} (*default*) |                                               |                                                |                                           |                                                     |                               |
| [Unpitched solo percussion]{.dfn}                 |                                               |                                                | X                                         |                                                     | X                             |
| [Resample without preserving pitch]{.dfn}         | *see below*                                   |                                                |                                           |                                                     |                               |

While the table above details *how* the different kinds of audio
material alter the fine-tuning of the DSP, from an user point of view,
the operation often consists in trying different settings and listening
to the result.

The best way to start experimenting is to consider the material itself:

-   If the material doesn\'t need its pitch to be preserved, the best
    choice is *Resample without preserving pitch*
-   For drum-type material, the best choice is (depending on the
    transients crispness, stretching factor\...) one of the two
    *percussion* types
-   For melodic mono-tonal material (bass, winds,...), the best (and
    default) choice is *Crisp monophonic instrumental*
-   For multi-tonal material (chords,...), either one of the three first
    choice, or the default *Crisp*.
