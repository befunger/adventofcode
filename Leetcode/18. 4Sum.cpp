# include <vector>
# include <iostream>
# include <algorithm>
# include <array>
# include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        /*
        Given an integer array nums, return all unique quadruplets that sum to target.
        Note that a quadruplet can contain duplicate numbers if there are duplicates in nums, but each quadruplet must be distinct.

        Approach: Similar to 3-sum, but with a nested loop + two pointers O(n^3)
        */

        // Setup: Sort array + initialise set
        int n = nums.size();
        sort(nums.begin(), nums.end());
        set<vector<int>> output_set;

        // 4 total values 0 < i < j < low < high < n
        for(int i = 0; i < n-3; i++){
            for(int j = i+1; j < n-2; j++){
                int low = j+1;
                int high = n-1;
                while(low < high){
                    long sum = (long)nums[i] + (long)nums[j] + (long)nums[low] + (long)nums[high];
                    if(sum == target){
                        output_set.insert({nums[i], nums[j], nums[low], nums[high]}); 
                        low++;
                        high--;
                    } else if(sum < target){
                        low++;
                    } else{
                        high--;
                    }
                }
            }
        }
        // Convert output set to vector
        vector<vector<int>> quads;
        for(auto quad: output_set){
            quads.push_back(quad);
        }
        return quads;
    }
};