from __future__ import annotations

import typing as t
from gracy import GracyNamespace, GracyOffsetPaginator, parsed_response

from gpokeapi.endpoints import PokeApiEndpoint
from gpokeapi.models.base import ResourceList
from gpokeapi.models.pokemons import abilities as ability_models
from gpokeapi.models.pokemons import base as base_models
from gpokeapi.models.pokemons import encounters as encounter_models

DICT_OR_NONE = t.Union[t.Dict[str, t.Any], None]


class PokemonNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(ResourceList)
    async def list(self, offset: int = 0, limit: int = 20):
        params = dict(offset=offset, limit=limit)
        return await self.get(PokeApiEndpoint.POKEMON_LIST, params=params)

    def paginate(self, limit: int = 20) -> GracyOffsetPaginator[ResourceList]:
        return GracyOffsetPaginator[ResourceList](
            gracy_func=self.list,
            has_next=lambda r: bool(r["next"]) if r else True,
            page_size=limit,
        )

    @parsed_response(base_models.Pokemon)
    async def get_one(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON, dict(KEY=str(name_or_id)))

    @parsed_response(t.List[encounter_models.PokemonLocationArea])
    async def get_encounters(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_ENCOUNTERS, dict(KEY=str(name_or_id)))

    @parsed_response(base_models.PokemonColor)
    async def get_color(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_COLOR, dict(KEY=str(name_or_id)))

    @parsed_response(base_models.PokemonForm)
    async def get_form(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_FORM, dict(KEY=str(name_or_id)))

    @parsed_response(base_models.PokemonHabitat)
    async def get_habitat(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_HABITAT, dict(KEY=str(name_or_id)))

    @parsed_response(base_models.PokemonShape)
    async def get_shape(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_SHAPE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_species(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEMON_SPECIES, dict(KEY=str(name_or_id)))

    @parsed_response(base_models.EggGroup)
    async def get_egg_group(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.EGG_GROUP, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_growth_rate(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.GROWTH_RATE, dict(KEY=str(name_or_id)))

    @parsed_response(base_models.Nature)
    async def get_nature(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.NATURE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_pokeathlon_stat(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEATHLON_STAT, dict(KEY=str(name_or_id)))

    @parsed_response(ability_models.AbilityPokemonRef)
    async def get_ability(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.ABILITY, dict(KEY=str(name_or_id)))

    @parsed_response(base_models.PokemonCharacteristics)
    async def get_characteristic(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.CHARACTERISTIC, dict(KEY=str(name_or_id)))

    @parsed_response(base_models.PokemonGender)
    async def get_gender(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.GENDER, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_type(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.TYPE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_stat(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.STAT, dict(KEY=str(name_or_id)))
