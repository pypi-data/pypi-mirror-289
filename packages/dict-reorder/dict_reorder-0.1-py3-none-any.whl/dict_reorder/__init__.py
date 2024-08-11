"""A tool used to easily reorder dictionary indexes."""

__version__ = "0.1"
__author__ = "xyzpw"
__description__ = "A tool used to easily reorder dictionary indexes."
__license__ = "MIT"

__all__ = [
    "DictReorder",
    "changeKeyIndex",
    "swapKeys",
]

class DictReorder:
    """Contains values which can be outputted as a dictionary in a proper order."""
    def __init__(self):
        pass
    def addKey(self, name: str, value, index: int):
        """Adds key to attribute along with index.

        :param name: name of the key
        :param value: value of the key
        :param index: dictionary index of the key"""
        setattr(self, name, (value, index))
    def removeKey(self, name: str):
        """Removes key attribute.

        :param name: name of the key
        """
        delattr(self, name)
    def getKeyIndex(self, key: str) -> int:
        """Returns index of the specified key."""
        return getattr(self, key)[1]
    def getIndexKey(self, index: int) -> str:
        """Returns key of the specified index."""
        return [i for i in list(vars(self)) if getattr(self, i)[1] == index][0]
    def getDictionary(self) -> dict:
        """Returns the dictionary in proper order."""
        workingDictionary = {}
        indexes = [vars(self)[i][1] for i in list(vars(self))]
        if sorted(indexes) != list(range(len(indexes))):
            raise IndexError("indexes are out of range")
        for i in sorted(indexes):
            workingDictionary[self.getIndexKey(i)] = getattr(self, self.getIndexKey(i))[0]
        return workingDictionary

def changeKeyIndex(dictionary: dict, key: str, newIndex: int) -> dict:
    """Changes the index of a key in a dictionary.

    :param dictionary: the dictionary to edit
    :param key: the key which will be moved to a new index
    :param newIndex: the new index for the specified key
    """
    currentIndex = list(dictionary).index(key)
    keyAtNewIndex = list(dictionary)[newIndex]
    keys = list(dictionary)
    keys[newIndex] = key
    keys[currentIndex] = keyAtNewIndex
    return {k: dictionary[k] for k in keys}

def swapKeys(dictionary: dict, key: str, targetKey: str) -> dict:
    """Swaps the keys indexes in a dictionary.

    :param dictionary: the dictionary to edit
    :param key: the key to be swapped
    :param targetKey: the key with which `key` will be swapped
    """
    keys = list(dictionary)
    currentIndex = keys.index(key)
    targetIndex = keys.index(targetKey)
    keys[targetIndex] = key
    keys[currentIndex] = targetKey
    newDictionary = {k: dictionary[k] for k in keys}
    return newDictionary
