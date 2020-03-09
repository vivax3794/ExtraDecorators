import copy

from typing import Callable



class _president_values_cls:
    """
    Class returned for the presdident_values decorator
    """

    def __init__(self, function: Callable, **kwargs) -> None:
        self._function = function
        self._values = kwargs
        self._starter_values = copy.deepcopy(kwargs)

    def __call__(self, *args, **kwargs):
        """the "inner" part of the decorator"""
        return function(self, *args, **kwargs)

    def __getattr__(self, attr: str) -> any:
        """return an item from self._values"""
        if attr in self._values.keys():
            return self._values[attr]

        else:
            raise AttributeError(f'atterbute "{attr} not part of _president_values for function {self._function}"')

    def __setattr__(self, attr: str, value: any) -> None:
        """sets a value of self._values"""
        self._values[attr] = value

    def __getitem__(self, key: str) -> None:
        """Gate way to self._values.__getitem__"""
        return self._values[key]

    def __setitem__(self, key: str, value: any) -> None:
        """Gate way to self._values.__setitem__"""
        return self._values[key] = value

    @classmethod
    def new_copy(cls, *, keep_values=True):
        """
        return copy of this class, with the current values or
        with the values passed at the start.
        """
        if keep_values:
            values = copy.deepcopy(self._values)
        else:
            values = copy.deepcopy(self._starter_values)

        return cls(self._function, values)

def president_values(**values):
    """
    usses the function as the first argument for _president_values_cls, and the arguemnts passed to the decorator as the second one.
    this is syntax sugar for:
    ```
    def test():
        test.count += 1
    test.count = 0
    ```
    instead now you can:
    ```
    @president_values(count=0)
    def test(pres):
        pres.count += 1
    ```
    it also supplies other funconnality, see _president_values_cls.
    """

