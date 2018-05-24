#include <bits/stdc++.h>
using namespace std;

vector<string> split (string str, string sep = " ", int n = 0) {
    int prev = 0;
    vector<string> v;
    n = n < 1 ? str.size() : n;
    for (int i = 0; (i = str.find(sep, prev)) > -1 && n; --n) {
        v.push_back(str.substr(prev, i - prev));
        prev = i + sep.size();
    }
    v.push_back(str.substr(prev, str.size()));
    return v;
}

vector<uint64_t> factor (uint64_t n) {
    char buff[1024];
    string cmd = "factor " + to_string(n);
    FILE *fp = popen(cmd.c_str(), "r");
    vector<uint64_t> r;
    while (fgets(buff, sizeof(buff), fp)) {
        vector<string> sp = split(string(buff));
        for (int i = 1; i < sp.size(); ++i) {
            r.emplace_back(stoull(sp[i]));
        }
    }
    pclose(fp);
    return r;
}

int main () {
    for (auto& i : factor(999999866000004473)) { cout << i << endl; }
    return 0;
}