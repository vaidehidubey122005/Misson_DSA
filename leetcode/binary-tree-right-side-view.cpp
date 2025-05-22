#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (!root) return result;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int levelSize = q.size();
            TreeNode* current = nullptr;

            for (int i = 0; i < levelSize; ++i) {
                current = q.front(); q.pop();

                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }

            // current now holds the last node in this level
            result.push_back(current->val);
        }

        return result;
    }
};
