from functools import reduce
from datetime import datetime
import operator

if __name__ == '__main__':
    start = datetime.now()
    x = reduce(operator.mul, (i + 1 for i in range(100)), 1)
    end = datetime.now()

    ellapsed = end - start

    print(f'Factorial of 100 is {x}')
    print(f'({ellapsed.microseconds / 1000}ms)')
