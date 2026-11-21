# Comparing Aux Sends and Subgroups
Auxes and Subgroups share a common concept---they both provide a way for
one or more tracks (or busses) to send their signal to a single bus so
that common signal processing can be applied to the mix of their
signals.

[Aux sends]{.dfn} leave the existing signal routing to the main mix in
place, and are typically used to create a separate mix to send to (for
example) monitors or headphones (for performer monitor mixes):

![Aux signal routing](https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/aux_routing.png){.invert-in-dark
width="300px"}

[Subgroups]{.dfn} usually remove the original signal routing to the main
mix and replace it with a new one that delivers the output of the
subgroup bus to the main mix instead.

<figure>
<img src="https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/subgroup_routes.png" class="invert-in-dark"
width="300" alt="sub group signal routing" />
<figcaption>Sub group signal routing</figcaption>
</figure>
