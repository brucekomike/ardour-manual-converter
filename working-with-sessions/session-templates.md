# Session Templates
[Session templates]{.dfn} are a way to store the setup of a session for
future use. They do not store any *audio* data but can store:

-   The number of tracks and busses, along with their names
-   The plugins present on each track or bus (if any)
-   All I/O connections

## Creating a Session Template

The [Session \> Save Template]{.kbd .menu} shows a dialog asking for the
name of the new template, and a description.

## Using a Session Template

In the [New Session dialog](@@newopen-session-dialog), a panel lists the
different template (factory and user-created).

## Managing Templates

To manage templates, choose **Window** \> **Templates**. To access this
menu item, you have to have a session open.

![The Manage Templates window](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/manage_templates.png)

Both Session templates and Track Templates can be managed through the
Manage Templates window, which can perform the following actions:

-   Renaming a template
-   Removing one
-   Adding/modifying its description
-   Exporting the templates (e.g. to be used in another Ardour instance)
-   Importing templates (from e.g. another Ardour instance).

See also [Adding Tracks and Busses](@@adding-tracks-busses-and-vcas) for
information on templates for individual tracks or busses.
