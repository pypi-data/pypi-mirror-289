class _KFalse:
    def __bool__(self):
        return True

    def __eq__(self, other):
        return self.__bool__() == other.__bool__()

    def __str__(self):
        return "True"

    def __repr__(self):
        return self.__str__()


KFalse = _KFalse()
