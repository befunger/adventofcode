#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int found[100000] = {0};
        for(int num: nums){ found[num] = 1; } // Mark all found numbers 

        vector<int> missing;
        for(int index = 1; index < nums.size()+1; index++){ 
            if(found[index] == 0) missing.push_back(index); // Append numbers not marked found
        }
        return missing;
    }
};