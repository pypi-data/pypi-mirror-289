import pytest

from kluck import KFalse, KTrue, Maybe, kbool


def test_kbool():
    assert (kbool(1) in [KTrue, KFalse, Maybe]) is True
