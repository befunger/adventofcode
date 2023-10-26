#include <vector>
#include <unordered_set>
using namespace std;
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {

        // O(n) time and O(1) space solution
        int i = 0;
        int n = nums.size();
        while(i < n){
            if(nums[i] > 0 && nums[i] <= n && nums[nums[i]-1] != nums[i]){  // Swap elements that are within the array size
                swap(nums[i], nums[nums[i]-1]); // Swap if number within [1, n] and target index isn't already correct
            }
            else{ i++; }
        }
        // Find first index that doesnt have matching value
        for(int i = 0; i < n; i++){
            if(nums[i] != i+1){
                return i+1;
            }
        }
        return n+1; // Only get here when the array contains [1, n], so return n+1

        /*O(n) time and space solution*/
        unordered_set<int> uniques;
        for(int num : nums){
            uniques.insert(num);
        }
        for(int i = 1; i<=nums.size(); i++){
            if(uniques.count(i)==0){ // Return first integer that is not in set
                return i;
            }
        }
        return nums.size()+1; // Only get here when the array contains [1, n], so return n+1
    }
};