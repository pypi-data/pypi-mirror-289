import pytest

from kluck import Maybe


def test_kmaybe_eq():
    assert ((Maybe == True) or (Maybe == False)) is True


def test_kmaybe_str():
    assert str(Maybe) == "Maybe"


def test_kmaybe_repr():
    assert repr(Maybe) == "Maybe"
