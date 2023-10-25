#include <vector>
#include <unordered_set>
using namespace std;
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        // O(n) time and space solution
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