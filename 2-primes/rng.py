'''Module for Random Number Generation functions.'''
from dataclasses import dataclass
from functools import partial
from enum import auto, Enum
from typing import Callable


@dataclass
class RNG:
    function: Callable[[int], int]
    seed: int = 88172645463325252
    limit: int = 2 ** 32

    def __iter__(self):
        return self

    def __next__(self):
        self.seed = self.function(seed=self.seed) % (self.limit)
        return self.seed


def xorshift(
        seed: int = RNG.seed,
        a: int = 13,
        b: int = 7,
        c: int = 17
) -> int:
    seed ^= seed << a
    seed ^= seed >> b
    seed ^= seed << c
    return seed


class BitLength(Enum):
    RNG32 = [32, 13, 17, 5]
    RNG64 = [64, 13, 7, 17]
    RNG128 = [128, 19, 11, 8]
    # TODO: RNG256 = auto()
    # TODO: RNG512 = auto()
    # TODO: RNG1024 = auto()
    # TODO: RNG2048 = auto()


def xorshift_iter(bits: BitLength = BitLength.RNG64, seed=RNG.seed):
    bits, a, b, c = bits.value
    return RNG(function=partial(xorshift, a=a, b=b, c=c), limit=2 ** bits - 1)
