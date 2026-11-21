# Video Timeline Setup
No configuration is required if everything is to meant be run on a
single machine, and the version of Ardour comes from
<http://www.ardour.org>. Everything is pre-configured and included with
the download/install.

## Single Machine

If Ardour is compiled from source, or installed from a 3rd party
repository, three additional tools will need to be installed manually,
which are used by Ardour to provide video features:

- xjadeo (the video monitor application):
  [http://xjadeo.sf.net](http://xjadeo.sourceforge.net/ "http://xjadeo.sourceforge.net/"){rel="nofollow"}
- harvid (a video decoder used for the thumbnail timeline):
  [http://x42.github.com/harvid/](http://x42.github.io/harvid/ "http://x42.github.io/harvid/"){rel="nofollow"}
- ffmpeg, ffprobe (used to import/export video, extract soundtracks and
  query video information and encode mp3 for export):
  [http://ffmpeg.org](http://ffmpeg.org "http://ffmpeg.org"){rel="nofollow"}

Ardour requires xjadeo ≥ version 0.6.4, harvid ≥ version 0.7.0 and
ffmpeg (known to work versions: 1.2, 2.8.2, 5.0)

The Ardour development team is in control of the first two applications.
ffmpeg however can be a bit of a problem. To avoid conflicts with
distribution packages, Ardour looks for `ffmpeg_harvid` and
`ffprobe_harvid`.

All four applications need to be found in `$PATH` (e.g. `$HOME/bin` or
`/usr/local/bin`). For convenience the binary releases of harvid include
ffmpeg_harvid and ffprobe_harvid. Ardour binaries from ardour.org do
include all relevant tools and most GNU/Linux distributions also provide
those.

Binary releases of the video-tools are available from ardour.org via a
dedicated installer script:
[install_video_tools.sh](https://github.com/Ardour/ardour/blob/master/tools/videotimeline/install_video_tools.sh "https://github.com/Ardour/ardour/blob/master/tools/videotimeline/install_video_tools.sh"){rel="nofollow"}.

The easiest way to install the video-utilities on Linux is by running
the following line in a terminal:

[sh -c \"\$(curl -s -L http://git.io/tVUCkw)\"]{.kbd .cmd .lin}

## Studio Setup

As Setting up a proper A/V post-production studio can be a complicated
task, it is advised to read the info in the previous section to get
familiar with the tools involved first. As much as the Ardour team
streamlines and simplifies the *single machine* setup, the [studio
setup]{.dfn} is focused on modularity.

- TODO:
- Synchronization ardour → video-display-box should be accomplished by
  external means. Jack-transport(netjack), MTC, LTC ([OSC]{.abbr
  title="Open Sound Control—\"postmodern MIDI\""} and/or ssh-pipe work
  but introduce additional latency + jitter)
- Ardour launches `XJREMOTE` (environment variable, default \'xjremote\'
  which comes with xjadeo).
- Either use a custom shell script that ssh\'es into the remote box and
  launches/controls xjadeo there, selects the sync-source and passes
  though communication between ardour ⇔ xjadeo via ssh (xjadeo is
  launched stopped with the session).
- ...or override xjremote\'s behavior---instead of IPC with a local
  running xjadeo-process, using [OSC]{.abbr title="Open Sound
      Control—\"postmodern MIDI\""} for example. Xjadeo would run
  permanently and Ardour will just tell it to load files and set offsets
  via OSC. See
  [xjremote-osc](http://xjadeo.git.sourceforge.net/git/gitweb.cgi?p=xjadeo/xjadeo;a=blob_plain;f=contrib/xjremote-osc "http://xjadeo.git.sourceforge.net/git/gitweb.cgi?p=xjadeo/xjadeo;a=blob_plain;f=contrib/xjremote-osc"){rel="nofollow"}
  example script.
- If the video server runs remotely, Ardour needs to be configured in
  Ardour \> Preference \> Video (hostname of the video-server).
- Ideally the machines have a common shared folder (NFS or similar).
  Ardour\'s import (audio-extract) and export (mux) functionality
  depends on having access to the video file. Also Ardour\'s
  video-import transcodes the file into a suitable proxy-format that
  allows reliable seeking to any frame...
