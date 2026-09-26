# Overview of all Timecode related settings
Timecode settings are accessed from the menu in three places:

-   [Session \> Properties \> Timecode]{.kbd .menu}
-   [Edit \> Preferences \> Transport]{.kbd .menu}
-   [Edit \> Preferences \> MIDI]{.kbd .menu}

## Timecode Settings
{#tc-settings}

|                                          |                                                                                                                                                                                             |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Timecode frames-per-second]{.kbd .menu} | Configure timecode frames-per-second (23.976, 24, 24.975, 25, 29.97, 29.97 drop, 30, 30 drop, 59.94, 60). Note that all fractional framerates are actually fps\*(1000.0/1001.0).            |
| [Pull up/down]{.kbd .menu}               | Video pull-up modes change the effective samplerate of Ardour to allow for changing a film soundtrack from one frame rate to another. See [Telecine](http://en.wikipedia.org/wiki/Telecine) |
| [Slave Timecode offset]{.kbd .menu}      | The specified offset is added to the received timecode (MTC or LTC).                                                                                                                        |
| [Timecode Generator offset]{.kbd .menu}  | Specify an offset which is added to the generated timecode (so far only LTC).                                                                                                               |
| [JACK Time Master]{.kbd .option}         | Provide Bar\|Beat\|Tick and other information to JACK.                                                                                                                                      |

These settings are session specific.

## Transport Preferences
{#transports-prefs}

|                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [External timecode source]{.kbd .menu}                              | Select timecode source: JACK, LTC, MTC, MIDI Clock                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Match session video frame rate to external timecode]{.kbd .option} | This option controls the value of the video frame rate *while chasing* an external timecode source. When enabled, the session video frame rate will be changed to match that of the selected external timecode source. When disabled, the session video frame rate will not be changed to match that of the selected external timecode source. Instead the frame rate indication in the main clock will flash red and Ardour will convert between the external timecode standard and the session standard.                           |
| [External timecode is sync locked]{.kbd .option}                    | Indicates that the selected external timecode source shares sync (Black & Burst, Wordclock, etc) with the audio interface.                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Lock to 29.9700 fps instead of 30000/1001]{.kbd .option}           | The external timecode source is assumed to use 29.97 fps instead of 30000/1001. SMPTE 12M-1999 specifies 29.97df as 30000/1001. The spec further mentions that drop-frame timecode has an accumulated error of -86ms over a 24-hour period. Drop-frame timecode would compensate exactly for a NTSC color frame rate of 30 \* 0.9990 (ie 29.970000). That is not the actual rate. However, some vendors use that rate---despite it being against the specs---because the variant of using exactly 29.97 fps has zero timecode drift. |
| [LTC incoming port]{.kbd .menu}                                     | Offers a session agnostic way to retain the LTC port connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Enable LTC generator]{.kbd .option}                                | Does just what it says.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Send LTC while stopped]{.kbd .option}                              | Enable to continue to send LTC information even when the transport (playhead) is not moving. This mode is intended to drive analog tape machines which unspool the tape if no LTC timecode is received.                                                                                                                                                                                                                                                                                                                              |
| [LTC generator level]{.kbd .menu}                                   | Specify the Peak Volume of the generated LTC signal in dbFS. A good value is 0 dBu (which is -18 dbFS in an EBU calibrated system).                                                                                                                                                                                                                                                                                                                                                                                                  |

These settings are common to all sessions.

## MIDI Preferences
{#midi-prefs}

|                                    |                             |
|------------------------------------|-----------------------------|
| [Send MIDI Timecode]{.kbd .option} | Enable MTC generator        |
| [Send MIDI Clock]{.kbd .option}    | Enable MIDI Clock generator |

These settings are also common to all sessions.
