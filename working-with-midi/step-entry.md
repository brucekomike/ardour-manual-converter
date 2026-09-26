# Step Entry
Entering notes in Ardour can be done by using a connected MIDI device
like a MIDI keyboard or pad controller, or by using the mouse. A third
option, which provides for fine-grained control, precision and speed
comes from using Ardour\'s Step Entry dialog.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/step_entry.png" class="fit"
alt="Ardour&#39;s Step Entry dialog" />
<figcaption>Ardour's Step Entry dialog.</figcaption>
</figure>

The step entry dialog is accessed by [right]{.kbd .mouse}-clicking on
the [●]{.kbd .menu style="color:red;"} (Rec-Enable) button of the [MIDI
track](@@midi-track-controls) to be edited and selecting [Step
Entry]{.kbd .menu} from the menu that appears.

Step editing and recording MIDI via the track\'s MIDI port cannot happen
simultaneously.

The dialog (closely modelled on Logic\'s) contains:

-   Chord entry switch (successive notes are stacked in a chord until it
    is released)
-   Note length selectors
-   Triplet toggle
-   Normal, single, double and triple dotted note selectors
-   Sustain button
-   Buttons to:
    -   Insert a rest of the current selected note duration
    -   Insert a rest of the current grid step size
    -   Move back to the last inserted note
    -   Move forward to the next beat, or bar
    -   Move to the edit point
-   Dynamics controls from pianississimo to fortississimo
-   Channel selector
-   Explicit numerical velocity selector, for more precise control than
    the dynamics selectors offer
-   Octave selector
-   A full 10-octave virtual keyboard

Almost all actions in the step entry dialog can be driven directly from
the keyboard, so that moving back and forth from the keyboard to the
mouse is typically not necessary---even for complex data entry. The
default key bindings are:

|                           |                                           |
|---------------------------|-------------------------------------------|
| [\`]{.kbd} (grave accent) | Set octave 0                              |
| [1]{.kbd} to [9]{.kbd}    | Set octave 1 to 9                         |
| [0]{.kbd}                 | Set octave 10                             |
| [f1]{.kbd}                | Set note length to whole                  |
| [f2]{.kbd}                | Set note length to half                   |
| [f3]{.kbd}                | Set note length to third                  |
| [f4]{.kbd} to [f8]{.kbd}  | Set note length to quarter to sixtyfourth |
| [a]{.kbd}                 | Insert C                                  |
| [w]{.kbd}                 | Insert C♯                                 |
| [s]{.kbd}                 | Insert D                                  |
| [e]{.kbd}                 | Insert D♯                                 |
| [d]{.kbd}                 | Insert E                                  |
| [f]{.kbd}                 | Insert F                                  |
| [t]{.kbd}                 | Insert F♯                                 |
| [g]{.kbd}                 | Insert G                                  |
| [y]{.kbd}                 | Insert G♯                                 |
| [h]{.kbd}                 | Insert A                                  |
| [u]{.kbd}                 | Insert A♯                                 |
| [j]{.kbd}                 | Insert B                                  |
| [tab]{.kbd}               | Insert a one note length rest             |
| [tab]{.kbd .mod1}         | Insert a one grid unit rest               |
| [backspace]{.kbd}         | Moves the cursor back one note length     |
| [z]{.kbd}                 | Set note velocity 𝆏𝆏𝆏                     |
| [x]{.kbd}                 | Set note velocity 𝆏𝆏                      |
| [c]{.kbd}                 | Set note velocity 𝆏                       |
| [v]{.kbd}                 | Set note velocity 𝆐𝆏                      |
| [b]{.kbd}                 | Set note velocity 𝆐𝆑                      |
| [n]{.kbd}                 | Set note velocity 𝆑                       |
| [m]{.kbd}                 | Set note velocity 𝆑𝆑                      |
| [,]{.kbd} (comma)         | Set note velocity 𝆑𝆑𝆑                     |
| [↑]{.kbd}                 | Set next note velocity                    |
| [↓]{.kbd}                 | Set prev note velocity                    |
| [↑]{.kbd .mod1}           | Set next note length                      |
| [↓]{.kbd .mod1}           | Set prev note length                      |
| [\']{.kbd}                | Toggle triplet                            |
| [.]{.kbd}                 | Set single dotted                         |
| [.]{.kbd .mod1}           | Clear dotted                              |
| [\|]{.kbd} (bar)          | Toggle chord                              |
