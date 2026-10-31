# SSL Nucleus
The Nucleus, from Solid State Logic, is a 16 fader Mackie Control device
that includes many buttons, separate meters, two LCD displays and other
features. The device is not cheap (around US\$5000 at the time of
writing), and has some [design features](#design) (or lack thereof)
which some Ardour developers find questionable. Nevertheless, it is a
very flexible device, and makes a nice 16 fader surface without the need
to somehow attach an extender to your main surface.

## Pre-configuring the Nucleus

Your Nucleus comes complete with a number of \"profiles\" for a few
well-known DAWs. At the time of writing it does not include one for
Ardour (or related products such as Harrison Mixbus).

We have prepared a profile in which as many buttons as possible send
Mackie Control messages, which makes the device maximally useful with
Ardour (and Mixbus). You can download [the
profile](https://community.ardour.org/files/ArdourNucleusProfile.zip)
and load it to your Nucleus using the `Edit Profiles` button in SSL\'s
Nucleus Remote application. Be sure to select it for the active DAW
layer in order to make Ardour work as well as possible. *Note:
unfortunately, the Nucleus Remote application only runs on OS X or
Windows, so Linux users will need access to another system to load the
profile. We will provide notes on the profile settings at a future
time.*

## Connecting the Nucleus

Unlike most Mackie Control devices, the Nucleus uses an ethernet
connection to send and receive the MIDI messages that make up the Mackie
Control protocol. Specifically, it uses a technology called \"ipMIDI\"
which essentially \"broadcasts\" MIDI messages on a local area network,
so that any connected devices (computers, control surfaces, tablets
etc.) can participate.

All other DAWs so far that support the Nucleus have chosen to do so by
using a 3rd party MIDI driver called \"ipMIDI\", which creates a number
of \"virtual\" MIDI ports on your computer. You, the user, tells the DAW
which ports to connect to, and ipMIDI takes care of the rest.

Ardour has builtin ipMIDI support, with no need of any 3rd party
packages, and no need to identify the \"ports\" to connect to in order
to communicate with the Nucleus. This makes setting it up a bit easier
than most other systems.

Unless ... you already installed the ipMIDI driver in order to use some
other DAW with your Nucleus. If ipMIDI is configured to create any
\"ports\", it is not possible for Ardour\'s own ipMIDI support to
function. We decided to offer both methods of communicating with your
Nucleus. If you regularly use other DAWs, and appreciate having ipMIDI
permanently set up to communication with the Nucleus---that\'s OK, you
can tell Ardour to use the ipMIDI driver you already have. But if
you\'re not using other DAWs with the Nucleus (and thus have not
installed the ipMIDI driver), then you can ignore the ipMIDI driver
entirely, and let Ardour connect directly with no configuration.

### Connecting via Ardour\'s own ipMIDI support

This is usable only on computers with no 3rd party ipMIDI driver
software installed and configured. If you have the OS X or Windows
ipMIDI driver from nerds.de, it **MUST** be configured to offer **ZERO**
ports before using this method.

Open `Preferences > Control Surfaces`. Ensure that the Mackie protocol
is enabled, then double-click on it to open the Mackie Control setup
dialog.

Ensure that the device selected is \"SSL Nucleus\". The dialog should
show a single numerical selector control below it, defining the ipMIDI
port number to use (it should almost always be left at the default value
of 21928).

Communication is automatically established with the Nucleus and you need
do nothing more.

If this does not work, then make sure your network cables are properly
connected, and that you are **not** running other ipMIDI software on the
computer.

### Connecting via 3rd party ipMIDI support

This is usable only on computers with 3rd party ipMIDI driver software
installed and configured for (at least) 2 ports.

Open `Preferences > Control Surfaces`. Ensure that the Mackie protocol
is enabled, then double-click on it to open the Mackie Control setup
dialog.

Ensure that the device selected is \"SSL Nucleus (via platform MIDI)\".
The dialog should show four combo/dropdown selectors, labelled
(respectively):

- `Main Surface receives via`
- `Main Surface sends via`
- `1st extender receives via`
- `1st extender sends via`

You should choose \"ipMIDI port 1\", \"ipMIDI port 1\", \"ipMIDI port
2\" and \"ipMIDI port 2\" for each of the 4 combo/dropdown selectors.

Communication should be automatically established with the Nucleus.

If this does not work, then make sure your network cables are properly
connected, and that you are running the appropriate ipMIDI driver and
have configured it for 2 (or more) ports.

## [Nucleus Design Discussion]{#design}

You might be reading this part of the manual seeking some guidance on
whether the Nucleus would make a suitable control surface for your
workflows. We don\'t want to try to answer that question definitively,
since the real answer depends on the very specific details of your
workflow and situation, but we would like to point out a number of
design features of the Nucleus that might change your opinion.

### Cons

|  |  |
|----|----|
| No Master Faster | It is not possible to control the level of the Master bus or Monitor section. Really don\'t know what SSL was thinking here. |
| No dedicated rec-enable buttons | You have to press the \"Rec\" button and convert the per-strip \"Select\" buttons into rec-enables |
| No dedicated automation buttons | You have to press the \"Auto\" button and convert the first 4 vpots into 4 automation-related buttons, losing your current view of the session. |
| No buttons with Mackie-defined \"Marker\" functionality | Mackie\'s design intentions for the interoperation of the Marker, rewind and ffwd buttons requires profile editing in order to function properly. |
| No \"Dyn\" button | This is hard to assign in an edited profile. To be fair, other Mackie Control devices also lack this button. |

### Pros

|  |  |
|----|----|
| Single cable connectivity | No need for multiple MIDI cables to get 16 faders |
| Broadcast connectivity | Connecting to multiple computers does not require recabling |
| 16 faders from a single box | No need to figure out how to keep extenders together |
| Meters separated from displays | Contrast with the Mackie Control Universal Pro, where meters interfere with the display |
| DAW profiles | Easy to flip profiles for use by different DAWs. |

### Ambiguous

|  |  |
|----|----|
| Ability to make buttons generate USB keyboard events | The extent to which this is useful reflects the target DAWs inability to manage all of its functionality via Mackie Control |
| Sophisticated \"profile\" editing | It is nice to be able to reassign the functionality of most buttons, but this is only necessary because of the relatively few global buttons on the surface. |
| Builtin analog signal path | SSL clearly expects users to route audio back from their computer via the Nucleus\' own 2 channel output path, and maybe even use the input path as well. They take up a significant amount of surface space with the controls for this signal path, space that could have been used for a master fader or more Mackie Control buttons. The USB audio device requires a proprietary driver, so Linux users can\'t use this, and OS X/Windows users will have to install a device driver (very odd for a USB audio device these days). The analog path also no doubt adds notable cost to the Nucleus. There\'s nothing wrong with this feature for users that don\'t already have a working analog/digital signal path for their computers. But who is going to spend \$5000 on a Nucleus that doesn\'t have this already? |
