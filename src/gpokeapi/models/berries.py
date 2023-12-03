from __future__ import annotations

import typing as t

from gpokeapi.models.base import ResourceName, ResourceReference


class FlavorBerryMap(t.TypedDict):
    potency: int
    """How powerful the referenced flavor is for this berry."""
    flavor: ResourceReference
    """The referenced berry flavor."""


class Berry(t.TypedDict):
    """
    Berries are small fruits that can provide HP and status condition restoration, stat enhancement, and even
    damage negation when eaten by Pokémon. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Berry)
    for greater detail.
    """

    id: int
    """	The identifier for this resource."""

    name: str
    """The name for this resource."""

    growth_time: int
    """Time it takes the tree to grow one stage, in hours.
    Berry trees go through four of these growth stages before they can be picked."""

    max_harvest: int
    """The maximum number of these berries that can grow on one tree in Generation IV."""

    natural_gift_power: int
    """The power of the move "Natural Gift" when used with this Berry."""

    size: int
    """The size of this Berry, in millimeters."""

    smoothness: int
    """	The smoothness of this Berry, used in making Pokéblocks or Poffins."""

    soil_dryness: int
    """The speed at which this Berry dries out the soil as it grows. A higher rate means the soil dries more quickly."""

    firmness: ResourceReference
    """	The firmness of this berry, used in making Pokéblocks or Poffins."""

    flavors: t.List[FlavorBerryMap]
    """A list of references to each flavor a berry can have and the potency of each of
    those flavors in regard to this berry."""

    item: ResourceReference
    """Berries are actually items. This is a reference to the item specific data for this berry."""

    natural_gift_type: ResourceReference
    """The type inherited by "Natural Gift" when used with this Berry."""


class BerryFirmness(t.TypedDict):
    """Berries can be soft or hard.
    Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Category:Berries_by_firmness) for greater detail."""

    id: str
    """The identifier for this resource."""

    name: str
    """The name for this resource."""

    berries: t.List[ResourceReference]
    """A list of the berries with this firmness."""

    names: t.List[ResourceName]
    """The name of this resource listed in different languages."""


class BerryFlavor(t.TypedDict):
    """Flavors determine whether a Pokémon will benefit or suffer from eating a berry based on their
    [nature](https://pokeapi.co/docs/v2#natures).
    Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Flavor) for greater detail."""

    id: str
    """The identifier for this resource."""

    name: str
    """The name for this resource."""

    berries: t.List[FlavorBerryMap]
    """A list of the berries with this flavor."""

    contest_type: ResourceReference
    """The contest type that correlates with this berry flavor."""

    names: t.List[ResourceName]
    """The name of this resource listed in different languages."""
