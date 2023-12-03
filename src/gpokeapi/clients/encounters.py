import typing as t
from gracy import GracyNamespace, parsed_response

from gpokeapi.endpoints import PokeApiEndpoint

DICT_OR_NONE = t.Union[t.Dict[str, t.Any], None]


class EncountersNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(DICT_OR_NONE)
    async def get_condition(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.ENCOUNTER_CONDITION, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_condition_value(self, name_or_id: t.Union[str, int]):
        return t.cast(
            DICT_OR_NONE, await self.get(PokeApiEndpoint.ENCOUNTER_CONDITION_VALUE, dict(KEY=str(name_or_id)))
        )

    @parsed_response(DICT_OR_NONE)
    async def get_method(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.ENCOUNTER_METHOD, dict(KEY=str(name_or_id)))
