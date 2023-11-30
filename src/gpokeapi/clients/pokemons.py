import typing as t

from gpokeapi.endpoints import PokeApiEndpoint
from gracy import GracyNamespace, parsed_response

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
