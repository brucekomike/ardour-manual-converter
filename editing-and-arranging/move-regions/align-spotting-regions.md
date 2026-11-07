# Align (Spot) Regions
Aligning regions (sometimes called \"spotting\") means moving one or
more regions based on a defined location, which in Ardour is always the
[edit point](@@edit-point-control). An alignment operation moves the
region(s) so that some part of the region is positioned at the edit
point. Available alignment commands include:

|  |  |
|----|----|
| Align Region starts [a]{.kbd .mod14} | Selected region(s) are moved so that their start is located at the current edit point |
| Align Region ends [a]{.kbd .mod2} | Selected region(s) are moved so that the end is located at the current edit point |
| Align Region sync points [a]{.kbd .mod3} | Selected region(s) are moved so that their sync point is located at the current edit point |
| Align Region starts relative [a]{.kbd .key} | Selected region(s) are moved so that the start of the earliest region is located at the current edit point, and all others maintain their relative position relative to that region |
