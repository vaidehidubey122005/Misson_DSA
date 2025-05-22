#include <iostream>
#include <vector>
#include <deque>
#include <climits>
using namespace std;

int shortestSubarray(vector<int>& nums, int k) {
    int n = nums.size();
    vector<long long> prefix(n + 1, 0);
    
    for (int i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    int minLen = INT_MAX;
    deque<int> dq;

    for (int i = 0; i <= n; ++i) {
        while (!dq.empty() && prefix[i] - prefix[dq.front()] >= k) {
            minLen = min(minLen, i - dq.front());
            dq.pop_front();
      }
        while (!dq.empty() && prefix[i] <= prefix[dq.back()]) {
            dq.pop_back();
        }
        dq.push_back(i);
    }
    return minLen == INT_MAX ? -1 : minLen;
}
