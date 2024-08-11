from random import choice
from typing import Union

from kluck import KFalse, KTrue, Maybe
from kluck.classes.kfalse import _KFalse
from kluck.classes.ktrue import _KTrue
from kluck.classes.maybe import _KMaybe


def kbool(value: object) -> Union[_KTrue, _KFalse, _KMaybe]:
    return choice((KFalse, KTrue, Maybe))
