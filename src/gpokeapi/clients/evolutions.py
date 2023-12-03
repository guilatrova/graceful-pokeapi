import typing as t
from gracy import GracyNamespace, parsed_response

from gpokeapi.endpoints import PokeApiEndpoint

DICT_OR_NONE = t.Union[t.Dict[str, t.Any], None]


class EvolutionNamespace(GracyNamespace[PokeApiEndpoint]):
    @parsed_response(DICT_OR_NONE)
    async def get_chain(self, id: int):
        return await self.get(PokeApiEndpoint.EVOLUTION_CHAIN, dict(KEY=str(id)))

    @parsed_response(DICT_OR_NONE)
    async def get_trigger(self, id: int):
        return await self.get(PokeApiEndpoint.EVOLUTION_TRIGGER, dict(KEY=str(id)))
