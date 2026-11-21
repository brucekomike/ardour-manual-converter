# Supported File Formats
Ardour supports all common audio file formats, including WAV, FLAC,
Ogg/Vorbis, Ogg/Opus, AIFF, AIFC, CAF, W64 and BWF, with all typical
sample formats (8-, 16-, 24-, 32-bit integer, floating point, and more).

The list of audio file formats that Ardour can understand is quite long.
Most formats are supported based on the functionality offered by
[libsndfile]{.dfn}, an excellent and widely used software library by
Australian programmer Erik de Castro Lopo.

A full list of libsndfile\'s supported formats is available on the
[libsndfile website](http://www.mega-nerd.com/libsndfile/#Features).

In addition, Ardour also supports MP3 lossy compression format files. We
do not recommend importing these for any serious work, but the option is
available if you are forced to use such files.

For MIDI import, Ardour will read any Standard MIDI Format (SMF) file.
