"""This is a Gracy script intedend to generate TEST data, so we can retest without hitting the API"""

import asyncio
import typing as t

from gracy import GracyReplay
from gracy.replays.storages.sqlite import SQLiteReplayStorage

from gpokeapi import PokeApi

TEST_STORAGE: t.Final = SQLiteReplayStorage("tests.sqlite3")

POKEMONS = {
    "bulbasaur",
    "charmander",
    "squirtle",
    "pikachu",
    "mew",
    "torchic",
    "blaziken",
    "FAKE",
}


async def generate():
    record_cache = GracyReplay("record", TEST_STORAGE)
    client = PokeApi(cache=record_cache)

    tasks = [asyncio.create_task(client.get_pokemon(p)) for p in POKEMONS]

    await asyncio.gather(*tasks)

    client.report_status("list")


if __name__ == "__main__":
    asyncio.run(generate())
