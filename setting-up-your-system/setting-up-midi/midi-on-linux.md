# MIDI on Linux
It is no longer necessary to use jackd as a backend for Ardour in Linux.
In fact with the spread of LV2 plugins, almost all workflows in Ardour
work well with the ALSA backend. When using the ALSA backend for Ardour,
Ardour will see all MIDI ports that ALSA sees without any user setup.
However, should jackd need to be used, the rest of this page is valid.

The right approach for using MIDI on Linux depends on which version of
JACK is in use. The world divides into:

|                                               |                                                                                                                                                                                                                           |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Systems using JACK 1, versions 0.124 or later | On these systems, JACK must be started with the `-X alsa_midi` server argument. To support legacy control applications, the `-X seq` argument to the ALSA backend of JACK can also be used to get the exact same results. |
| All others                                    | Using a2jmidid acts as a bridge between ALSA MIDI and JACK. The `-X seq` or `-X raw` arguments should *not* be used---the timing and performance of these options is unacceptable.                                        |

## Using a2jmidid
{#a2jmidid}

[a2jmidid]{.dfn} is an application that bridges between the system MIDI
ports and JACK.

First it must be ensured that there is no ALSA sequencer support enabled
in JACK. To check that, one must open QJackCtl\'s [Setup]{.kbd .menu}
window and set [Settings \> MIDI Driver]{.kbd .menu} to [none]{.kbd
.input}, then uncheck the [Misc \> Enable ALSA Sequencer support]{.kbd
.optoff} option. The jack server must then be restarted before going on.

### Checking for a2jmidid availability
{#checking-a2jmidid-availability}

Next, it must be checked whether a2jmidid is already installed. This is
done by starting the JACK server, then going to the command line and
typing:

[a2jmidid -e]{.kbd .cmd .lin}

If a2jmidid does not exist, it must be installed with the software
manager of the Linux distribution in use until this command responds.

## Checking available MIDI ports
{#checking-available-ports}

If JACK is correctly configured for MIDI, then the MIDI ports should
appear in qjackctl under [Connections \> MIDI]{.kbd .menu}.

### Making it automatic
{#automatic}

Once it has been verified that the ports appear in JACK as expected,
this can be made to happen whenever JACK is started:

-   If a newer version of JACK 1 is in use, by just making sure the
    `-X alsa_midi` or `-X seq` options are enabled for whatever
    technique is being used to start JACK.
-   For other versions of JACK, by adding `a2jmidid -e &` as an \"after
    start-up\" script in the [Setup \> Options]{.kbd .menu} tab of
    QJackCtl, so that it is started automatically whenever JACK is
    started.
