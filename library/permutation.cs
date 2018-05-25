using System;
using System.Linq;
using System.Text;
using System.Collections;
using System.Collections.Generic;
 
public class Program {
    static void Swap<t> (ref T a, ref T b) {
        T t = a;
        a = b;
        b = t;
    }
     
    static bool NextPermutation<t> (T[] a) where T : IComparable {
        for (int i = a.Length - 1; i > 0; --i) {
            if (a[i].CompareTo(a[i - 1]) > 0) {
                int t = i;
                for (int j = i + 1; j < a.Length; ++j) {
                    if (a[i - 1].CompareTo(a[j]) < 0 && a[t].CompareTo(a[j]) >= 0) { t = j; }
                }
                Swap(ref a[i - 1], ref a[t]);
                for (int j = 0; j < (a.Length - i) / 2; ++j) {
                    Swap(ref a[a.Length - 1 - j], ref a[i + j]);
                }
                return true;
            }
        }
        return false;
    }
     
    static bool _NextPermutation<T> (T[] a, T[] b, int n) where T : IComparable {
        int p = n;
        bool f = true;
        while (f && p > n - 1) {
            for (int i = a.Length - 1; i > 0; --i) {
                if (a[i].CompareTo(a[i - 1]) > 0) {
                    int t = i;
                    for (int j = i + 1; j < a.Length; ++j) {
                        if (a[i - 1].CompareTo(a[j]) < 0 && a[t].CompareTo(a[j]) >= 0) { t = j; }
                    }
                    Swap(ref a[i - 1], ref a[t]);
                    p = i - 1;
                    for (int j = 0; j < (a.Length - i) / 2; ++j) {
                        Swap(ref a[a.Length - 1 - j], ref a[i + j]);
                    }
                    f = true;
                    break;
                }
                f = false;
            }
        }
        if (f) { 
            for (int i = p; i < n; ++i) {
                b[i] = a[i];
            }
        }
        return f;
    }
     
    static IEnumerable Permutations<T> (T[] array, int n = 0) where T : IComparable {
        n = n < 1 ? array.Length : n;
        T[] a = new T[array.Length];
        Array.Copy(array, 0, a, 0, array.Length);
        T[] b = new T[n];
        Array.Copy(array, 0, b, 0, n);
        yield return b;
        while (_NextPermutation(a, b, n)) {
            yield return b;
        }
    }
     
    static void Main (string[] args) {
        char[] ca = {'A', 'B', 'C' ,'D'};
        foreach (char[] i in Permutations(ca, 2)) {
            Console.WriteLine(string.Join("", i));
        }// AB AC AD BA BC BD CA CB CD DA DB DC
         
        int[] ia = {0, 1, 2};
        foreach (int[] i in Permutations(ia)) {
            Console.WriteLine(string.Join("", i));
        }// 012 021 102 120 201 210
         
        int[] ia2 = {1, 2, 2};
        foreach (int[] i in Permutations(ia2)) {
            Console.WriteLine(string.Join("", i));
        }// 122 212 221
    }
}