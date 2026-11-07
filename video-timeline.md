# Video Timeline and Monitoring
Ardour offers a [video timeline]{.dfn} and [video monitoring]{.dfn} for
convenient audio mixing and editing to video, in order to produce film
soundtracks and music videos, or perform TV post-production tasks.

The video capabilities are:

- Import a single video and optionally extract the soundtrack from it.
- Provide a video monitor window, or full-screen display, of the
  imported video in sync with any of the available Ardour timecode
  sources.
- Display a frame-by-frame (thumbnail) timeline of the video.
- Allow for a configurable timecode offset.
- *Lock* audio regions to the video.
- Move audio regions with the video at video-frame granularity.
- Export the video, trim start and end, add blank frames and/or
  multiplex it with the soundtrack of the current session.

The setup of the video subsystem is modular and can be configured in
different ways, including:

- One machine for all video decoding, video monitoring and audio editing
  tasks
- Two machines, one for video monitoring, one for Ardour
- Three machines, separate video server (for timeline decoding and file
  archive), dedicated video monitor, and Ardour

Ardour does *not*:

- allow for more than one video to be loaded at a time.
- provide video editing capabilities
