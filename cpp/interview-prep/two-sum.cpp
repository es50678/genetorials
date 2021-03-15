#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> nums, int target) {
        return nums;
    }
};

int main() {
    Solution test = *new Solution();

    vector<int> input { 5, 4, 3, 2, 3, 4};

    vector<int> res = test.twoSum(input, 5);

    return 0;
}
