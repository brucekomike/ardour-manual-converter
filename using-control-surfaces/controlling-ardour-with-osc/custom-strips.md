# Custom Strip Lists
It is sometimes desirable to work only with a set of strips out of the
whole list of available strips. This could be in any case where there is
more than one engineer and one of them is responsible for only a group
of strips such as all percussion, all sound effects, choir only,
orchestra only, etc.

New Ardour 6.0

After a strip is added to the custom strip list, it will retain the same
SSID for the life of the session so long as banking is not used. If a
strip is removed it will leave a gap in the SSID list. Custom strip
lists do not survive a session reload and need to be recreated at
session start.

A custom strip list will only affect the surface that sets it. Any other
surface will continue to operate on all strips or may have it\'s own set
of custom strips.

The commands below control the use of a custom strip set.

|  |  |
|----|----|
| [/strip/listen *ssid* *\...*]{.kbd .osc} | where *ssid* is an integer or list of integers representing tracks to add to the custom track list |
| [/strip/ignore *ssid* *\...*]{.kbd .osc} | where *ssid* is an integer or list of integers representing tracks to remove from the custom track list |
| [/strip/custom/mode *mode*]{.kbd .osc} | where *mode* is an integer representing the desired mode of custom strips. |
| [/strip/custom/clear ]{.kbd .osc} | disables custom strips and clears the previously set custom strip list |

## Setting up a custom strip set

The control surface may set up a custom strip list all at once or one
strip at a time. A control surface that uses banking would probably be
best served by setting up one strip at a time, while one that does no
banking (bank_size = 0) and uses `/strip/list` would probably be best
served by having them all selected at once.

- One at a time example:

  `/strip/listen 2`

  adds strip 2 to custom strip list

- Many at a time example:

  `/strip/listen 2 4 6 8`

  Adds strips 2, 4, 6 and 8 to the custom strip list

`/strip/listen` will only work with custom enable turned off. Using
`/strip/listen` while in custom mode will have no effect.

## Using the custom strip set

Once the custom strip set has been set up as shown above, it must be
enabled. This is done from the control surface with the
`/strip/custom/mode `*`mode`* OSC command. *Mode* may be *0*: Off, *1*:
Use custom strip set in selected order or *2*: Use custom strip set in
mixer order. `/strip/list` will now show the custom strip list and and
its SSIDs. No more strips may be added to the custom strip list while in
custom mode. To add more strips to the end of the list, first send the
`/strip/custom/mode 0` then more strips can be added to the end of the
list. After adding the next strips send the
`/strip/custom/mode `*`mode`* to re-enable custom mode. It is possible
to switch back and forth between normal and custom mode as desired.

### Custom Strip ordering

The ordering of strips in the custom strip set is affected by both the
custom `mode` and the `bank_size` setting for the surface.

A `bank_size` of *0* is also described as having banking turned off. In
such a case all strips are shown.

- #### Mode 0

  Custom mode *Off*. All strips will be used as set by `strip_types`.

- #### Mode 1

  If `mode` is set to *1* the custom strip ordering is always \"first
  come, first served\". That is, `/strip/listen 2 4` followed by
  `/strip/listen 1 3` will result in strip 2 showing as SSID 1 , strip 4
  as SSID 2, strip 1 as SSID 3 and strip 3 as SSID 4 when in custom mode
  *1*. Once these SSID are set in this way, they will remain linked to
  this SSID with banking turned off and will at least remain in the same
  order with banking on.

- #### Mode 2

  If `mode` is set to *2* the custom strip ordering will be set to mixer
  order and any deleted strips will not leave a blank strip in the set.

- #### With banking on

  If `bank_size` is set to greater than *0*, Then banking is turned on.
  In this case `strip_types` will be honored and only strips from the
  custom strip set that match `strip_types` will be shown in a bank.
  However, the order that the strips appear will still be affected by
  the `mode`.

## Removing a strip from the custom strip list

`/strip/ignore ssid` will remove that strip from the custom strip list
if custom strip use is enabled. In `mode` *1* there will be a blank
strip at that SSID and all other SSIDs will remain the same for no
banking. With banking in use, `strip_types` are honored and so removed
strips which have no type, will not be shown.

`/strip/custom/clear` will remove all strips and SSIDs allowing custom
strip lists to be restarted from SSID 1. Custom `mode` will be set to
*0*.
