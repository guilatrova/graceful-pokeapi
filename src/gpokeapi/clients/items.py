import typing as t
from gracy import GracyNamespace, parsed_response

from gpokeapi.endpoints import PokeApiEndpoint

DICT_OR_NONE = t.Union[t.Dict[str, t.Any], None]


class ItemNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(DICT_OR_NONE)
    async def get_one(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.ITEM, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_attribute(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.ITEM_ATTRIBUTE, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_category(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.ITEM_CATEGORY, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_fling_effect(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.ITEM_FLING_EFFECT, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_pocket(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.ITEM_POCKET, dict(KEY=str(name_or_id)))
