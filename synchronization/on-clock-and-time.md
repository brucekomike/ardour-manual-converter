# On Clock and Time
[Synchronization]{.dfn} in multimedia involves two concepts which are
often confused: [clock]{.dfn} (or speed) and [time]{.dfn} (location in
time).

A [clock]{.dfn} determines the speed at which one or more systems
operate. In the audio world this is generally referred to as [Word
Clock](https://en.wikipedia.org/wiki/Word_clock "https://en.wikipedia.org/wiki/Word_clock").
It does not carry any absolute reference to a point in time: A clock is
used to keep a system\'s sample rate regular and accurate. Word clock is
usually at the frequency of the sample rate---at 48 kHz, its period is
about 20 μs. Word Clock is the most common sample rate based clock but
other clocks do exist such as Black and Burst, Tri-Level and DARS.
Sample rates can be derived from these clocks as well.

Time or [timecode]{.dfn} specifies an absolute position on a timeline,
such as `01:02:03:04` (expressed as Hours:Mins:Secs:Frames). It is
actual *data* and not a clock *signal* per se. The granularity of
timecode is [Video Frames]{.dfn} and is an order of magnitude lower
than, say, Word Clock which is counted in [samples]{.dfn}. A typical
frame rate is 25 [fps]{.abbr title="frames
  per second"} with a period of 40 ms. In the case of 48 kHz and 25 fps,
there are 1920 audio samples per video frame.

The concepts of clock and timecode are reflected in JACK and Ardour:

JACK (Ardour does this internally if using the ALSA backend) provides
clock synchronization and is not concerned with time code (this is not
entirely true, more on jack-transport later). On the software side,
jackd provides sample-accurate synchronization between all JACK
applications. On the hardware side, JACK and Ardour use the clock of the
audio-interface. Synchronization of multiple interfaces requires
hardware support to sync the clocks. If two interfaces run at different
clocks the only way to align the signals is via re-sampling
(SRC---Sample Rate Conversion), which is expensive in terms of CPU usage
and may decrease fidelity if done incorrectly.

Timecode is used to align systems already synchronized by a clock to a
common point in time, this is application specific and various standards
and methods exist to do this.

To make things confusing, there are possibilities to synchronize clocks
using timecode. e.g. using mechanism called [jam-sync]{.dfn} and a
[phase-locked loop]{.dfn}.

An interesting point to note is that LTC (Linear Time Code) is a
Manchester encoded, frequency modulated signal that carries both clock
and time. It is possible to extract absolute position data and speed
from it.
