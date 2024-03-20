from Model.WriteResponse import *
from Model.ReadResponse import *
from .ILevelCache import *

class NullEffectLevelCache(ILevelCache):
    def set(self, key, value):
        return WriteResponse(0.0)

    def get(self, key):
        return ReadResponse(None, 0.0)

    def get_usages(self):
        return []