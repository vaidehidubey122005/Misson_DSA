#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int nonDivisibleSubset(int k, vector<int>& S) {
    vector<int> remainder_count(k, 0);
    
    // Count occurrences of each remainder when divided by k
    for (int num : S) {
        remainder_count[num % k]++;
    }

    int subset_size = 0;

    // Handle remainder 0 separately, can only include at most one element
    if (remainder_count[0] > 0) {
        subset_size++;
    }

    // For each remainder from 1 to k/2, select the larger of the two complementary groups
    for (int i = 1; i <= k / 2; i++) {
        if (i != k - i) {
            subset_size += max(remainder_count[i], remainder_count[k - i]);
        }
    }

    // If k is even, handle the middle remainder case
    if (k % 2 == 0) {
        subset_size += min(1, remainder_count[k / 2]);
    }

    return subset_size;
}
