# Generic MIDI Learn
## Philosophy

There are no \"best\" ways to map an arbitrary MIDI controller for
controlling Ardour. There may be very legitimate reasons for different
users to prefer quite different mappings.

## Basics

1.  Enable Generic MIDI control: [Edit \> Preferences \> Control
    Surfaces \> Generic MIDI]{.kbd .menu}
2.  Connect Ardour\'s MIDI port named `control`{.sample} to whatever
    hardware or software you want (using a MIDI patchbay app)
3.  [Middle]{.kbd .mod1 .mouse}-click on whatever on-screen fader,
    plugin parameter control, button etc. you want to control
4.  A small window appears that says \"Operate Controller now\"
5.  Move the hardware knob or fader, or press the note/key.
6.  The binding is complete. Moving the hardware should control the
    Ardour fader etc.

There\'s a complication to this story, however. You cannot use MIDI
learn with the GUI provided by the plugin. This is true no matter what
the plugin format or platform is. When we refer to \"whatever on-screen
fader \...\" above, we are referring to an "Ardour-owned" control of
some sort. You can get access to that in one of 3 ways:

- right click on the processor element in the mixer strip, and choose
  "Edit with Generic GUI"
- right click on the processor element in the mixer strip, and from
  "Controls", make the desired parameter visible inline in the mixer
  strip
- in the editor, click on the "A" (automation) button for the track,
  find the desired parameter. This will make the automation lane for
  that parameter visible, and it comes with a fader you can use for MIDI
  learn.

You can't just "click the GUI" because the plugin owns the GUI, and
cannot (and should not) be a part of the MIDI learn process.

## Cancelling a Learned MIDI Binding

To unlearn a learned MIDI binding, [Middle]{.kbd .mod1 .mouse}-click on
the control in the same way as you did to learn it in the first place,
but click on the popup to cancel it.

## Avoiding work in the future

If you want the bindings you set up to be used automatically in every
session, the simplest thing to do is to use [Session \> Save
Template]{.kbd .menu}. Then, when creating new sessions, select that
template and all the bindings will be automatically set up for you.
