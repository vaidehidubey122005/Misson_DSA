class Solution {
public:
    void allPaths(TreeNode* root, string path, vector<string> &ans) {
        if(root->left == NULL && root->right == NULL) {
            ans.push_back(path);
            return;
        }
        if(root->left) {
            allPaths(root->left, path+"->"+to_string(root->left->val), ans);
        }
        if(root->right) {
            allPaths(root->right, path+"->"+to_string(root->right->val), ans);
        }
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        string path = to_string(root->val);

        allPaths(root, path, ans);
        return ans;
    }
};
