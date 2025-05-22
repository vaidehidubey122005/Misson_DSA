#include <iostream>
#include <vector>
using namespace std;

int sansaAndXor(const vector<int>& arr) {
    int n = arr.size();
    
    // If n is even, the result is 0
    if (n % 2 == 0) {
        return 0;
    }

    // If n is odd, XOR all the elements
    int result = 0;
    for (int i = 0; i < n; ++i) {
        result ^= arr[i];
    }
    
    return result;
}
