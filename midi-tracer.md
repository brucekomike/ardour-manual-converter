# MIDI Tracer
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/midi-tracer.png" width="340"
alt="The MIDI Tracer window" />
<figcaption aria-hidden="true">The MIDI Tracer window</figcaption>
</figure>

The [MIDI Tracer]{.dfn} window, which is accessed by selecting [Window
\> MIDI Tracer]{.kbd .menu} from the main menu, is similar to the [MIDI
List Editor](@@midi-list-editor) in that it displays MIDI information as
tabular text, and has a vertical flow (i.e. the events follow a top to
bottom time-oriented order).

Its use is different however, as it is *not* bound to a specific region
or track; the MIDI shown in the MIDI Tracer window is any global input
or output Ardour presents to the system. As such, it is a very useful
way to monitor MIDI traffic, whether it is an external controller or
device or the input or output of any track.

The MIDI Tracer can list all types of MIDI and \"audio\" events, and
[scene automation](@@midi-scene-automation) and
[timecode](@@timecode-generators-and-slaves) events as well.

The window consists of:

|                      |                                                                                                                                                            |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Port]{.dfn}         | A list of all the MIDI ports Ardour presents to the system. They are both internal and external and are the same ports Ardour presents to JACK, if enabled |
| The events list      | Where all the events for this port are listed, see below                                                                                                   |
| [Line history]{.dfn} | How many lines should be kept in the events list; once this limit is reached, older events will be removed from the list                                   |
| [Delta times]{.dfn}  | If checked, shows the times as the duration since the last event, instead of [absolute times](@@on-clock-and-time)                                         |
| [Decimal]{.dfn}      | If checked, shows the MIDI data as decimal values instead of hexadecimal                                                                                   |
| [Enabled]{.dfn}      | If checked, events are displayed in the events list as they occur, otherwise stops the logging                                                             |
| [Auto-Scroll]{.dfn}  | If checked, the events list scrolls as new events are logged, keeping the newest events on screen                                                          |
| [Scroll]{.dfn}       | When clicked, this deletes all previous recorded events from the list.                                                                                     |

The events list displays the events as columns:

|                                    |                                                                                                      |
|------------------------------------|------------------------------------------------------------------------------------------------------|
| Time of the event                  | Either absolute or relative, based on the [Delta times]{.kbd .option} checkbox                       |
| MIDI status (event type)           | What MIDI events happened (e.g. Note On, Note Off, Pitch Bend, etc.)                                 |
| MIDI channel                       | The MIDI channel the event happened in                                                               |
| MIDI data bytes (event parameters) | Parameters of the event, e.g. for a Note On: what the [note](@@midi-notes-ref) was, and its velocity |
