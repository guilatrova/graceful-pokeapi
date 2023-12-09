from __future__ import annotations

import typing as t

from gpokeapi.models.base import FlavorText as BaseFlavorText
from gpokeapi.models.base import ResourceName, ResourceReference


class Effect(t.TypedDict):
    effect: str
    """	The localized effect text for an API resource in a specific language."""

    language: ResourceReference
    """The language this effect is in."""


class VerboseEffect(Effect):
    short_effect: str
    """The localized effect text in brief."""


class AbilityEffectChange(t.TypedDict):
    version_group: ResourceReference
    """The version group in which the previous effect of this ability originated."""

    effect_entries: t.List[Effect]
    """The previous effect of this ability listed in different languages."""


class FlavorTextEntriesItem(BaseFlavorText):
    version_group: ResourceReference
    """The game version this flavor text is extracted from."""


class AbilityPokemonRef(t.TypedDict):
    is_hidden: bool
    """Whether or not this a hidden ability for the referenced Pokémon."""

    slot: int
    """Pokémon have 3 ability 'slots' which hold references to possible abilities they could have.
    This is the slot of this ability for the referenced pokemon."""

    pokemon: ResourceReference
    """The Pokémon this ability could belong to."""


class PokemonAbility(t.TypedDict):
    """Abilities provide passive effects for Pokémon in battle or in the overworld.
    Pokémon have multiple possible abilities but can have only one ability at a time.
    Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Ability) for greater detail.
    """

    id: int
    """The identifier for this resource."""

    name: str
    """The name for this resource."""

    is_main_series: bool
    """Whether or not this ability originated in the main series of the video games."""

    generation: ResourceReference
    """The generation this ability originated in."""

    names: t.List[ResourceName]
    """The name of this resource listed in different languages."""

    effect_entries: t.List[VerboseEffect]
    """The effect of this ability listed in different languages."""

    effect_changes: t.List[AbilityEffectChange]
    """The list of previous effects this ability has had across version groups."""

    flavor_text_entries: t.List[FlavorTextEntriesItem]
    """The flavor text of this ability listed in different languages."""

    pokemon: t.List[AbilityPokemonRef]
    """A list of Pokémon that could potentially have this ability."""
