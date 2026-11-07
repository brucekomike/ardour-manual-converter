# Waveform display
The display of [waveforms]{.dfn} (or, more correctly, [peak
envelopes]{.dfn}, since the actual waveform is only visible at the
highest zoom levels) is configurable via the [Edit \> Preferences \>
Appearance \> Editor]{.kbd .menu} dialog, to support different use cases
and user preferences. The following options are available:

```{eval-rst}
+----------------------+----------------------+----------------------+
| Show waveforms in    | By default, Ardour draws waveforms within   |
| regions              | audio regions. Disable this option to hide  |
|                      | them.                                       |
+----------------------+----------------------+----------------------+
| Waveform scale       | Linear               | This is the          |
|                      |                      | traditional          |
|                      |                      | [linear]{.dfn} (1:1) |
|                      |                      | display of the peak  |
|                      |                      | envelope, or, at     |
|                      |                      | higher zoom levels,  |
|                      |                      | the individual       |
|                      |                      | samples.             |
|                      +----------------------+----------------------+
|                      | Logarithmic          | Alternatively, a     |
|                      |                      | [logarithmic]{.dfn}  |
|                      |                      | display of the peak  |
|                      |                      | envelope can be      |
|                      |                      | used. This will give |
|                      |                      | a better idea of     |
|                      |                      | program loudness (it |
|                      |                      | is similar to dBs)   |
|                      |                      | and plot soft        |
|                      |                      | passages more        |
|                      |                      | clearly, which is    |
|                      |                      | useful for soft      |
|                      |                      | recordings or small  |
|                      |                      | track height.        |
+----------------------+----------------------+----------------------+
| Waveform shape       | Traditional          | The [zero]{.dfn}     |
|                      |                      | line appears in the  |
|                      |                      | middle of the        |
|                      |                      | display and          |
|                      |                      | waveforms appear as  |
|                      |                      | positive and         |
|                      |                      | negative peaks above |
|                      |                      | *and* below.         |
|                      +----------------------+----------------------+
|                      | Rectified            | The zero line        |
|                      |                      | appears at the       |
|                      |                      | bottom of the        |
|                      |                      | display and          |
|                      |                      | waveforms appear as  |
|                      |                      | absolute peaks       |
|                      |                      | *above* the line     |
|                      |                      | only.                |
+----------------------+----------------------+----------------------+
```
