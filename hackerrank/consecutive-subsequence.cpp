#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

long long countDivisibleSubarrays(const vector<int>& nums, int k) {
    unordered_map<int, long long> modCount;
    modCount[0] = 1;  // base case for subarrays starting from index 0
    long long count = 0;
    long long prefixSum = 0;

    for (int num : nums) {
        prefixSum += num;
        int mod = ((prefixSum % k) + k) % k;  // handle negative mods safely
        count += modCount[mod];
        modCount[mod]++;
    }

    return count;
}
