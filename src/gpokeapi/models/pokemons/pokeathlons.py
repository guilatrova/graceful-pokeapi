from __future__ import annotations

import typing as t

from gpokeapi.models.base import BasePokemonModel, ResourceName, ResourceReference


class NaturePokeathlonStatAffect(t.TypedDict):
    max_change: int
    """The maximum amount of change to the referenced Pokéathlon stat."""

    nature: ResourceReference
    """The nature causing the change."""


class PokeathlonStat(BasePokemonModel):
    affecting_natures: t.Dict[t.Literal["increase", "decrease"], t.List[NaturePokeathlonStatAffect]]
    names: t.List[ResourceName]
