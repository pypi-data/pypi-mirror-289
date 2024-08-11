import pytest

from kluck import KFalse


def test_kfalse_eq():
    assert KFalse == True


def test_kfalse_str():
    assert str(KFalse) == "True"


def test_kfalse_repr():
    assert repr(KFalse) == "True"
