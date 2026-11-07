# Transcoding, Formats and Codecs
This chapter provides a short primer on video files, formats and codecs
-- because it is often cause for confusion:

A video file is a [container]{.dfn}. It usually contains one [video
track]{.dfn}, one or more [audio tracks]{.dfn}, and possibly [
subtitle]{.dfn} tracks, [chapters]{.dfn}... The way these tracks are
stored in the file is defined by the [file format]{.dfn}. Common formats
are avi, mov, ogg, mkv, mpeg, mpeg-ts, mp4, flv, or vob.

Each of the tracks by itself is encoded using a [[Codec]{.dfn}]{.abbr
title="Coder-Decoder"}. Common video codecs are h264, mpeg2, mpeg4,
theora, mjpeg, wmv3. Common audio codecs are mp2, mp3, dts, aac,
wav/pcm.

Not all codecs can be packed into a given format. For example the mpeg
format is limited to mpeg2, mpeg4 and mp3 codecs (not entirely true).
DVDs do have stringent limitations as well. The opposite would be .avi:
pretty much every audio/video codec combination can be contained in an
avi file-format.

To make things worse, naming conventions for video codecs and formats
are often identical (especially MPEG ones) which leads to confusion. All
in all it is a very wide and deep field. Suffice there are different
uses for different codecs and formats.

## Ardour specific issues

Ardour supports a wide variety of video file formats codecs. More
specifically, Ardour itself actually does not support any video at all
but delegates handling of video files to [ffmpeg](http://ffmpeg.org/),
which supports over 350 different video codecs and more than 250 file
formats.

When importing a video into Ardour, it will be [transcoded]{.dfn}
(changed from one format and codec to another) to avi/mjpeg for internal
use (this allows reliable seeking to frames at low CPU cost---the file
size will increase, but hard disks are large and fast).

The export dialog includes presets for common format and codec
combinations (such as DVD, web-video,..). If in doubt, one of the
presets should be used.

As a last note: every time a video is transcoded, the quality can only
get worse. Hence for the final mastering/[muxing]{.abbr
title="Multiplexing Audio and Video"} process, one should always go back
and use the original source of the video.
