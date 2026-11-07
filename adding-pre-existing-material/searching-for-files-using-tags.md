# Searching for Files Using Tags
A [tag]{.dfn} is bit of information, or metadata, that is associated
with a data file. Specifically, tags are texts, keywords or terms that
have some relevance to a particular sound file. Ardour can store these
tags in a searchable [database]{.dfn} so that they can quickly be
searched for to retrieve sounds based on the tags that have been
assigned to them.

For example if the term [120bpm]{.kbd .input} has been assigned to a
sound, search later for this tag will make the file appear in the search
list. Tags are independent of the filename or anything else about the
file. Tags, and the file paths that they are associated with, are stored
in a file called `sfdb`{.sample} in the Ardour user folder.

## Creating and adding tags

Adding tags to a given file is done by opening the [Session \>
Import]{.kbd .menu} dialog, selecting the file in the browser, and
typing new tags into the tag area in the soundfile information box on
the right.

Tags are stored when the input box loses focus, there is no need to
explicitly save them.

To have more than one tag for a file, new tags can either be added on
new lines (meaning the [Enter]{.kbd} key is pressed between two tags) or
they can be separated from the previous ones by a comma ([,]{.kbd
.input}), with or without spaces.

## Searching for files by tag

Searching for specific tags is done in the [Search Tags]{.kbd .menu} tab
of the same dialog. Files which have been tagged with the relevant terms
will appear in the results window. Selected files can be auditioned and
marked with additional tags if required.
