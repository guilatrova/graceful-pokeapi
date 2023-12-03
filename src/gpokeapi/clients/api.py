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

        self._pokemon_ns = PokemonNamespace(self)
        self._berry_ns = BerryNamespace(self)
        self._item_ns = ItemNamespace(self)
        self._encounter_ns = EncountersNamespace(self)
        self._move_ns = MoveNamespace(self)
        self._evolution_ns = EvolutionNamespace(self)
        self._contest_ns = ContestNamespace(self)

    @property
    def pokemon(self):
        return self._pokemon_ns

    @property
    def berry(self):
        return self._berry_ns

    @property
    def item(self):
        return self._item_ns

    @property
    def encounter(self):
        return self._encounter_ns

    @property
    def move(self):
        return self._move_ns

    @property
    def evolution(self):
        return self._evolution_ns

    @property
    def contest(self):
        return self._contest_ns

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
