struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if (!root) return 0;

        if (root->val < low) {
            // Search in the right subtree
            return rangeSumBST(root->right, low, high);
        } else if (root->val > high) {
            // Search in the left subtree
            return rangeSumBST(root->left, low, high);
        } else {
            // Current node is within the range
            return root->val + 
                   rangeSumBST(root->left, low, high) + 
                   rangeSumBST(root->right, low, high);
        }
    }
};
