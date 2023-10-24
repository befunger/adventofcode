#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {

        /*Faster O(n) time, O(log n) space using Gauss Summation
        The sum of all numbers is O(n^2). Storing a number of size n^2 takes log(n^2) = O(log n) space*/
        int sum = 0;
        for(int num : nums){ sum += num; } // Sum up numbers

        int gauss_sum = nums.size()*(nums.size()+1)/2; // Gauss summation formula for 0+1+2+...+n

        return gauss_sum - sum; // Difference gives the missing number in sum


        /*O(n) time, O(n) space using array*/
        int n = nums.size();
        int found[10000] = {0};

        for(int num: nums){ found[num] = 1; } // Note all found numbers

        for(int index = 0; index < n+1; index++){ if(found[index] == 0) return index; } // Return index that wasn't found
        
        return 0;
    }
};