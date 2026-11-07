# Navigating the Editor
Navigating the Editor window is obviously a very frequent operation.
Ardour sticks with a lot of the usual conventions in this regard, to
allow for a quick learning. As those operations are so common, it is
worth taking the time to learn most of the keyboard and mouse shortcuts
in order for these to become fast and natural.

The keyboard shortcuts can, as always, be edited, so the defaults are
shown here.

## Scrolling

Scrolling can be done on-canvas, or with the [Summary](@@summary).

### On Canvas

| Action                  | Mouse                  | Keyboard  |
|-------------------------|------------------------|-----------|
| Scrolling up            | [⇑]{.kbd .mouse}       | [↑]{.kbd} |
| Scrolling down          | [⇓]{.kbd .mouse}       | [↓]{.kbd} |
| Scrolling up one page   |                        | [⇞]{.kbd} |
| Scrolling down one page |                        | [⇟]{.kbd} |
| Scrolling left          | [⇑]{.kbd .mod3 .mouse} |           |
| Scrolling right         | [⇓]{.kbd .mod3 .mouse} |           |

Moving the playhead outside the view may scroll the screen accordingly,
so using [←]{.kbd .mod2} or [→]{.kbd .mod2}, while not *scrolling* per
se, will result in scrolling if [Transport \> Follow playhead]{.kbd
.option} is checked. This is also true with the [Navigation
Timeline](@@mini-timeline), and anything that moves the Playhead.

### In the Summary

Clicking and dragging in the Summary will scroll the view left and
right. If the screen view is clicked (the white rectangle) and dragged,
the view can also be scrolled vertically.

Additionally, on the left and the right of the Summary, the two
[\<]{.kbd .menu} and [\>]{.kbd .menu} arrows buttons allow to scroll one
screen either left or right.

## Zooming

Zooming (on time) can be done on-canvas (which will always be centered
around the mouse cursor), with the Summary, or with the [Zoom
Controls](@@zoom-controls).

### On Canvas

|             |                        |
|-------------|------------------------|
| Zooming in  | [⇑]{.kbd .mod1 .mouse} |
| Zooming out | [⇓]{.kbd .mod1 .mouse} |

### In the Summary

Resizing the screen view in the Summary (the white rectangle) changes
the zoom accordingly.

### With the Zoom Controls

With the Zoom Focus set, the [−]{.kbd} and [+]{.kbd} buttons will zoom
out or in around this focus. The [\[ \]]{.kbd} button zooms to the whole
session as defined by the start and end markers.

These controls are bound to the keyboard [−]{.kbd} and [=]{.kbd}
respectively by default.

## Height of the tracks

Changing the height of the tracks results in more or less tracks on
screen. This can be done on canvas, with the Summary or with the Zoom
Controls.

### On canvas

Using [⇓]{.kbd .mod2 .mouse} or [⇑]{.kbd .mod2 .mouse} while hovering
over a track reduces or enhances its height, i.e. zooms on the hovered
track, regardless of the selection.

The [F]{.kbd} key resizes the tracks so that only the selected one(s)
are displayed. If some unselected tracks are in-between those selected
tracks, their [visibility](@@the-tracks-and-busses-list) will be toggled
off.

### In the Summary

Resizing the screen view in the Summary (the white rectangle) changes
the number of tracks displayed (hence their heights) accordingly. It
behaves more like a zoom as the relative height of the tracks are kept.

### With the Zoom Controls

The three rightmost buttons of the Zoom Control bar, while not zoom
buttons, act upon the height of the tracks:

- The first selector directly selects how many tracks are currently on
  screen.
- The second one reduces the height of the selected track(s). If none
  are selected, all the tracks are affected, while maintaining (as long
  as it is possible) their relative heights.
- The third one enlarges the tracks, and is the counterpart of the
  previous one.
