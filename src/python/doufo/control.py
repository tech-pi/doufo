"""
Functor is base class for the generic functors.
A composite function can be obtain by the fmap method.
Usually the PureFunction class is used to implement this rather than the basic functor class.

Monad: to be added
"""

from typing import Generic, TypeVar, Callable
from abc import abstractmethod, ABCMeta

A = TypeVar('A')
B = TypeVar('B')

__all__ = ['Functor', 'Monad']


class Functor(Generic[A], metaclass=ABCMeta):
    """
    a functor is
    """
    @abstractmethod
    def fmap(self, f: Callable[[A], B]) -> 'Functor[B]':
        pass

    @abstractmethod
    def unbox(self) -> A:
        pass


class Monad(Functor[A]):
    """
    """

    def __rshift__(self, f: Callable[[A], 'Monad[B]']) -> 'Monad[B]':
        """ Alias to bind """
        return self.bind(f)

    @abstractmethod
    def fmap(self, f: Callable[[A], B]) -> 'Monad[B]':
        pass

    @abstractmethod
    def bind(self, f: Callable[[A], 'Monad[B]']) -> 'Monad[B]':
        pass
