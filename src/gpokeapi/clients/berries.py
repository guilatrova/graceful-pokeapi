import typing as t

from gracy import GracyNamespace, parsed_response

from gpokeapi.endpoints import PokeApiEndpoint

DICT_OR_NONE = t.Union[t.Dict[str, t.Any], None]


class BerryNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(DICT_OR_NONE)
    async def get_one(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_flavor(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_FLAVOR, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_firmness(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_FIRMNESS, dict(KEY=str(name_or_id)))
