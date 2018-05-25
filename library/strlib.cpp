#include <bits/stdc++.h>
using namespace std;

namespace strlib {
    // 置き換え
    string replace (string str, string old_s, string new_s, int n = 0) {
        n = n < 1 ? str.size() : n;
        for (int i; (i = str.find(old_s)) > -1 && n; --n) { str.replace(i, old_s.size(), new_s); }
        return str;
    }

    // カウント
    int count (string str, string t) {
        int cnt = 0;
        for (int i = 0; (i = str.find(t, i)) > -1; i += t.size()) { ++cnt; }
        return cnt;
    }

    // 分割
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
    
    vector<string> split (string str, char sep = ' ', int n = 0) {
        string s = {sep};
        return split(str, s, n);
    }

    vector<string> rsplit (string str, string sep = " ", int n = 0) {
        int prev = str.size() - 1;
        vector<string> v;
        n = n < 1 ? str.size() : n;
        for (int i = 0; (i = str.rfind(sep, prev)) > -1 && n; --n) {
            v.insert(v.begin(), str.substr(i + sep.size(), prev - i + sep.size() - 1));
            prev = i - 1;
        }
        v.insert(v.begin(), str.substr(0, prev + 1));
        return v;
    }

    vector<string> rsplit (string str, char sep = ' ', int n = 0) {
        string s = {sep};
        return rsplit(str, s, n);
    }

    // スライス
    string slice (string str, int a, int b) {
        int s = a < 0 ? str.size() + a : a;
        int e = b < 0 ? str.size() + b : b;
        e = b == 0 ? str.size() : e;
        return str.substr(s, (s > e ? s : e) - s);
    }
}

int main () {
    string s = "12345678";
    
    // string {"12", "45678"}
    for (auto& i : strlib::split(s, "3")) { std::cout << i << std::endl; }
    
    cout << strlib::slice(s, 1, 3) << endl;// "23"
    cout << strlib::slice(s, 0, 0) << endl;// "12345678"
    cout << strlib::slice(s, -2, 0) << endl;// "78"
    cout << strlib::slice(s, 3, 3) << endl;// ""
    return 0;
}