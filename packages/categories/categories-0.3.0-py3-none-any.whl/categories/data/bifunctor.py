from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.data.either import Either, Left, Right
from categories.type import Lambda, hkt, typeclass

__all__ = (
    'Bifunctor',
    'BifunctorEither',
    'BifunctorTuple',
)


a = TypeVar('a')

b = TypeVar('b')

c = TypeVar('c')

d = TypeVar('d')

p = TypeVar('p')


@dataclass(frozen=True)
class Bifunctor(typeclass[p]):
    def bimap(self, f : Lambda[a, b], g : Lambda[c, d], x : hkt[p, a, c], /) -> hkt[p, b, d]:
        return self.first(f, self.second(g, x))

    def first(self, f : Lambda[a, b], x : hkt[p, a, c], /) -> hkt[p, b, c]:
        return self.bimap(f, lambda x, /: x, x)

    def second(self, g : Lambda[b, c], x : hkt[p, a, b], /) -> hkt[p, a, c]:
        return self.bimap(lambda x, /: x, g, x)


@dataclass(frozen=True)
class BifunctorEither(Bifunctor[Either]):
    def bimap(self, f : Lambda[a, b], g : Lambda[c, d], e : Either[a, c], /) -> Either[b, d]:
        match e:
            case Left(x):
                return Left(f(x))
            case Right(y):
                return Right(g(y))
        assert None


@dataclass(frozen=True)
class BifunctorTuple(Bifunctor[tuple]):
    def bimap(self, f : Lambda[a, b], g : Lambda[c, d], z : tuple[a, c], /) -> tuple[b, d]:
        match z:
            case (x, y):
                return (f(x), g(y))
        assert None
