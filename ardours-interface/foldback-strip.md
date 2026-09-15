# Foldback Section
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/foldback-gui.png" alt="The Foldback strip" />
<figcaption aria-hidden="true">The Foldback strip</figcaption>
</figure>

The [Foldback section]{.dfn} is an optional feature that provides stage
monitoring mixes. Many times the main mix is used for this purpose in a
setup with only the control room. However, for a separate studio and
multiple monitor mixes for in-ear use, a separate set of Foldback buses
provides that flexibility.

These foldback buses may be mono for a stage monitor wedge or stereo to
allow in-ear or headphones to have different mixes for each ear, such as
one\'s self in one ear and the rest of the music in the other.

A Foldback bus can be created in the same manner as any other bus is
created, from the [Track \> Add Track, Bus or VCA]{.kbd .menu} Window.
Once at least one Foldback bus has been created, the Foldback strip will
appear in the mixer window.

Foldback sends can be created from the processor box context menu by
selecting [New Foldback Send]{.kbd .menu} and then the Foldback bus
desired.

![create send](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/foldbacksend.png)

A second method is to select all the source channels and then use the
Foldback bus sendbox context menu and select either [Assign Selected
Tracks]{.kbd .menu} or [Assign Selected Tracks and Buses]{.kbd .menu}.

The [View \> Mixer: Show Foldback Strip]{.kbd .menu} checkbox will
determine if the Foldback strip is visible. The Foldback strip appears
just to the left of the Master strip in the Mixer window. It comprises:

1.  Previous and Next buttons
2.  Hide button
3.  Foldback bus name button
4.  Invert button
5.  Show sends button
6.  Send controls
7.  Bus pan control
8.  Processor box
9.  Listen button
10. Foldback bus level control
11. Foldback bus output routing
12. Comments button

## Previous and Next

The Previous button shows the previous Foldback bus in the Foldback
strip. The Next button shows the next Foldback strip. The button will be
disabled if there are no more Foldback buses in that direction.

## Hide

The hide button hides the Foldback strip when not being adjusted. The
Foldback strip can be shown again from the main menu [View \> Mixer:
Show Foldback Strip]{.kbd .menu} item.

## Name button

The name button shows the name of the current Foldback bus. It has two
menus: the Foldback bus selection menu, activated with a mouse button 1
click, and the context menu, activated with a mouse button 3 click. The
context menu has these items in it:

-   [Comments]{.kbd .menu} is the same as the Comments button at the
    bottom of the strip
-   [Outputs]{.kbd .menu} shows the output routing grid
-   [Save as a template]{.kbd .menu} opens the template save dialog. The
    template saved has the same number of channels and the same
    processors but does not have any sends selected.
-   [Rename]{.kbd .menu} shows a rename dialog that allows the Foldback
    bus name to be renamed
-   [Active]{.kbd .menu} toggles The active status of the current
    Foldback bus
-   [Protect Against Denormals]{.kbd .menu} turns on denormal protection
    for the current Foldback bus
-   [Remove]{.kbd .menu} will remove the current Foldback bus

## Invert Buttons

The invert buttons (one for each channel) invert the audio signal. This
may be useful in some situations for controlling feedback. However,
proper microphone and monitor placement or the use of head phones or in
ear monitoring will be more effective.

## Show Sends

Show sends allows the send levels and pan to be controlled from the
originating track by using the main fader for the track. The fader and
pan controls will change color to indicate this mode and the show sends
button will flash to indicate this mode. Changing the current Foldback
bus will disable this mode.

## The Send Box

The send box shows controls for each send. There is a context menu
available by clicking mouse button 3 anywhere in the send box.

-   [Assign Selected Tracks]{.kbd .menu} creates Foldback sends on each
    selected track that feed the current Foldback bus
-   [Assign Selected Tracks and Buses]{.kbd .menu} creates Foldback
    sends on each selected track and bus that feed the current Foldback
    bus
-   [Copy track/bus gains to sends]{.kbd .menu} Sets the gain on the
    send to be the same as the gain of the track or bus the send comes
    from for the current Foldback bus
-   [Set sends gain to -inf]{.kbd .menu} sets the gain on all sends for
    the current Foldback bus to −∞ (the lowest gain possible)
-   [Set sends gain to 0dB]{.kbd .menu} sets the gain on all sends for
    the current Foldback bus to 0dB

### The Send Control Block

![The Foldback send](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/foldback-send.png)

There is a send control block for every send to the current Foldback
bus. The Send control block features three controls:

-   The button which shows the Foldback bus\' name, has an active
    \"LED\" indicator that can be clicked to enable or disable that send
    and has a menu (mouse button 1) with items for that send:
    -   [Copy track/bus gain to send]{.kbd .menu} Sets the gain on the
        send to be the same as the gain of the track or bus the send
        comes from for the current Foldback bus
    -   [Set send gain to -inf]{.kbd .menu} sets the send gain for the
        current Foldback bus to −∞ (the lowest gain possible)
    -   [Set send gain to 0dB]{.kbd .menu} sets the send gain for the
        current Foldback bus to 0dB
    -   [Remove This Send]{.kbd .menu} removes the send from the sending
        track or bus.
-   The knob, only present on a stereo Foldback bus, which controls the
    pan azimuth
-   The horizontal slider which control the level input from that
    channel

## The Pan Control

This is just like every other track or bus strip and works the same way.

## The Processor Box

This processor box is the same as on the other tracks and buses and
allows for adding things like reverb to the Foldback mix without writing
it to the track. It would also be possible to add in sound from a reverb
bus instead.

## The Listen Button

This is only available in PFL or AFL mode as it uses the same code as
the solo on other tracks and buses. It allows the control room monitor
or headphones to hear what the performer will hear in their monitor.

## The Foldback Level Knob

This controls the output level being sent to the stage monitor.

## The Output Port Selector

This is similar to the output selectors on the tracks and buses. It
differs in only a few ways. First it is never automatically connected. A
Foldback bus is always meant to be directly connected to an output
device and never to master or the monitor bus. The choices shown
therefore reflect this.

## The Comment Button

Just like the track and bus comment button, this allows opening a window
to type in notes about the current Foldback bus for future reference.
