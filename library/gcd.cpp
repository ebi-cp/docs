#include <unordered_set>
#include <vector>
#include <iostream>
using namespace std;

uint64_t gcd (uint64_t a, uint64_t b) {
    if (a < b) { swap(a, b); }
    while (b > 0) {
        a = a % b;
        swap(a, b);
    }
    return a;
}

uint64_t lcm (uint64_t a, uint64_t b) {
    return a / gcd(a, b) * b;
}


int main () {
    
    return 0;
}