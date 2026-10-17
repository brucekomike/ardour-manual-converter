# Mono Panner
The default [mono panner]{.dfn} distributes 1 input to 2 outputs. Its
behaviour is controlled by a single parameter, the [position]{.dfn}. By
default, the panner is centered.

## Mono Panner User Interface

<figure class="left">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/mono-panner.png" alt="The mono panner" />
<figcaption aria-hidden="true">The mono panner</figcaption>
</figure>

The mono panner looks quite similar to the [stereo
panner](@@stereo-panner) interface. The difference is that the L/R
labels in the lower half of the mono panner do not move because there is
no \"width\" to control.

On the adjacent picture, the panner is centered, as shown by the central
position of the slider, called [position indicator]{.dfn}.

## Using the mouse

To change the position smoothly, press the right button and drag
anywhere within the panner. *Note: grabbing the position indicator is
not needed in order to drag.*

|                            |                                                                   |
|----------------------------|-------------------------------------------------------------------|
| Reset to defaults          | Click [right]{.kbd .mod3 .mouse}                                  |
| Change to a \"hard left\"  | Double click [right]{.kbd .mouse} in the left side of the panner  |
| Change to a \"hard right\" | Double click [right]{.kbd .mouse} in the right side of the panner |
| Set the position to center | Double Click [right]{.kbd .mouse} in the middle of the panner     |

## Keyboard bindings

When the pointer is within a mono panner user interface, the following
keybindings are available to operate on that panner:

|                             |                                    |
|-----------------------------|------------------------------------|
| [←]{.kbd} / [←]{.kbd .mod1} | move position 1° / 5° to the left  |
| [→]{.kbd} / [→]{.kbd .mod1} | move position 1° / 5° to the right |
| [0]{.kbd}                   | reset position to center           |

## Using the scroll wheel/touch scroll

When the pointer is within a mono panner user interface, the scroll
wheel may be used as follows:

|                                                  |                                  |
|--------------------------------------------------|----------------------------------|
| [⇑]{.kbd .mouse} or [⇐]{.kbd .mouse}             | move position to the left by 1°  |
| [⇑]{.kbd .mod1 .mouse} or [⇐]{.kbd .mod1 .mouse} | move position to the left by 5°  |
| [⇓]{.kbd .mouse} or [⇒]{.kbd .mouse}             | move position to the right by 1° |
| [⇓]{.kbd .mod1 .mouse} or [⇒]{.kbd .mod1 .mouse} | move position to the right by 5° |
