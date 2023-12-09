<p align="center">
    <img width="200px" src="./img/logo.svg">
</p>

<h2 align="center">Graceful PokeApi</h2>

<p align="center">
  <!-- CI --><a href="https://github.com/guilatrova/graceful-pokeapi/actions"><img alt="Actions Status" src="https://github.com/guilatrova/graceful-pokeapi/workflows/CI/badge.svg"></a>
  <!-- PyPI --><a href="https://pypi.org/project/graceful_pokeapi/"><img alt="PyPI" src="https://img.shields.io/pypi/v/graceful_pokeapi"/></a>
  <!-- Supported Python versions --><img src="https://badgen.net/pypi/python/graceful_pokeapi" />
  <!-- Alternative Python versioning: <img alt="python version" src="https://img.shields.io/badge/python-3.9%20%7C%203.10-blue"> -->
  <!-- LICENSE --><a href="https://github.com/guilatrova/graceful-pokeapi/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/guilatrova/graceful_pokeapi"/></a>
  <!-- PyPI downloads --><a href="https://pepy.tech/project/graceful_pokeapi/"><img alt="Downloads" src="https://static.pepy.tech/personalized-badge/graceful_pokeapi?period=total&units=international_system&left_color=grey&right_color=blue&left_text=%F0%9F%A6%96%20Downloads"/></a>
  <!-- Formatting --><a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"/></a>
   <!-- Tryceratops --><a href="https://github.com/guilatrova/tryceratops"><img alt="try/except style: tryceratops" src="https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black" /></a>
  <!-- Follow handle --><a href="https://twitter.com/intent/user?screen_name=guilatrova"><img alt="Follow guilatrova" src="https://img.shields.io/twitter/follow/guilatrova?style=social"/></a>
</p>

[PokeAPI](https://pokeapi.co/) client powered by [Gracy](https://github.com/guilatrova/gracy).

---

## Get Started

```
pip install graceful_pokeapi
```

or

```
poetry add graceful_pokeapi
```

### Usage

```py
from gpokeapi import PokeApi

client = PokeApi()

async def main():
  pokemon = await client.get_pokemon("pikachu")
  if pokemon:
    print(f"{pokemon['name']} is no {pokemon['id']}")

  pokemon = await client.get_pokemon("nonexisting")
  print(pokemon)  # outputs NONE
```

## Capabilities Comparison

| API                  | [Pokebase](https://github.com/PokeAPI/pokebase) | [Pokepy](https://github.com/PokeAPI/pokepy) | [aiopokeapi](https://github.com/beastmatser/aiopokeapi) | Graceful PokeAPI                         |
| -------------------- | ----------------------------------------------- | ------------------------------------------- | ------------------------------------------------------- | ---------------------------------------- |
| Async                | ❌                                               | ❌                                           | ✅                                                       | ✅                                        |
| Type hints           | ❌                                               | ❌                                           | ✅ Data Class                                            | ✅ TypedDict                              |
| Caching              | ✅ File                                          | ✅ File                                      | ✅ Memory                                                | ✅ SQLite, Memory, or custom (extensible) |
| Resource Pagination  | ✅                                               | ❓                                           | ❌                                                       | ✅                                        |
| Customizable         | ❌                                               | ❌                                           | ❌                                                       | ✅                                        |
| Interactive Sessions | ❌                                               | ❌                                           | ❌                                                       | 🔜                                        |

## Customization

Since PokeAPI uses [Gracy](https://github.com/guilatrova/gracy) everything is customizable.

### Cache Types

This API Client caches the requests by default through [Gracy Replays](https://github.com/guilatrova/gracy#replay-requests).

You can choose between `memory`, `sqlite` or your own storage.

```py
client = PokeApi(cache="memory") # default
client = PokeApi(cache="sqlite")
client = PokeApi(cache=custom_gracy_replay) # Extend with your own
```

### Parsers

... todo

### More

You can implement throttling, logging, retry logic and anything else by extending the class and setting your own settings.

```py
from gracy import GracyConfig


class ResourceNotFound(Exception):
  pass


class MyCustomPokeApi(PokeApi):
  class Config(PokeApi.Config):
    SETTINGS = GracyConfig(
            parser={
                HTTPStatus.OK: lambda resp: resp.json(),
                HTTPStatus.NOT_FOUND: ResourceNotFound,
            },
            strict_status_code=HTTPStatus.OK,
            log_errors=LogEvent(LogLevel.CRITICAL),
            log_request=LogEvent(LogLevel.INFO),
        )
```

You can find all available options on [Gracy's documentation](https://github.com/guilatrova/gracy).
