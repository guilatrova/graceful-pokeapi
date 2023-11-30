import typing as t

from gpokeapi.endpoints import PokeApiEndpoint
from gpokeapi.models import berries as models
from gpokeapi.models.base import ResourceList
from gracy import GracyNamespace, parsed_response


class BerryNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(t.List[ResourceList])
    async def list(self, offset: int = 0, limit: int = 20):
        params = dict(offset=offset, limit=limit)
        return await self.get(PokeApiEndpoint.BERRY_LIST, params=params)

    @parsed_response(t.Union[models.Berry, None])
    async def get_one(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_GET, dict(KEY=str(name_or_id)))

    @parsed_response(t.Union[models.BerryFlavor, None])
    async def get_flavor(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_FLAVOR, dict(KEY=str(name_or_id)))

    @parsed_response(t.Union[models.BerryFirmness, None])
    async def get_firmness(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_FIRMNESS, dict(KEY=str(name_or_id)))
