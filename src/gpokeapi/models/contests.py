import typing as t

from gpokeapi.models.base import ResourceName, ResourceReference


class ContestName(ResourceName):
    color: str
    """The color associated with this contest's name."""


class ContestType(t.TypedDict):
    id: str
    """The identifier for this resource."""

    name: str
    """The name for this resource."""

    berry_flavor: ResourceReference
    """The berry flavor that correlates with this contest type."""

    names: list[ContestName]
    """The name of this contest type listed in different languages."""


class EffectEntry(t.TypedDict):
    effect: str
    language: ResourceReference


class FlavorText(t.TypedDict):
    flavor_text: str
    language: ResourceReference


class ContestEffect(t.TypedDict):
    id: str
    """The identifier for this resource."""

    appeal: int
    """The base number of hearts the user of this move gets."""

    jam: int
    """The base number of hearts the user's opponent loses."""

    effect_entries: list[EffectEntry]
    """The result of this contest effect listed in different languages."""

    flavor_text_entries: list[FlavorText]
    """The flavor text of this contest effect listed in different languages."""


class SuperContestEffect(t.TypedDict):
    id: str
    """The identifier for this resource."""

    appeal: int
    """The base number of hearts the user of this move gets."""

    flavor_text_entries: list[FlavorText]
    """The flavor text of this contest effect listed in different languages."""

    moves: list[ResourceReference]
    """A list of moves that have the effect when used in super contests."""