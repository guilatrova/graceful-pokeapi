from __future__ import annotations

import typing as t
from gracy import Gracy, GracyConfig, GracyReplay, LogEvent, LogLevel, parsed_response
from gracy.replays.storages.sqlite import SQLiteReplayStorage
from http import HTTPStatus

from gpokeapi.clients.berries import BerryNamespace
from gpokeapi.clients.contests import ContestNamespace
from gpokeapi.clients.encounters import EncountersNamespace
from gpokeapi.clients.evolutions import EvolutionNamespace
from gpokeapi.clients.items import ItemNamespace
from gpokeapi.clients.moves import MoveNamespace
from gpokeapi.clients.pokemons import PokemonNamespace
from gpokeapi.endpoints import PokeApiEndpoint
from gpokeapi.replays import InMemoryStorage

CACHE_TYPE = t.Union[t.Literal["memory", "sqlite"], GracyReplay]
DICT_OR_NONE = t.Union[t.Dict[str, t.Any], None]


class PokeApi(Gracy[PokeApiEndpoint]):
    class Config:
        BASE_URL = "https://pokeapi.co/api/v2/"
        REQUEST_TIMEOUT = 5.0
        SETTINGS = GracyConfig(
            parser={
                HTTPStatus.OK: lambda resp: resp.json(),
                HTTPStatus.NOT_FOUND: None,
            },
            allowed_status_code=HTTPStatus.NOT_FOUND,
            log_errors=LogEvent(LogLevel.ERROR),
        )

    def __init__(self, cache: CACHE_TYPE = "memory") -> None:
        if cache == "memory":
            storage = InMemoryStorage()
            replay = GracyReplay("smart-replay", storage)

        elif cache == "sqlite":
            storage = SQLiteReplayStorage(".pokeapi.sqlite3")
            replay = GracyReplay("smart-replay", storage)

        else:
            replay = cache

        super().__init__(replay=replay)

    pokemon: PokemonNamespace
    berry: BerryNamespace
    item: ItemNamespace
    encounter: EncountersNamespace
    move: MoveNamespace
    evolution: EvolutionNamespace
    contest: ContestNamespace

    @parsed_response(DICT_OR_NONE)
    async def get_generation(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.GENERATION, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_language(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.LANGUAGE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_location(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.LOCATION, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_location_area(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.LOCATION_AREA, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_machine(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.MACHINE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_pal_park_area(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.PAL_PARK_AREA, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_pokedex(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.POKEDEX, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_region(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.REGION, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_version(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.VERSION, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_version_group(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.VERSION_GROUP, dict(KEY=str(name_or_id)))
