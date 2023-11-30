import typing as t

from gpokeapi.endpoints import PokeApiEndpoint
from gracy import GracyNamespace, parsed_response

DICT_OR_NONE = t.Union[t.Dict[str, t.Any], None]


class BerryNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(t.List[DICT_OR_NONE])
    async def list(self, offset: int = 0, limit: int = 20):
        params = dict(offset=offset, limit=limit)
        return await self.get(PokeApiEndpoint.BERRY_LIST, params=params)

    @parsed_response(DICT_OR_NONE)
    async def get_one(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_GET, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_flavor(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_FLAVOR, dict(KEY=str(name_or_id)))

    @parsed_response(DICT_OR_NONE)
    async def get_firmness(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_FIRMNESS, dict(KEY=str(name_or_id)))
