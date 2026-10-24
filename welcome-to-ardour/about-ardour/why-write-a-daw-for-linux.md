# Why Write a DAW for Linux?
There are already a number of excellent digital audio workstations. To
mention just a few: ProTools, Nuendo, Samplitude, Digital Performer,
Logic, Cubase (SX), Sonar, along with several less well known systems
such as SADIE, SAWStudio and others. Each of these programs has its
strengths and weaknesses, although over the last few years most of them
have converged on a very similar set of core features. However, each of
them suffers from two problems when seen from the perspective of
Ardour\'s development group:

- they do not run natively on Linux
- they are not available in source code form, making modifications,
  improvements, or bugfixes by technically inclined users or their
  friends or consultants impossible.

It is fairly understandable that most existing proprietary DAWs do not
run on Linux, given the rather small (but growing) share of the desktop
market that Linux has. However, when surveying the landscape of
\"popular operating systems\", we find:

- older versions of Windows: plagued by abysmal stability and appalling
  security
- newer versions of Windows seem stable but still suffer from security
  problems
- macOS: a nice piece of engineering that is excellent for audio work
  but only runs on proprietary hardware and still lacks the flexibility
  and adaptability of Linux.

Security matters today, and will matter more in the future as more and
more live or semi-live network based collaborations take place.

Let\'s contrast this with Linux, an operating system which:

- can stay up for months (or even years) without issues
- is endlessly configurable down to the tiniest detail
- is not owned by any single corporate entity, ensuring its life and
  direction are not intertwined with that of a company (for a contrary
  example, consider BeOS)
- is fast and efficient
- runs on almost any computing platform ever created, including old
  \"slow\" systems and new \"tiny\" systems (e.g. Raspberry Pi)
- is one of the most secure operating systems \"out of the box\"

More than anything, however, Ardour\'s primary author uses Linux and
wanted a DAW that ran there.

Having written a DAW for Linux, it turned out to be relatively easy to
port Ardour to macOS, mostly because of the excellent work done by the
JACK development group that ported JACK to macOS.
