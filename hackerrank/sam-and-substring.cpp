#include <iostream>
#include <string>
using namespace std;

long long samAndSubstring(const string &s) {
    long long totalSum = 0;
    long long currentSum = 0;
    long long mod = 1000000007;
    long long factor = 1;
    
    // Traverse the string from right to left
    for (int i = s.size() - 1; i >= 0; --i) {
        // Convert char to int
        int digit = s[i] - '0';
        
        // Update the current sum for substrings ending at s[i]
        currentSum = (currentSum + digit * factor) % mod;
        
        // Add current sum to total sum
        totalSum = (totalSum + currentSum) % mod;
        
        // Update the factor for the next iteration
        factor = (factor * 10 + 1) % mod;
    }
    
    return totalSum;
}
