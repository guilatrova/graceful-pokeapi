import typing as t
from http import HTTPStatus

from gracy import Gracy, GracyConfig, GracyReplay, LogEvent, LogLevel
from gracy.replays.storages.sqlite import SQLiteReplayStorage

from .endpoints import PokeApiEndpoint
from .replays import InMemoryStorage

CACHE_TYPE = t.Union[t.Literal["memory", "sqlite"], GracyReplay]
RESP_TYPE = t.Union[t.Dict[str, t.Any], None]


class PokeApi(Gracy[PokeApiEndpoint]):
    class Config:  # type: ignore
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

    async def get_ability(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.ABILITY, dict(KEY=str(name_or_id))))

    async def get_berry(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.BERRY, dict(KEY=str(name_or_id))))

    async def get_berry_flavor(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.BERRY_FLAVOR, dict(KEY=str(name_or_id))))

    async def get_berry_firmness(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.BERRY_FIRMNESS, dict(KEY=str(name_or_id))))

    async def get_characteristic(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.CHARACTERISTIC, dict(KEY=str(name_or_id))))

    async def get_contest_effect(self, id: int) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.CONTEST_EFFECT, dict(KEY=str(id))))

    async def get_contest_type(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.CONTEST_TYPE, dict(KEY=str(name_or_id))))

    async def get_egg_group(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.EGG_GROUP, dict(KEY=str(name_or_id))))

    async def get_encounter_condition(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.ENCOUNTER_CONDITION, dict(KEY=str(name_or_id))))

    async def get_encounter_condition_value(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.ENCOUNTER_CONDITION_VALUE, dict(KEY=str(name_or_id))))

    async def get_encounter_method(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.ENCOUNTER_METHOD, dict(KEY=str(name_or_id))))

    async def get_evolution_chain(self, id: int) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.EVOLUTION_CHAIN, dict(KEY=str(id))))

    async def get_evolution_trigger(self, id: int) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.EVOLUTION_TRIGGER, dict(KEY=str(id))))

    async def get_gender(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.GENDER, dict(KEY=str(name_or_id))))

    async def get_generation(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.GENERATION, dict(KEY=str(name_or_id))))

    async def get_growth_rate(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.GROWTH_RATE, dict(KEY=str(name_or_id))))

    async def get_item(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.ITEM, dict(KEY=str(name_or_id))))

    async def get_item_attribute(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.ITEM_ATTRIBUTE, dict(KEY=str(name_or_id))))

    async def get_item_category(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.ITEM_CATEGORY, dict(KEY=str(name_or_id))))

    async def get_item_fling_effect(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.ITEM_FLING_EFFECT, dict(KEY=str(name_or_id))))

    async def get_item_pocket(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.ITEM_POCKET, dict(KEY=str(name_or_id))))

    async def get_language(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.LANGUAGE, dict(KEY=str(name_or_id))))

    async def get_location(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.LOCATION, dict(KEY=str(name_or_id))))

    async def get_location_area(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.LOCATION_AREA, dict(KEY=str(name_or_id))))

    async def get_machine(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.MACHINE, dict(KEY=str(name_or_id))))

    async def get_move(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.MOVE, dict(KEY=str(name_or_id))))

    async def get_move_ailment(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.MOVE_AILMENT, dict(KEY=str(name_or_id))))

    async def get_move_battle_style(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.MOVE_BATTLE_STYLE, dict(KEY=str(name_or_id))))

    async def get_move_category(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.MOVE_CATEGORY, dict(KEY=str(name_or_id))))

    async def get_move_damage_class(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.MOVE_DAMAGE_CLASS, dict(KEY=str(name_or_id))))

    async def get_move_learn_method(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.MOVE_LEARN_METHOD, dict(KEY=str(name_or_id))))

    async def get_move_target(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.MOVE_TARGET, dict(KEY=str(name_or_id))))

    async def get_nature(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.NATURE, dict(KEY=str(name_or_id))))

    async def get_pal_park_area(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.PAL_PARK_AREA, dict(KEY=str(name_or_id))))

    async def get_pokeathlon_stat(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.POKEATHLON_STAT, dict(KEY=str(name_or_id))))

    async def get_pokedex(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.POKEDEX, dict(KEY=str(name_or_id))))

    async def get_pokemon(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.POKEMON, dict(KEY=str(name_or_id))))

    async def get_pokemon_color(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.POKEMON_COLOR, dict(KEY=str(name_or_id))))

    async def get_pokemon_form(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.POKEMON_FORM, dict(KEY=str(name_or_id))))

    async def get_pokemon_habitat(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.POKEMON_HABITAT, dict(KEY=str(name_or_id))))

    async def get_pokemon_shape(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.POKEMON_SHAPE, dict(KEY=str(name_or_id))))

    async def get_pokemon_species(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.POKEMON_SPECIES, dict(KEY=str(name_or_id))))

    async def get_region(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.REGION, dict(KEY=str(name_or_id))))

    async def get_stat(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.STAT, dict(KEY=str(name_or_id))))

    async def get_super_contest_effect(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.SUPER_CONTEST_EFFECT, dict(KEY=str(name_or_id))))

    async def get_type(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.TYPE, dict(KEY=str(name_or_id))))

    async def get_version(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.VERSION, dict(KEY=str(name_or_id))))

    async def get_version_group(self, name_or_id: t.Union[str, int]) -> RESP_TYPE:
        return t.cast(RESP_TYPE, await self.get(PokeApiEndpoint.VERSION_GROUP, dict(KEY=str(name_or_id))))
