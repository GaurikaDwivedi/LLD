class Comparable(object):
    @staticmethod
    def _compare(a, b):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

    def _compare_key(self, other):
        return self._compare(self._cmpkey(), other._cmpkey())

    def __lt__(self, other):
        return self._compare_key(other) < 0

    def __le__(self, other):
        return self._compare_key(other) <= 0

    def __eq__(self, other):
        return self._compare_key(other) == 0

    def __ge__(self, other):
        return self._compare_key(other) >= 0

    def __gt__(self, other):
        return self._compare_key(other) > 0

    def __ne__(self, other):
        return self._compare_key(other) != 0

    def _cmpkey(self):
        raise NotImplementedError("'_cmpkey' method must be implemented in the derived class")
