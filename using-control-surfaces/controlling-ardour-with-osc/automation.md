# Automation
Ardour has automation modes for many of its controls. As of version 5.9,
OSC can control what automation mode a fader uses. ([See
Automation.](@@automation))

The form of the automation mode command is:

`/strip/[control]/automation ii ssid mode`

- /strip may also be /select in which case the only parameter is the
  mode.
- \[control\] as of Ardour version 5.9 control can be:
  - gain
  - fader

  This list will expand.
- ssid can be a parameter as shown or inline (automation/\[ssid\]).
  /select has no ssid.
- mode can be one of:
  - `0` Manual mode
  - `1` Play mode
  - `2` Write mode
  - `3` Touch mode

  The mode value may be sent as a float allowing a \"pot\" or \"slider\"
  with a range of 0 to 3 to be used to control mode.

The next version of Ardour will add
`/strip/[control]/automation_name is ssid mode_name` as feedback. A
surface may choose to use only the first character of the string (M, P,
W or T) instead of the whole string (this is in git now).

The touch mode needs more input so there is a Touch command as well
(added post 5.9). It is almost identical to the automation command:

`/strip/[control]/touch ii ssid touch`

The only difference is the last parameter is 1 for touched and 0 for
touch released. All of the rest of the explanation above applies.
