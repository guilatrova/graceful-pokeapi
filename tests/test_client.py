import pytest

from gpokeapi import PokeApi


@pytest.mark.parametrize(
    "pokemon_name, pokemon_id",
    [
        ("bulbasaur", 1),
        ("charmander", 4),
        ("squirtle", 7),
        ("pikachu", 25),
        ("mew", 151),
        ("torchic", 255),
        ("blaziken", 257),
    ],
)
async def test_get_pokemon(test_client: PokeApi, pokemon_name: str, pokemon_id: int):
    result = await test_client.get_pokemon(pokemon_name)

    assert isinstance(result, dict)
    assert result["name"] == pokemon_name
    assert result["id"] == pokemon_id


async def test_get_nonexisting_pokemon(test_client: PokeApi):
    result = await test_client.get_pokemon("FAKE")
    assert result is None
