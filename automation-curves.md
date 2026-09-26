# Automation Curves
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/automation-curve1.png" />
<figcaption>A typical automation curve.</figcaption>
</figure>

An [automation curve]{.dfn} is a series of lines connected by [control
points]{.dfn} that typically defines a continuous line. As the curve is
traversed from left to right, the line defines the level of the
parameter controlled by the automation lane.

There are two types of automation curves: [Linear]{.kbd .menu} and
[Discrete]{.kbd .menu}. The most common type is [Linear]{.kbd .menu}, in
which the space between any two contiguous control points is
continuously interpolated; in other words, the values between any two
contiguous control points at any given time is given by the straight
line connecting them. The second type of automation curve is
[Discrete]{.kbd .menu}, in which no interpolation between control points
is done; whatever value the control point is set at is the value it will
yield until it reaches the next control point, at which point it will
give that value until the next control point, and so on until there are
no more control points.

The curve by itself does nothing; it will *only* control playback if the
lane it resides in is in [Play]{.kbd .menu} mode.
