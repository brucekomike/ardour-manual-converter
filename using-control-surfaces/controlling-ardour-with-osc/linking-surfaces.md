# Linking Surfaces
As of Ardour 6.0, Ardour provides the possibility of linking two or more
surface to work as one surface. This means that two surfaces, one with 8
strips and one with 6 strips would look like a single 14 strip surface.
A `/bank_up` or down on either surface with bank the two so that they
bank in 14 strip increments.

Ardour 5.0 to 5.12 can use two surfaces as shown in [Example
3](#example3).

## Surface Linking Concepts

-   A group of surfaces linked together are called a `Link Set`. A
    `Link Set` is called by a positive integer number.
-   There may be more than one `Link Set` at a time used with Ardour.
-   Each surface inside a `Link Set` has a `Link Id`.
-   The `Link ID` is a positive integer numbering consecutive surfaces
    starting from 1 for the left most and going up to the right. So if
    there are three surfaces in a `Link Set`, The left surface will have
    a `Link Id` of *1*, the middle surface will have a `Link Id` of *2*
    and the right surface will have a `Link Id` of *3*.
-   There may not be skipped `Link Ids`. If there are a surface 1 and 3,
    there must also be a surface 2. Surface 1 must always exist. If any
    surface is missing, the track names will indicate the `Link Id` of
    the first device missing.
-   In most things, surfaces are separate and can do things
    independently.
    -   Each surface can have a different `Gain Mode`
    -   Each surface has it\'s own `Bank Size`
    -   Each surface has it\'s own `Feedback`
    -   Each surface has it\'s own *Expanded Strip*

    However, some things are shared by all surfaces in a `Link Set`:
    -   Banking is done as a unit and each surface bank start is
        determined by the `Link Set`. Any surface can *Bank Up* or *Bank
        Down*.
    -   All surfaces share the same *strip types*. Setting *Strip Types*
        in any one surface sets it for the whole `Link Set`.

## Setting Up a Link Set

There are only two OSC commands needed to set up a `Link Set`:

|                                                   |                                                                                                                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [/link/set *linkset* *linkid*]{.kbd .osc}         | Where *linkset* is the Link Set this surface will be added to and *linkid* is the Link Id of this surface.                                                                                           |
| [/link/bank_size *linkset* *banksize*]{.kbd .osc} | Where *linkset* is the Link Set this surface will be added to and *banksize* is the target bank size for this Link Set. This Link Set will not operate unless the total strip numbers is *banksize*. |

It is also possible to send link set and ID values as part of a
`/set_surface` command. [/set_surface *bank_size* *strip_types*
*feedback* *fadermode* *send_page_size* *plugin_page_size* *port*
*linkset* *linkid*]{.kbd .osc}

The `/link/bank_size` command is optional. Ardour defaults to linking
with auto sizing banks where the `Link Set` bank size is determined by
adding the available surface bank sizes together. So long as the
`Link Ids` are consecutive, the `Link Set` is considered ready. If the
surface wants to make sure all surfaces are present before the
`Link Set` is ready, the `/link/bank_size` command will not allow the
`Link Set` to be ready until the surface bank sizes add up to the
`Link Set's` bank size.

Setting up a linked set of surfaces is a simple as choosing a number for
the `Link Set`, *1* will work fine if there is only one linked set of
surfaces, and giving each surface a ` Link Id`. This can be done with
the same method as the ` /set_surface` command is sent or by having each
surface send the `/link/set` command. As with other commands, the first
parameter (linkset) may be sent inline: `/link/set/1 `*`linkid`* for
those surfaces unable to send multi parameter OSC messages.

## Example Multi Device Surfaces

### Example 1

Assuming two devices, the left device has 8 strips and very little else
on it\'s main page or tab. It may have secondary pages or tabs or a
physical control section to access the extra selected strip controls
like send levels or plugin controls. The right device has only 6 strips
because it also has Master and Monitor channel as well as transport
controls. It also has a select section. As part of it\'s Global controls
it has a Bank up and a bank down button. (there is nothing stopping the
left surface from also having banking buttons) The left surface will be
linkid *1* and the right surface will be linkid *2*. For this example
the linkset will be *1*.

Device *1* will have a \"Connect\" button that will send:
`/set_surface iiiiiiiii 8 159 8323 0 0 0 0 1 1` and the second device
will have two buttons. One will be a \"Connect\" button that sends:
`/set_surface iiii 6 159 8403 0` and the other will be a \"Link\" button
that will send: `/link/set ii 1 2`. These devices use two different
methods of setup both to illustrate their use and because this will
allow them to be used unlinked. Device *1* even as a linked device will
operate on it\'s own as a one device `Link Set`. However, device *2*
would show an error condition if device *1* is not present so we have a
separate \"Link\" button. This is an optional way of doing things and
both could use just one \"Connect\" button or both could have a separate
\"Link\" button. Device *2* could also have an \"Unlink\" button that
sends: `/link/set ii 0 0` if desired.

To use these two devices as one, the \"Connect\" button on both devices
and the \"Link\" button on the second device are pressed in any order.
The two surfaces will now act as one surface with 14 bankable strips.

### Example 2

This example will be more complex and use a total of five devices. The
first three devices will form Link Set *1* and have 8 strips each. They
are similar to the left device above, but will only show \"input\"
strips. The last two devices will form Link Set *2*. Device *1* will be
similar to the first three devices with 8 strips and the other will be
similar to the 6 strip device in example 1 having Master and transport
controls as well. The devices in Link Set 2 will be set up to only use
bus and VCA strips and so don\'t need to include record enable buttons
etc. It is expected that all devices have banking buttons, but at least
one surface in each Link Set would have to have them.

Devices 1 to 3 (from left to right) would each have a \"Connect\" button
that sends: `/set_surface iiiiiiiii 8 3 8323 0 0 0 0 1 n` where *n* is
the position or Link Id of that surface from 1 to 3, left to right.
Device 4 would use: `/set_surface iiiiiiiii 8 156 8323 0 0 0 0 2 1` and
device 5 would use: `/set_surface iiiiiiiii 6 156 8403 0 0 0 0 2 2`.

As before, the \"Connect\" on each surface is pressed in any order and
the resulting surface would have 24 input strips where the banking
buttons on any of the first three surfaces would bank those three
surfaces 24 strips at a time through the input strips (assuming more
than 24 input strips are available). The last two strips would form a
master and bus section with 14 bus only strips that will bank through
the bus strips (assuming more than 14 bus strips). This combined surface
would have 38 strips (plus Master) all together.

## Example 3
{#example3}

In this example there are two devices as in example 1. However, the goal
is to have only input strips on the left device and only bus strips,
Master and transport controls on the right device. In this case linking
is not needed. The left device would use a \"Connect\" button that sent:
`/set_surface iiii 8 3 8323 0` and the right device would use a
\"Connect\" button that sent: `/set_surface iiii 6 156 8403 0`. The
banking buttons on the left surface would bank through the input
channels and the banking buttons on the right surface would bank through
the buses and VCAs. As this example does not use Ardours OSC linking
commands, it will also work with Ardour versions 5.0 to 5.12.
