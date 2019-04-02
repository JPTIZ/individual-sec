#include <iostream>
#include "bigint/src/bigint.h"

int main() {
    auto n = Dodecahedron::Bigint{1};
    
    for (auto i = 0; i < 100; ++i) {
        n *= i + 1;
    }

    std::cout << "Factorial of 100 is " << n << "\n";
}