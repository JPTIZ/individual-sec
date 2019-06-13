import datetime
from functools import partial
from random import randint
from textwrap import dedent
from sys import argv

from rng import BitLength, RNG, xorshift


ALGORITHMS = {
    'xorshift': partial(xorshift, a=13, b=7, c=17),
}

BITS = {
    32: BitLength.RNG32,
    64: BitLength.RNG64,
    128: BitLength.RNG128,
    256: BitLength.RNG256,
    512: BitLength.RNG512,
    1024: BitLength.RNG1024,
    2048: BitLength.RNG2048,
    4096: BitLength.RNG2048,
}


def now():
    return datetime.datetime.now()


def into_milliseconds(delta: datetime.timedelta):
    return delta.seconds * 1000 + delta.microseconds / 1000


if __name__ == '__main__':
    try:
        algorithm = argv[1]
        bits = int(argv[2])
    except IndexError:
        print(dedent(
            f'''
            Usage: {argv[0]} <algorithm> <output bit length> [executions]'

            Available algorithms:
                {', '.join(ALGORITHMS)}

            Available bit lengths:
                {', '.join(str(k) for k in BITS)}
            '''
        ).strip())
        exit(1)

    try:
        executions = int(argv[3])
    except IndexError:
        executions = 10

    try:
        seed = 88172645463325252
        for i in range(bits):
            seed += 2 ** bits

        avg = 0
        rng = iter(RNG(
            ALGORITHMS[algorithm],
            seed=seed,
            limit = 2 ** bits
        ))
        for i in range(executions):
            start = now()
            n = next(rng)
            avg += into_milliseconds(now() - start) / executions
        print(f'Average of {executions} executions of {algorithm} ({bits} bits): {avg}')
    except KeyError:
        print(f'Valid bitlengths: {[*BITS.keys()]}')
