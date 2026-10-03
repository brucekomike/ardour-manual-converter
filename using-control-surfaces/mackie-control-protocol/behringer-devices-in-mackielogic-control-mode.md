# Behringer Devices in Mackie/Logic Control Mode
-   [Behringer BCF-2000](#bcf2000)
-   [Behringer X-Touch](#xtouch)
-   [Behringer X-Touch Compact](#compact)
-   [Behringer X-Touch Mini](#mini)

## Behringer BCF-2000 Faders Controller
{#bcf2000}

<figure>
<a href="/images/BCF2000.png"><img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/BCF2000.png"
style="max-width:500px;" alt="Digramatic Image of the BCF2000" /></a>
<figcaption>Diagrammatic Image of the BCF2000 (click for a full-size
view)</figcaption>
</figure>

The Behringer BCF-2000 Fader Controller is a control surface with 8
motorized faders, 8 rotary encoders and 30 push buttons. The device is a
class compliant USB Midi Interface and also has standard Midi DIN
IN/OUT/THRU ports. The device has included a Mackie/Logic Control
Emulation Mode since firmware v1.06. Any devices with a firmware older
than v1.06 will require an update before Mackie Control Emulation works
as described here.

<figure>
<a href="/images/BCF2000-EG.png"><img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/BCF2000-EG.png"
style="max-width:500px;"
alt="Digramatic Image of the BCF2000 in Edit Global Mode" /></a>
<figcaption>Diagrammatic Image of the BCF2000 in Edit Global Mode (click
for a full-size view)</figcaption>
</figure>

In order to put the controller into Mackie/Logic control mode, the unit
must be turned on while holding the third button from the left in the
top most row of buttons (under the rotary encoder row). The button must
be held down until [EG]{.kbd .input} or edit global mode is displayed on
the LCD screen of the unit. The global parameters can then be edited
using the 8 rotary encoders in the top row.

-   Encoder #1 sets the operating mode and should be set to [U-1]{.kbd
    .input} or USB mode 1 if using with a USB cable connection.
-   Encoder #3 sets the foot switch mode and should most likely be set
    to [Auto]{.kbd .input} to detect how the foot switch is wired.
-   Encoder #5 sets the device id, if you are using only 1 device the id
    should be set to [ID 1]{.kbd .input}. If you are using multiple
    BCF/BCR2000 each device is required to be set up sequentially and
    one at a time.
-   Encoder #7 controls the MIDI [Dead Time]{.dfn} or the amount of
    milliseconds after a move has been made that the device ignores
    further changes, this should be set to [100]{.kbd .input}.
-   Encoder #8 controls the MIDI message [Send Interval]{.dfn} in
    milliseconds and should be set to [10]{.kbd .input}

To exit the [EG]{.kbd .input} mode press the [Exit]{.kbd .button}
button. The device is now ready to use with Ardour.

### Modes of Operation

<figure>
<a href="/images/BCF2000-Modes.png"><img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/BCF2000-Modes.png"
style="max-width:500px;"
alt="Digramatic Image of the BCF2000 Control Modes" /></a>
<figcaption>Diagrammatic Image of the BCF2000 Control Modes (click for a
full-size view)</figcaption>
</figure>

The four buttons arranged in a rectangle and located under the Behringer
logo are the mode selection buttons in Logic Control Emulation Mode,
currently Ardour has implemented support for two of these modes.

The surface can be broken into 8 groups of controls:

1.  The rotary encoders at the top of the device
2.  The first row of buttons under the encoders
3.  The second row of buttons under the encoders
4.  The row of motorized faders
5.  
6.  The group of 4 buttons at the top right that will be referred to
    here as the [Shift Group]{.dfn}
7.  The group of 4 buttons under the [Shift Group]{.dfn} referred to
    here as the [Mode Group]{.dfn}
8.  The group of 2 buttons under the [Mode Group]{.dfn} referred to here
    as the [Select Group]{.dfn}
9.  The group of 4 buttons under the [Select Group]{.dfn} referred to
    here as the [Transport Group]{.dfn}

### Mixer Pan Mode

<figure>
<a href="/images/BCF2000-Pan.png"><img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/BCF2000-Pan.png"
style="max-width:500px;"
alt="Digramatic Image of the BCF2000 Control Modes" /></a>
<figcaption>Diagrammatic Image of the BCF2000 Control Modes (click for a
full-size view)</figcaption>
</figure>

This is the standard work mode that organizes the control surface to
emulate a standard mixer layout where controls for each track/bus are
arranged vertically. The order of the faders is either controlled by the
order of the tracks in the mixer or can be set manually by the user.

```{eval-rst}
+-----------------------------------+-----------------------------------+
| Encoders                          | Mixer Pans. The red LEDs show the |
|                                   | amount of pan left or right       |
+-----------------------------------+-----------------------------------+
| First Row of Buttons              | Mixer Mutes. The button led       |
|                                   | lights up if the track is         |
|                                   | currently muted                   |
+-----------------------------------+-----------------------------------+
| Second Row of Buttons             | Select Active Track/Bus.          |
|                                   | Currently selected track/bus is   |
|                                   | indicated by the button led       |
+-----------------------------------+-----------------------------------+
| Faders                            | Mixer Gains                       |
+-----------------------------------+-----------------------------------+
| Shift Group                       | -   The top and bottom left       |
|                                   |     buttons are simply shifts to  |
|                                   |     change the function of other  |
|                                   |     buttons.                      |
|                                   | -   The top right is the [Fine    |
|                                   |     Control]{.dfn} button that    |
|                                   |     allows the increment values   |
|                                   |     sent by by rotary encoders    |
|                                   |     and faders to be a small      |
|                                   |     value for more precise        |
|                                   |     editing. This button can also |
|                                   |     act as a shift button.        |
|                                   | -   The bottom right is the       |
|                                   |     [Global Shift]{.dfn} button   |
|                                   |     that allows you to change     |
|                                   |     back to the standard Mixer    |
|                                   |     Pan view from other views and |
|                                   |     modes. This button can also   |
|                                   |     act as a shift button.        |
+-----------------------------------+-----------------------------------+
| Mode Group                        | -   The top two buttons functions |
|                                   |     are not currently implemented |
|                                   |     in Ardour.                    |
|                                   | -   The bottom left button sets   |
|                                   |     the device to [Pan]{.dfn}     |
|                                   |     mode and should currently be  |
|                                   |     lit                           |
|                                   | -   The bottom right button sets  |
|                                   |     the device to [Send]{.dfn}    |
|                                   |     mode but will only allow the  |
|                                   |     switch if the currently       |
|                                   |     selected track/bus has a send |
|                                   |     or sends to control.          |
+-----------------------------------+-----------------------------------+
| Select Group                      | In this mode they function as     |
|                                   | bank select left and right. If    |
|                                   | the current session has more than |
|                                   | 8 tracks the next set of 8 tracks |
|                                   | is selected with the right button |
|                                   | and the faders will move to match |
|                                   | the current gain settings of that |
|                                   | bank of 8 tracks/busses. If the   |
|                                   | last bank contains less than 8    |
|                                   | tracks/busses the unused faders   |
|                                   | will move to the bottom and the   |
|                                   | pan lights will all turn off. An  |
|                                   | unlimited amount of tracks can be |
|                                   | controlled with the device.       |
+-----------------------------------+-----------------------------------+
| Transport Group                   | -   The upper left button         |
|                                   |     controls [Rewind]{.dfn}.      |
|                                   | -   The upper right button        |
|                                   |     controls [Fast Forward]{.dfn} |
|                                   | -   The lower left button         |
|                                   |     controls [Stop]{.dfn}         |
|                                   | -   The lower right button        |
|                                   |     controls [Play]{.dfn}         |
+-----------------------------------+-----------------------------------+
```

### Send Mode

<figure>
<a href="/images/BCF2000-Send.png"><img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/BCF2000-Send.png"
style="max-width:500px;" alt="Digramatic Image of the Send Mode" /></a>
<figcaption>Diagrammatic Image of the Send Mode (click for a full-size
view)</figcaption>
</figure>

Send mode allows for the top row of encoders to control the sends for a
selected channel. One interesting option is to flip the controls from
the encoders to the faders by pressing the [shift 1]{.kbd .button}
button and the [global view]{.kbd .button} button at the same time.

|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Encoders              | In send mode, the encoders control sends from left to right instead of mixer pans. If there are less than 8 sends the behavior of the encoder will be to continue controlling the mixer pan. Visually it is indicated by the change in the LED from originating at the 12 o\'clock position to originating at the 7 o\'clock position. If [FLIP]{.kbd .button} is pressed the encoder will control the mixer gain for the selected track/bus. |
| First row of buttons  | No Change                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Second row of buttons | No Change.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Faders                | No change unless [FLIP]{.kbd .button}is pressed then it controls the send for the selected track/bus.                                                                                                                                                                                                                                                                                                                                         |
| Shift Group           | No Change                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Select Group          | No Change                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Transport Group       | No Change                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Mixer Pan While Holding [Shift 1]{.kbd .button}

<figure>
<a href="/images/BCF2000-Shift1.png"><img
src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/BCF2000-Shift1.png" style="max-width:500px;"
alt="Digramatic Image of the Mixer Mode while holding down shift 1" /></a>
<figcaption>Diagrammatic Image of the Mixer Mode while holding down <kbd
class="button">Shift 1</kbd></figcaption>
</figure>

The operations of various buttons change while holding down the [Shift
1]{.kbd .button} button:

```{eval-rst}
+-----------------------------------+-----------------------------------+
| Encoders                          | No Change                         |
+-----------------------------------+-----------------------------------+
| First row of buttons              | These now control the Soloing of  |
|                                   | each track/bus in the current     |
|                                   | bank                              |
+-----------------------------------+-----------------------------------+
| Second row of buttons             | These now control the Enable      |
|                                   | Record for each track             |
+-----------------------------------+-----------------------------------+
| Faders                            | No Change                         |
+-----------------------------------+-----------------------------------+
| Shift Group                       | No change                         |
+-----------------------------------+-----------------------------------+
| Mode Group                        | No Change                         |
+-----------------------------------+-----------------------------------+
| Select Group                      | These now change the current bank |
|                                   | of tracks being controlled over   |
|                                   | by one. So if tracks 1-8 where    |
|                                   | controlled, pushing the           |
|                                   | [right]{.kbd .button} button will |
|                                   | change the controlled tracks to   |
|                                   | 2-9, and pressing the [left]{.kbd |
|                                   | .button} would then shift back to |
|                                   | controlling tracks 1-8.           |
+-----------------------------------+-----------------------------------+
| Transport Group                   | -   The upper left now controls   |
|                                   |     turning on and off            |
|                                   |     [Loop]{.dfn} mode.            |
|                                   | -   The upper right now toggles   |
|                                   |     [Click]{.dfn}.                |
|                                   | -   The lower left toggles        |
|                                   |     [Replace]{.dfn}.              |
|                                   | -   The lower right toggles       |
|                                   |     [Global Record]{.dfn}.        |
+-----------------------------------+-----------------------------------+
```

### Mixer Pan While Holding [Shift 2]{.kbd .button}

<figure>
<a href="/images/BCF2000-Shift2.png"><img
src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/BCF2000-Shift2.png" style="max-width:500px;"
alt="Digramatic Image of the Mixer Mode while holding down shift 2" /></a>
<figcaption>Diagrammatic Image of the Mixer Mode while holding down <kbd
class="button">Shift 2</kbd></figcaption>
</figure>

The operations of various buttons change while holding down the [Shift
2]{.kbd .button} button:

|                       |                                                                               |
|-----------------------|-------------------------------------------------------------------------------|
| Encoders              | No Change                                                                     |
| First row of buttons  | FIX ME                                                                        |
| Second row of buttons | These now control setting up different [Views]{.dfn}. See below for more info |
| Faders                | No Change                                                                     |
| Shift Group           | No change                                                                     |
| Mode Group            | No Change                                                                     |
| Select Group          | Left button controls [Undo]{.dfn}(FIXME: NEEDS VERIFICATION)                  |
| Transport Group       | FIX ME                                                                        |

### Views

<figure>
<a href="/images/BCF2000-Views.png"><img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/BCF2000-Views.png"
style="max-width:500px;"
alt="Digramatic Image of the LED display for different Views" /></a>
<figcaption>Diagrammatic Image of the LED display for different
Views</figcaption>
</figure>

## Behringer X-Touch
{#xtouch}

The Behringer X-Touch is a direct emulation of the Mackie Control and
has all the buttons the Mackie device does. There is a \"Behringer
X-Touch\" map included with Ardour. The X-Touch can be connected to the
computer with USB or through a MIDI port. Using USB keeps MIDI ports
free for other uses. The Ethernet port uses RTP MIDI which should show
up as MIDI devices on MacOS computers.

## Behringer X-Touch Compact
{#compact}

The Behringer X-Touch Compact has a Mackie Control mode. From the device
manual:

\"To switch between standard operating mode and MC (Mackie Control)
mode, press and hold down the MC button in the bottom left corner, and
then turn on the unit's power switch. Keep holding down the MC button
until the MC MODE LED lights continuously to show that the unit is in MC
mode.\"

There is a \"Behringer X-Touch Compact\" map included with Ardour. The
X-Touch can be connected to the computer with USB or through a MIDI
port. Using USB keeps MIDI ports free for other uses.

The Behringer X-Touch Compact has fewer controls than the Mackie control
and therefore less function as well. See pages 19-21 of the Behringer
X-Touch Compact Quick Start Guide For an explanation of what controls on
the Compact map to which Mackie Control buttons.

## Behringer X-Touch Mini
{#mini}

The Behringer X-Touch Mini says it can emulate Mackie control as well.
There is a \"Behringer X-Touch Mini\" map included with Ardour. The
control layout in Mackie Control mode is shown below.

![X-Touch Mini MC mode
layout](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/xtouch-mini-mcp.png){.invert-in-dark}

Missing content
