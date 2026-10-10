# Automation States
In order to understand how automation in Ardour works, it is necessary
to understand the five states of automation. They are: [Manual]{.kbd
.menu}, [Play]{.kbd .menu}, [Write]{.kbd .menu}, [Touch]{.kbd .menu},
and [Latch]{.kbd .menu}.

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/automation-modes1.png" />
<figcaption>The automation state menu.</figcaption>
</figure>

[Manual]{.kbd .menu} state is basically analogous to a processor\'s
bypass switch. Whenever an automation lane is in this state, it is
inactive and any level that is manually set for controlling the lane\'s
parameter will persist during playback like normal.

In Ardour, every track and processor parameter is initially set to
[Manual]{.kbd .menu} state.

[Play]{.kbd .menu} state tells Ardour to use the automation curve in the
automation lane to control the level of the parameter controlled by the
lane *during playback*. The control that normally sets the parameter
will be *unresponsive to manual input* and will move automatically in
accord with the lane\'s automation curve during playback.

[Write]{.kbd .menu} state allows continuous, dynamic setting of a
control during playback; all such settings are written to the lane the
control is in. This defines the lane\'s automation curve in the interval
being played, and overwrites any existing automation curve in the lane
being manipulated. As this might be sometimes dangerous, this state is
automatically changed to [Touch]{.kbd .menu} state when playing is
stopped.

[Touch]{.kbd .menu} state is similar to [Write]{.kbd .menu} state,
except it only overwrites sections of a lane\'s automation curve when
the control is changed in some way. This allows for changing only the
parts of an automation curve that are desired to be changed, while
leaving the rest unchanged.

[Latch]{.kbd .menu} state is similar to [Touch]{.kbd .menu} state as it
will also change automation when the control is changed in some way
during session play back. But additionally it will overwrite the
automation curve with the last value that it was changed to until
play-back is stopped.\
Latch state is also useful when the user wants Touch-style behavior but
is using a device incapable of sending messages to indicate the start
and end of the \"touch\".
