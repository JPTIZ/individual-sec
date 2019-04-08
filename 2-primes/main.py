from random import randint
from sys import argv

from rng import xorshift_iter, BitLength


if __name__ == '__main__':
    try:
        bits = int(argv[1])
    except IndexError:
        print(f'Usage: {argv[0]} <output bit length>')
        exit(1)

    BITS = {
        32: BitLength.RNG32,
        64: BitLength.RNG64,
        128: BitLength.RNG128,
    }

    try:
        for i, n in zip(range(20), xorshift_iter(BITS[bits])):
            print(f'{i:2}: {n:>64} vs {randint(0, 2**bits):<64}')
    except KeyError:
        print(f'Valid bitlengths: {[*BITS.keys()]}')
