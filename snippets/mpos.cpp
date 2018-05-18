#include <bits/stdc++.h>
using namespace std;

struct mpos {
public:
    int x;
    int y;
    mpos () { this->x = 0; this->y = 0; }
    mpos (int x, int y) {
        this->x = x;
        this->y = y;
    }
    mpos operator + (const mpos &t) { return mpos(this->x + t.x, this->y + t.y); }
    mpos operator - (const mpos &t) { return mpos(this->x - t.x, this->y - t.y); }
    bool operator == (const mpos &t) const { return this->x == t.x && this->y == t.y; }
};

namespace std {
    template <> class hash<mpos> {
    public:
        size_t operator () (const mpos& t) const{ return hash<int>()(t.x<<16) | hash<int>()(t.y); }
    };
}

ostream& operator << (ostream& os, const mpos& mp) {
    os << "(" + to_string(mp.x) + ", " + to_string(mp.y) + ")";
    return os;
};

int main () {
    cin.tie(0);
    ios::sync_with_stdio(false);
    
    unordered_map<mpos, int> v;
    v[mpos(1, 1)] = 5;
    
    return 0;
}