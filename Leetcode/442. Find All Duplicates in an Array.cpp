#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        /*nums is an array of n numbers in range [1, n] where all numbers appear either once or twice.
        Return an array containing all the integers that appear twice
        Must be O(n) and use O(1) space*/

        // We can still abuse that nums are in range [1, n]. For each number i we can put it at index nums[i]
        // At the end find all elements that don't match their index
        int index = 0;
        int n = nums.size();
        while(index < n){ // Swap if (a) element in wrong place and (b) its rightful spot does not have right number
            if(nums[index] != index+1 && nums[index] != nums[nums[index]-1]){
                swap(nums[index], nums[nums[index]-1]);
            }
            else{ index++; }
        }

        vector<int> ans;
        for(int i = 0; i < n; i++){ // Return all numbers at the wrong index (they are duplicates since the correct index is occupied)
            if(nums[i] != i+1){
                ans.push_back(nums[i]);
            }
        }

        return ans;
    }
};