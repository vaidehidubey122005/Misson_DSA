#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class RunningMedian {
private:
    priority_queue<int> maxHeap; // Max-heap for the smaller half (largest element on top)
    priority_queue<int, vector<int>, greater<int>> minHeap; // Min-heap for the larger half (smallest element on top)

public:
    void addNumber(int num) {
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);  // Add to max-heap (smaller half)
        } else {
            minHeap.push(num);  // Add to min-heap (larger half)
        }

        // Balance the heaps to ensure size difference is at most 1
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double getMedian() {
        if (maxHeap.size() > minHeap.size()) {
            return maxHeap.top();  // Odd size, median is the top of max-heap
        } else {
            return (maxHeap.top() + minHeap.top()) / 2.0;  // Even size, median is the average of the tops
        }
    }
};

int main() {
    RunningMedian rm;
    vector<int> nums = {1, 5, 2, 8, 3, 7}; // Example input

    for (int num : nums) {
        rm.addNumber(num);
        cout << "Current Median: " << rm.getMedian() << endl;
    }

    return 0;
}
