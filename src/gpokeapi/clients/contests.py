import typing as t

from gpokeapi.endpoints import PokeApiEndpoint
from gpokeapi.models import contests as models
from gracy import GracyNamespace, parsed_response


class ContestNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(t.Optional[models.ContestType])
    async def get_type(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.CONTEST_TYPE, dict(KEY=str(name_or_id)))

    @parsed_response(t.Optional[models.ContestEffect])
    async def get_effect(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.CONTEST_EFFECT, dict(KEY=str(name_or_id)))

    @parsed_response(t.Optional[models.SuperContestEffect])
    async def get_super_effect(self, name_or_id: t.Union[str, int]):
        return await self.get(PokeApiEndpoint.CONTEST_SUPER_EFFECT, dict(KEY=str(name_or_id)))
