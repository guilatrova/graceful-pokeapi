from __future__ import annotations

import httpx
import logging
import typing as t
from datetime import datetime
from gracy import GracyReplayStorage
from gracy.exceptions import GracyReplayRequestNotFound

CACHE_KEY = t.Tuple[str, str, t.Union[bytes, None]]

logger = logging.getLogger("gpokeapi")


class InMemoryStorage(GracyReplayStorage):
    def prepare(self) -> None:
        self._cache: t.Dict[CACHE_KEY, httpx.Response] = {}

    def _build_key(self, request: httpx.Request) -> CACHE_KEY:
        return (str(request.method), str(request.url), request.content or None)

    async def record(self, response: httpx.Response) -> None:
        key = self._build_key(response.request)
        self._cache[key] = response

    async def find_replay(self, request: httpx.Request, discard_before: t.Union[datetime, None]) -> t.Any | None:
        pass

    async def _load(self, request: httpx.Request, discard_before: t.Union[datetime, None] = None) -> httpx.Response:
        key = self._build_key(request)
        response = self._cache.get(key)

        if response is None:
            raise GracyReplayRequestNotFound(request)

        if discard_before:
            logger.warning("discard_before was passed to InMemoryStorage, it will be ignored")

        return response
