#include <iostream>
#include <cmath>
using namespace std;

// Function to calculate sum of digits of a number
int sum_of_digits(int num) {
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

// Function to find the smallest multiple of n whose sum of digits equals n
int special_multiple(int n) {
    int num = n;
    while (true) {
        if (sum_of_digits(num) == n) {
            return num;
        }
        num += n;  // Try next multiple of n
    }
}

int main() {
    int n;
    cout << "Enter the number n: ";
    cin >> n;
    
    cout << "The smallest special multiple of " << n << " is: " << special_multiple(n) << endl;
    
    return 0;
}
