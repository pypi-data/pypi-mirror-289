import pytest

from kluck import Maybe


def test_kmaybe_eq():
    assert (Maybe == True) in [True, False]


def test_kmaybe_str():
    assert str(Maybe) == "Maybe"


def test_kmaybe_repr():
    assert repr(Maybe) == "Maybe"
