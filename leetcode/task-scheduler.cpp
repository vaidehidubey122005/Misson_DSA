#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int leastInterval(vector<char>& tasks, int n) {
    vector<int> freq(26, 0);
    for (char task : tasks) {
        freq[task - 'A']++;
    }

    sort(freq.begin(), freq.end());

    int f_max = freq[25];
    int count = 1;

    for (int i = 24; i >= 0; --i) {
        if (freq[i] != f_max) break;
        count++;
    }
    int min_time = (f_max - 1) * (n + 1) + count;
    return max((int)tasks.size(), min_time);
}
