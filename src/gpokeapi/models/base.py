from __future__ import annotations

import typing as t


class BasePokemonModel(t.TypedDict):
    id: int
    """The identifier for this resource."""

    name: str
    """The name for this resource."""


class ResourceReference(t.TypedDict):
    name: str
    """The name of the referenced resource."""

    url: str
    """The URL of the referenced resource."""


class ResourceName(t.TypedDict):
    name: str
    """The localized name for an API resource in a specific language."""

    language: t.List[ResourceReference]
    """The language this name is in."""


class FlavorText(t.TypedDict):
    flavor_text: str
    language: ResourceReference


T = t.TypeVar("T")


class ResourceList(t.TypedDict):
    count: int
    """The total number of resources available from this API."""

    next: t.Optional[str]
    """The URL for the next page in the list."""

    previous: t.Optional[str]
    """The URL for the previous page in the list."""

    results: t.List[ResourceReference]
    """A list of named API resources."""
