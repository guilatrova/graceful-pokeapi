import typing as t
from gracy import GracyNamespace, parsed_response

from gpokeapi.endpoints import PokeApiEndpoint
from gpokeapi.models import pokemons as models

DICT_OR_NONE = t.Union[t.Dict[str, t.Any], None]


class PokemonNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(DICT_OR_NONE)
    async def get_one(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_encounters(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_ENCOUNTERS, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_color(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_COLOR, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_form(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_FORM, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_habitat(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_HABITAT, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_shape(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_SHAPE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_species(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_SPECIES, dict(KEY=str(name_or_id)))

    @parsed_response(models.EggGroup)
    async def get_egg_group(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.EGG_GROUP, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_growth_rate(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.GROWTH_RATE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_nature(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.NATURE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_pokeathlon_stat(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEATHLON_STAT, dict(KEY=str(name_or_id)))

    @parsed_response(models.AbilityPokemon)
    async def get_ability(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.ABILITY, dict(KEY=str(name_or_id)))

    @parsed_response(models.PokemonCharacteristics)
    async def get_characteristic(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.CHARACTERISTIC, dict(KEY=str(name_or_id)))

    @parsed_response(models.PokemonGender)
    async def get_gender(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.GENDER, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_type(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.TYPE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_stat(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.STAT, dict(KEY=str(name_or_id)))
