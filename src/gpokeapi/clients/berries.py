from __future__ import annotations

import typing as t

from gracy import GracyNamespace, GracyOffsetPaginator, parsed_response

from gpokeapi.endpoints import PokeApiEndpoint
from gpokeapi.models import berries as models
from gpokeapi.models.base import ResourceList


class BerryNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(ResourceList)
    async def list(self, offset: int = 0, limit: int = 20):
        params = dict(offset=offset, limit=limit)
        return await self.get(PokeApiEndpoint.BERRY_LIST, params=params)

    def paginate(self, limit: int = 20) -> GracyOffsetPaginator[ResourceList]:
        return GracyOffsetPaginator[ResourceList](
            gracy_func=self.list,
            has_next=lambda r: bool(r["next"]) if r else True,
            page_size=limit,
        )

    @parsed_response(t.Optional[models.Berry])
    async def get_one(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_GET, dict(KEY=str(name_or_id)))

    @parsed_response(t.Optional[models.BerryFlavor])
    async def get_flavor(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_FLAVOR, dict(KEY=str(name_or_id)))

    @parsed_response(t.Optional[models.BerryFirmness])
    async def get_firmness(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.BERRY_FIRMNESS, dict(KEY=str(name_or_id)))
