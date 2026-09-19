# Monitor Setup in Ardour
Ardour has two main settings which affect how monitoring is performed.
The first is [Edit \> Preferences \> Monitoring \> Record monitoring
handled by]{.kbd .menu}. There are two or three options here, depending
on the capabilities of the hardware.

The other setting is the [Session \> Properties \> Track Input
Monitoring automatically follows transport state (auto-input)]{.kbd
.option}.

Monitoring also depends on the state of the track\'s record-enable
button and the session record-enable button, as well as on whether or
not the transport is rolling.

If Ardour is set to [external monitoring]{.dfn}, Ardour does not do any
monitoring.
