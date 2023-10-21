#include <vector>
#include <iostream>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool circularArrayLoop(vector<int>& nums) {
        /*
        Return true/false based on if a cycle exists.
        A cycle is a sequence of indices with same-sign values which cause a loop when traversing the array.
        We traverse by moving the number of indices indicated by the value at the current position.
        (If nums[i] = -3, we traverse 3 indices to the left.)
        */

        /* O(n) time, O(1) space by blacklisting entries in the array in-place*/
        int n = nums.size();
        int MAX_VAL = 1001;

        for(int i=0;i<nums.size();i++){
            int start = i;
            int id = MAX_VAL + i; // Unique identifier for indices visited this iteration
            int start_sign = nums[i] >= 0 ? 1 : -1;
            int curr = start;
            int curr_sign;
            int next;
            do{ 
                if(nums[curr] >= MAX_VAL) break; // Skip entries from previous iterations
                next = (curr+nums[curr])%n; // Traverse index by nums[i] steps
                if(next < 0) next += n; // Ensure positive modulo output
                if(next == curr) break; // Cancel if self-loop
                curr_sign = nums[curr] >= 0 ? 1 : -1;
                if(curr_sign != start_sign){ // Cancel if cycle switches sign
                    break;
                }
                nums[curr] = id; // Mark handled index
                curr = next;
                if(nums[curr] == id && curr_sign == start_sign){
                    return true;
                } 
            } while(nums[curr] != id);
        }
        return false; // No cycles found
    }
};