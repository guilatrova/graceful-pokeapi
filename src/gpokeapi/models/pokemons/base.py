from __future__ import annotations

import typing as t

from gpokeapi.models.base import BasePokemonModel, ResourceName, ResourceReference

from .abilities import AbilityPokemonRef


class Description(t.TypedDict):
    description: str
    """The localized description for an API resource in a specific language."""

    language: ResourceReference
    """The language this name is in."""


class PokemonCharacteristics(t.TypedDict):
    """Characteristics indicate which stat contains a Pokémon's highest IV.
    A Pokémon's Characteristic is determined by the remainder of its highest IV divided by 5 (gene_modulo).
    Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Characteristic) for greater detail."""

    id: int
    """The identifier for this resource."""

    gene_modulo: int
    """The remainder of the highest stat/IV divided by 5."""

    possible_values: int
    """The possible values of the highest stat
    that would result in a Pokémon recieving this characteristic when divided by 5."""

    highest_stat: ResourceReference
    """The stat which results in this characteristic."""

    descriptions: Description
    """	The descriptions of this characteristic listed in different languages."""


class PokemonColor(BasePokemonModel):
    """Colors used for sorting Pokémon in a Pokédex.
    The color listed in the Pokédex is usually the color most apparent or covering each Pokémon's body.
    No orange category exists; Pokémon that are primarily orange are listed as red or brown."""

    names: t.List[ResourceName]
    """The name of this resource listed in different languages."""

    pokemon_species: t.List[ResourceReference]
    """A list of the Pokémon species that have this color."""


class EggGroup(BasePokemonModel):
    """Egg Groups are categories which determine which Pokémon are able to interbreed. Pokémon may belong to either
    one or two Egg Groups. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Egg_Group) for greater detail.
    """

    names: ResourceName
    """The name of this resource listed in different languages."""

    pokemon_species: t.List[ResourceReference]
    """A list of all Pokémon species that are members of this egg group."""


class PokemonSpeciesDetails(t.TypedDict):
    rate: int
    """	The chance of this Pokémon being female, in eighths; or -1 for genderless."""

    pokemon_species: ResourceReference
    """A Pokémon species that can be the referenced gender."""


class PokemonGender(BasePokemonModel):
    """Genders were introduced in Generation II for the purposes of breeding Pokémon but can also result in
    visual differences or even different evolutionary lines.
    Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Gender) for greater detail."""

    pokemon_species_details: t.List[PokemonSpeciesDetails]
    """A list of Pokémon species that can be this gender and how likely it is that they will be."""

    required_for_evolution: t.List[ResourceReference]
    """A list of Pokémon species that required this gender in order for a Pokémon to evolve into them."""


class PokemonFormType(t.TypedDict):
    slot: int
    """The order the Pokémon's types are listed in."""

    type: ResourceReference
    """The type the referenced Form has."""


class PokemonFormSprites(t.TypedDict):
    front_default: str
    """The default depiction of this Pokémon form from the front in battle."""
    front_shiny: str
    """The shiny depiction of this Pokémon form from the front in battle."""
    back_default: str
    """The default depiction of this Pokémon form from the back in battle."""
    back_shiny: str
    """The shiny depiction of this Pokémon form from the back in battle."""


class PokemonForm(BasePokemonModel):
    """Some Pokémon may appear in one of multiple, visually different forms.
    These differences are purely cosmetic. For variations within a Pokémon species, which do differ in more than
    just visuals, the 'Pokémon' entity is used to represent such a variety."""

    order: int
    """The order in which forms should be sorted within all forms.
    Multiple forms may have equal order, in which case they should fall back on sorting by name."""

    form_order: int
    """The order in which forms should be sorted within a species' forms."""

    is_default: bool
    """True for exactly one form used as the default for each Pokémon."""

    is_battle_only: bool
    """Whether or not this form can only happen during battle."""

    is_mega: bool
    """Whether or not this form requires mega evolution."""

    form_name: str
    """The name of this form"""

    pokemon: ResourceReference
    """The Pokémon that can take on this form."""

    types: t.List[PokemonFormType]
    """A list of details showing types this Pokémon form has."""

    sprites: PokemonFormSprites
    """A set of sprites used to depict this Pokémon form in the game."""

    version_group: ResourceName
    """The version group this Pokémon form was introduced in."""

    names: t.List[ResourceName]
    """The form specific full name of this Pokémon form, or empty if the form does not have a specific name."""

    form_names: t.List[ResourceName]
    """The form specific form name of this Pokémon form, or empty if the form does not have a specific name."""


class GrowthRateExperienceLevel(t.TypedDict):
    level: int
    """The level gained."""

    experience: int
    """The amount of experience required to reach the referenced level."""


class GrowthRates(BasePokemonModel):
    """Growth rates are the speed with which Pokémon gain levels through experience.
    Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Experience) for greater detail.
    """

    formula: str
    """The formula used to calculate the rate at which the Pokémon species gains level."""

    descriptions: t.List[Description]
    """The descriptions of this characteristic listed in different languages."""

    levels: str
    """A list of levels and the amount of experienced needed to atain them based on this growth rate."""

    pokemon_species: t.List[ResourceReference]
    """A list of Pokémon species that gain levels at this growth rate."""


class NatureName(t.TypedDict):
    name: str

    language: ResourceReference


class NatureStatChange(t.TypedDict):
    max_change: int
    """The amount of change."""

    pokeathlon_stat: ResourceReference
    """The stat being affected."""


class MoveBattleStylePreference(t.TypedDict):
    low_hp_preference: int
    """Chance of using the move, in percent, if HP is under one half."""

    high_hp_preference: int
    """Chance of using the move, in percent, if HP is over one half."""

    pokeathlon_stat: ResourceReference
    """The move battle style."""


class Nature(BasePokemonModel):
    """Natures influence how a Pokémon's stats grow.
    See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Nature) for greater detail.
    """

    decreased_stat: ResourceReference
    """The stat decreased by 10% in Pokémon with this nature."""

    increased_stat: ResourceReference
    """The stat increased by 10% in Pokémon with this nature."""

    likes_flavor: ResourceReference
    """The flavor liked by Pokémon with this nature."""

    hates_flavor: ResourceReference
    """The flavor hated by Pokémon with this nature."""

    pokeathlon_stat_changes: t.List[NatureStatChange]
    """A list of Pokéathlon stats this nature effects and how much it effects them."""

    move_battle_style_preferences: t.List[MoveBattleStylePreference]
    """A list of battle styles and how likely a Pokémon with this nature is to
    use them in the Battle Palace or Battle Tent."""

    names: t.List[NatureName]
    """The name of this resource listed in different languages."""


class Pokemon(BasePokemonModel):
    """Pokémon are the creatures that inhabit the world of the Pokémon games.
    They can be caught using Pokéballs and trained by battling with other Pokémon.

    Each Pokémon belongs to a specific species but may take on a variant which makes it
    differ from other Pokémon of the same species, such as base stats, available abilities
    and typings.

    See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_(species)) for greater detail."""

    base_experience: int
    """The base experience gained for defeating this Pokémon."""

    height: int
    """The height of this Pokémon in decimetres."""

    is_default: bool
    """Set for exactly one Pokémon used as the default for each species."""

    order: int
    """Order for sorting. Almost national order, except families are grouped together."""

    weight: int
    """The weight of this Pokémon in hectograms."""

    abilities: t.List[AbilityPokemonRef]
    """A list of abilities this Pokémon could potentially have."""

    forms: t.List[ResourceReference]
    """A list of forms this Pokémon can take on."""

    game_indices: t.List[t.Dict]
    """A list of game indices relevent to Pokémon item by generation."""

    held_items: t.List[t.Dict]
    """A list of items this Pokémon may be holding when encountered."""

    location_area_encounters: str
    """A link to a list of location areas, as well as encounter details pertaining to specific versions."""

    moves: t.List[t.Dict]
    """A list of moves along with learn methods and level details pertaining to specific version groups."""

    past_types: t.List[t.Dict]
    """A list of details showing types this pokémon had in previous generations"""

    sprites: t.List[t.Dict]
    """A set of sprites used to depict this Pokémon in the game.
    A visual representation of the various sprites can be found at
    [PokeAPI/sprites](https://github.com/PokeAPI/sprites#sprites)"""

    species: ResourceReference
    """The species this Pokémon belongs to."""

    stats: t.List[t.Dict]
    """A list of base stat values for this Pokémon."""

    types: t.List[t.Dict]
    """A list of details showing types this Pokémon has."""


class PokemonHabitat(BasePokemonModel):
    """Habitats are generally different terrain Pokémon can be found in but can also be areas designated
    for rare or legendary Pokémon."""

    names: t.List[ResourceName]
    """The name of this resource listed in different languages."""

    pokemon_species: t.List[ResourceReference]
    """A list of the Pokémon species that can be found in this habitat."""
