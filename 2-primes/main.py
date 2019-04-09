from random import randint
from sys import argv

from rng import xorshift_init, BitLength


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
        256: BitLength.RNG256,
        512: BitLength.RNG512,
        1024: BitLength.RNG1024,
        2048: BitLength.RNG2048,
    }

    try:
        for i, n in zip(range(1), xorshift_init(BITS[bits])):
            charsxor = len(str(n))
            rand = randint(0, 2**bits)
            charsrand = len(str(rand))
            print(
                f'>>> rng.py ({charsxor}):\n'
                f'{n}\n\n'
                f'>>> randint ({charsrand}):\n'
                f'{rand}\n'
                f'{"-"*80}'
            )
    except KeyError:
        print(f'Valid bitlengths: {[*BITS.keys()]}')
