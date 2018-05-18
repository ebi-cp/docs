#include <unordered_set>
#include <vector>
#include <iostream>
using namespace std;

uint64_t mgcd (uint64_t a, uint64_t b) {
    uint64_t t;
    if (a < b) {
        t = a;
        a = b;
        b = t;
    }
    while (b > 0) {
        t = a % b;
        a = b;
        b = t;
    }
    return a;
}

uint64_t mlcm (uint64_t a, uint64_t b) {
    return a / gcd(a, b) * b;
}


int main () {
    
    return 0;
}