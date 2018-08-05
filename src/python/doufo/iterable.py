from typing import Iterable, Callable, Optional, TypeVar
from .control import Functor
from .monoid import Monoid
from .function import identity
import itertools
from .on_collections import take_
from functools import partial

__all__ = ['PureIterable', 'IterableElemMap', 'IterableIterMap', 'Count']

T = TypeVar('T')


class PureIterable(Iterable[T], Functor[Iterable[T]], Monoid[Iterable[T]]):
    """
    Only iterable, iterator is not PureIterable
    """


class IterableElemMap(PureIterable[T]):
    """
    Iterable Functor, fmap functon on elements of iterable.
    Useful for chaning data.
    """
    def __init__(self, source: PureIterable[T], opeartion=Optional[Callable]):
        self.source = source
        if opeartion is None:
            opeartion = identity
        self.opeartion = opeartion

    def fmap(self, f):
        return IterableElemMap(self, f)

    def __iter__(self):
        return (self.opeartion(x) for x in self.source)

    def unbox(self):
        return iter(self)

    @classmethod
    def empty(cls):
        return IterableElemMap(tuple())

    def extend(self, xs: PureIterable[T]):
        return IterableElemMap(IterableIterMap(self).extend(xs))

    def filter(self, f):
        return IterableElemMap(IterableIterMap(self).filter(f))

class IterableIterMap(PureIterable):
    """
    Iterable Functor, fmap on iterable itself, useful for concatnating, 
    filtering, etc.
    """
    def __init__(self, source: PureIterable, opeartion=Optional[Callable]):
        self.source = source
        if opeartion is None:
            opeartion = identity
        self.opeartion = opeartion

    def fmap(self, f):
        return ItertoolsIterable(self, f)

    def __iter__(self):
        return (x for x in self.opeartion(self.source))

    def unbox(self):
        return iter(self)

    def extend(self, xs: PureIterable[T]):
        return self.fmap(lambda s: itertools.chain(s, xs))

    def filter(self, f):
        return self.fmap(partial(filter, f))

    @classmethod
    def empty(cls):
        return IterableIterMap(tuple())


class Count(PureIterable):
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step

    def __iter__(self):
        return itertools.count(self.start, self.step)


@take_.register(Iterable)
def _(xs: Iterable, n: int)->Iterable:
    return IterableIterMap(xs, itertools.islice(0, n))
