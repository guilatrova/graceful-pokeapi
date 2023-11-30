import typing as t


class ResourceReference(t.TypedDict):
    name: str
    url: str


class ResourceName(t.TypedDict):
    name: str
    """The localized name for an API resource in a specific language."""

    language: list[ResourceReference]
    """The language this name is in."""


T = t.TypeVar("T")


class ResourceList(t.TypedDict):
    count: int
    """The total number of resources available from this API."""

    next: str
    """The URL for the next page in the list."""

    previous: str
    """The URL for the previous page in the list."""

    results: list[ResourceReference]
    """A list of named API resources."""
