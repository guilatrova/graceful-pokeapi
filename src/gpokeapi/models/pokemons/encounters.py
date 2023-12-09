from __future__ import annotations

import typing as t

from gpokeapi.models.base import ResourceName, ResourceReference


class VersionEncounterDetail(t.TypedDict):
    version: ResourceReference
    """The game version this encounter happens in."""

    max_chance: int
    """The total percentage of all encounter potential."""

    encounter_details: t.List[str]
    """A list of encounters and their specifics."""


class Encounter(t.TypedDict):
    min_level: int
    """The lowest level the Pokémon could be encountered at."""

    max_level: int
    """The highest level the Pokémon could be encountered at."""

    condition_values: t.List[ResourceReference]
    """A list of condition values that must be in effect for this encounter to occur."""

    chance: int
    """Percent chance that this encounter will occur."""

    method: ResourceName
    """The method by which this encounter happens."""


class PokemonLocationArea(t.TypedDict):
    """Pokémon Location Areas are ares where Pokémon can be found."""

    name: ResourceReference
    """The location area the referenced Pokémon can be encountered in."""

    version_details: t.List[VersionEncounterDetail]
    """A list of versions and encounters with the referenced Pokémon that might happen."""
