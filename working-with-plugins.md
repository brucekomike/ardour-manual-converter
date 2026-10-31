# Working With Plugins
[Plugins]{.dfn} are bits of software that get loaded by Ardour in order
to:

- Create various audio or MIDI effects
- Generate audio by functioning as \"software instruments\"

They are usually written by 3rd parties, though a few [come bundled with
Ardour](@@bundled-plugins) (some are only available in official builds
distributed from ardour.org). The sources for plugins are many and
varied; see [here](@@getting-more-plugins) for some information on how
to get them.

Ardour supports a variety of different plugin standards:

|  |  |
|----|----|
| [LADSPA]{.abbr title="Linux Audio Developers' Simple Plugin API"} | An early, simple, lightweight plugin [API]{.abbr title="Application
      Programming Interface"}, audio effects only, plugins have no editors/GUI of their own (Ardour provides one, however). |
| [LV2]{.abbr title="LADSPA Version 2"} | An extensible, full-featured plugin API, audio and [MIDI]{.abbr title="Musical Instrument Digital Interface"}, plugins can provide their own [GUI]{.abbr title="Graphical User Interface"}s but may use the one Ardour provides instead. |
| [AU]{.abbr title="Audio Unit"} | OS X only, full featured, audio and MIDI, plugins can provide their own GUI |
| [VST]{.abbr title="Virtual Studio Technology"} | Plugins using Steinberg\'s VST2 and VST3 plugin standard. |

## Adding/Removing/Copying Plugins

Within Ardour, plugins are just another type of [Processor]{.dfn} and so
the techniques for adding/removing/copying/moving processors apply to
plugins as well. These techniques are covered on the [Processor
Box](@@processor-box) page.
