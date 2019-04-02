from functools import reduce
import operator

if __name__ == '__main__':
    x = reduce(operator.mul, (i + 1 for i in range(100)), 1)

    print(f'Factorial of 100 is {x}')