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


class AbilityPokemon(t.TypedDict):
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

    pokemon: t.List[AbilityPokemon]
    """A list of Pokémon that could potentially have this ability."""


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


class EggGroup(t.TypedDict):
    """Egg Groups are categories which determine which Pokémon are able to interbreed. Pokémon may belong to either
    one or two Egg Groups. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Egg_Group) for greater detail.
    """

    id: int
    """The identifier for this resource."""

    name: str
    """The name for this resource."""

    names: ResourceName
    """The name of this resource listed in different languages."""

    pokemon_species: t.List[ResourceReference]
    """A list of all Pokémon species that are members of this egg group."""


class PokemonSpeciesDetails(t.TypedDict):
    rate: int
    """	The chance of this Pokémon being female, in eighths; or -1 for genderless."""

    pokemon_species: ResourceReference
    """A Pokémon species that can be the referenced gender."""


class PokemonGender(t.TypedDict):
    """Genders were introduced in Generation II for the purposes of breeding Pokémon but can also result in
    visual differences or even different evolutionary lines.
    Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Gender) for greater detail."""

    id: int
    """The identifier for this resource."""

    name: str
    """The name for this resource."""

    pokemon_species_details: t.List[PokemonSpeciesDetails]
    """A list of Pokémon species that can be this gender and how likely it is that they will be."""

    required_for_evolution: t.List[ResourceReference]
    """A list of Pokémon species that required this gender in order for a Pokémon to evolve into them."""


class GrowthRateExperienceLevel(t.TypedDict):
    level: int
    """The level gained."""

    experience: int
    """The amount of experience required to reach the referenced level."""


class GrowthRates(t.TypedDict):
    """Growth rates are the speed with which Pokémon gain levels through experience.
    Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Experience) for greater detail.
    """

    id: int
    """The identifier for this resource."""

    name: str
    """The name for this resource."""

    formula: str
    """The formula used to calculate the rate at which the Pokémon species gains level."""

    descriptions: t.List[Description]
    """The descriptions of this characteristic listed in different languages."""

    levels: str
    """A list of levels and the amount of experienced needed to atain them based on this growth rate."""

    pokemon_species: t.List[ResourceReference]
    """A list of Pokémon species that gain levels at this growth rate."""
