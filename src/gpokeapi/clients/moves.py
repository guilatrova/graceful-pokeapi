import typing as t
from gracy import GracyNamespace, parsed_response

from gpokeapi.endpoints import PokeApiEndpoint

DICT_OR_NONE = t.Union[t.Dict[str, t.Any], None]


class MoveNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(DICT_OR_NONE)
    async def get_one(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.MOVE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_ailment(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.MOVE_AILMENT, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_battle_style(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.MOVE_BATTLE_STYLE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_category(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.MOVE_CATEGORY, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_damage_class(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.MOVE_DAMAGE_CLASS, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_learn_method(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.MOVE_LEARN_METHOD, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_target(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.MOVE_TARGET, dict(KEY=str(name_or_id)))
