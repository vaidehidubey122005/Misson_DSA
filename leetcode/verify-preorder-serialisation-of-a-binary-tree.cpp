#include <iostream>
#include <sstream>
using namespace std;

class Solution {
public:
    bool isValidSerialization(string preorder) {
        int slots = 1;  // Root node creates one initial slot
        stringstream ss(preorder);
        string token;

        while (getline(ss, token, ',')) {
            slots--;  // Consume one slot

            if (slots < 0) return false;  // No slot available to place node

            if (token != "#") {
                slots += 2;  // Non-null node creates two more slots
            }
        }

        return slots == 0;
    }
};
