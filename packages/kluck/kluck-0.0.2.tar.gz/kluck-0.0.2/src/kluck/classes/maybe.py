from random import choice


class _KMaybe:
    def __bool__(self):
        return choice((True, False))

    def __eq__(self, other):
        return self.__bool__() == other.__bool__()

    def __str__(self):
        return "Maybe"

    def __repr__(self):
        return self.__str__()


Maybe = _KMaybe()
