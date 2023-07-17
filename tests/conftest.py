import pytest
import typing as t

from gracy import GracyReplay
from gracy.replays.storages.sqlite import SQLiteReplayStorage

from gpokeapi import PokeApi

TEST_STORAGE: t.Final = SQLiteReplayStorage("tests.sqlite3")


@pytest.fixture
def gracy_replay() -> GracyReplay:
    return GracyReplay("replay", TEST_STORAGE)


@pytest.fixture
def test_client(gracy_replay: GracyReplay) -> PokeApi:
    return PokeApi(cache=gracy_replay)
