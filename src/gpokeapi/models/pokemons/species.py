from __future__ import annotations

import typing as t

from gpokeapi.models.base import BasePokemonModel, FlavorText, ResourceName, ResourceReference
from gpokeapi.models.pokemons.base import Description


class PokemonSpeciesDexEntry(t.TypedDict):
    entry_number: int
    pokedex: ResourceName


class Genus(t.TypedDict):
    genus: str
    """The localized genus for the referenced Pokémon species."""
    language: ResourceReference


class PokemonSpeciesVariety(t.TypedDict):
    is_default: bool
    pokemon: ResourceReference


class PokemonSpecies(BasePokemonModel):
    """A Pokémon Species forms the basis for at least one Pokémon. Attributes of a Pokémon species are shared across all varieties of Pokémon within the species. A good example is Wormadam; Wormadam is the species which can be found in three different varieties, Wormadam-Trash, Wormadam-Sandy and Wormadam-Plant."""

    order: int
    gender_rate: int
    capture_rate: int
    base_happiness: int
    is_baby: bool
    is_legendary: bool
    is_mythical: bool
    hatch_counter: int
    has_gender_differences: bool
    forms_switchable: bool
    growth_rate: ResourceReference
    pokedex_numbers: t.List[PokemonSpeciesDexEntry]
    egg_groups: t.List[ResourceReference]
    color: ResourceReference
    shape: ResourceReference
    evolves_from_species: t.Optional[ResourceReference]
    evolution_chain: ResourceReference
    habitat: t.Optional[ResourceReference]
    generation: ResourceReference
    names: t.List[ResourceName]
    flavor_text_entries: t.List[FlavorText]
    form_descriptions: t.List[Description]
    genera: t.List[Genus]
    varieties: t.List[PokemonSpeciesVariety]
