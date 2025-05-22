#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};
struct compare {
    bool operator()(ListNode* a, ListNode* b) {
        return a->val > b->val; // min-heap
    }
};
ListNode* mergeKLists(vector<ListNode*>& lists) {
    priority_queue<ListNode*, vector<ListNode*>, compare> minHeap;
    for (auto l : lists) {
        if (l)
            minHeap.push(l);
    }
    ListNode* dummy = new ListNode(0);
    ListNode* tail = dummy;
    while (!minHeap.empty()) {
        ListNode* smallest = minHeap.top();
        minHeap.pop();
        tail->next = smallest;
        tail = tail->next;
        if (smallest->next) {
            minHeap.push(smallest->next);
        }
    }
    return dummy->next;
}
