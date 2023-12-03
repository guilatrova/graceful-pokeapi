from __future__ import annotations

from gracy import GracyNamespace

from gpokeapi.clients.api import PokeApi


def test_namespaces_are_created(test_client: PokeApi):
    assert isinstance(test_client.pokemon, GracyNamespace)
    assert isinstance(test_client.berry, GracyNamespace)
    assert isinstance(test_client.item, GracyNamespace)
    assert isinstance(test_client.encounter, GracyNamespace)
    assert isinstance(test_client.move, GracyNamespace)
    assert isinstance(test_client.evolution, GracyNamespace)
    assert isinstance(test_client.contest, GracyNamespace)
