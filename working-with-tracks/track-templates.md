# Track Templates
<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/track-template-in-add-track-dialog.png" width="400"
alt="Selecting a track template" />
<figcaption aria-hidden="true">Selecting a track template</figcaption>
</figure>

Track templates simplify recording of new material by reusing tried and
true I/O and processing settings. They are listed in the [Add
Track/Bus/VCA]{.kbd .menu} dialog below regular options such as audio
and tracks, busses, and VCAs.

Each track templates stores the entire state of a track it was created
from:

-   I/O configuration including sends and inserts
-   State of mixer controls (mute, solo, solo iso/lock etc.)
-   All the processors and their settings

## Creating track templates

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/track-save-as-template-dialog.png" width="200"
alt="Save As Template" />
<figcaption aria-hidden="true">Save As Template</figcaption>
</figure>

To create a new track template, [right]{.kbd .mouse}-click the name of
the track in its mixer channel and select [Save Track Template...]{.kbd
.menu}

In the newly opened dialog, add a description for the template, then
give it a name that will be displayed in the [Add Track/Bus/VCA]{.kbd
.menu} dialog, click [Save]{.kbd}.

A slightly verbose description of a template will be helpful when there
are multiple similar templates available.

## Managing track templates

<figure class="right">
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/track-templates.png" width="400"
alt="Track templates management" />
<figcaption aria-hidden="true">Track templates management</figcaption>
</figure>

Track templates are managed in the same dialog as session templates.

You can rename existing templates to help differentiate between similar
options, change the description, or remove an existing template.

Additionally, you can export all track templates to an archive for
sharing, or import track templates from an archive that someone shared
with you.
