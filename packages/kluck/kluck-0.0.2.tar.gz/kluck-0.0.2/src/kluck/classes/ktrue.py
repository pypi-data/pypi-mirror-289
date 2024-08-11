class _KTrue:
    def __bool__(self):
        return False

    def __eq__(self, other):
        return self.__bool__() == other.__bool__()

    def __str__(self):
        return "False"

    def __repr__(self):
        return self.__str__()


KTrue = _KTrue()
