#include <iostream>
using namespace std;

class Solution {
public:
    string smallestNumber(int s, int d) {
        // If sum of digits 's' is more than the maximum possible sum with 'd' digits, return -1
        if (s > 9 * d) {
            return "-1";
        }
        
        // Array to store the digits of the result
        int digits[d];
        
        // Initialize all digits as 0
        for (int i = 0; i < d; i++) {
            digits[i] = 0;
        }
        
        // Decrease sum by 1 to handle the leading zero case
        s -= 1;
        
        // Fill the digits array from the least significant to the most significant digit
        for (int i = d - 1; i > 0; i--) {
            if (s > 9) {
                digits[i] = 9;
                s -= 9;
            } else {
                digits[i] = s;
                s = 0;
            }
        }
        
        // Set the most significant digit
        digits[0] = s + 1;
        
        // Convert the digits array to a string
        string result;
        for (int i = 0; i < d; i++) {
            result += to_string(digits[i]);
        }
        
        return result;
    }
};

int main() {


    int s, d;
    cout << "Enter the sum of digits (s): ";
    cin >> s;
    cout << "Enter the number of digits (d): ";
    cin >> d;

    Solution ob;
    string result = ob.smallestNumber(s, d);
    cout << "Smallest number with sum " << s << " and " << d << " digits: " << result << endl;

    return 0;
}
