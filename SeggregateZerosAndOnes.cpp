#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    void segregate0and1(vector<int> &arr) {
        int count = 0;

        // Count the number of 0s in the array
        for(int i = 0; i < arr.size(); i++) {
            if(arr[i] == 0) {
                count++;
            }
        }

        // Place the 0s at the beginning
        for(int i = 0; i < count; i++) {
            arr[i] = 0;
        }

        // Place the 1s after the 0s
        for(int i = count; i < arr.size(); i++) {
            arr[i] = 1;
        }
    }
};

int main() {
    Solution solution;
    vector<int> arr = {0, 1, 0, 1, 1, 0, 0, 1};

    cout << "Original array: ";
    for(int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    solution.segregate0and1(arr);

    cout << "Segregated array: ";
    for(int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}

