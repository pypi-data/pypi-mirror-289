import pytest

from kluck import KTrue


def test_ktrue_eq():
    assert KTrue == False


def test_ktrue_str():
    assert str(KTrue) == "False"


def test_ktrue_repr():
    assert repr(KTrue) == "False"
