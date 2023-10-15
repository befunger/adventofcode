class Solution {
public:
    void sortColors(vector<int>& nums) {
        /*
        Given an array nums with n objects 0, 1, and 2. Sort to [0, 0, 0, 1, 1, 2, 2, 2, 2]
        Sort the array in-place.

        Two-pass approach with constant space: 
        1. Scan list first and save three integers x,y,z denoting counts
        2. Iterate through list again and make first x 0, next y 1, and the last z 2.

        One-pass two-pointer approach:
        1. Keep two pointers at start and end.
        2. Iterate through list. Any 0 is swapped to start pointer, 2 moved to end pointer, and the relevant pointer is moved in one step
        */

        // One pass with three pointers 
        int start = 0;
        int mid = 0;
        int end = nums.size()-1;
        while(mid <= end){
            if(nums[mid] == 0){
                nums[mid] = nums[start];
                nums[start] = 0;
                start++;
            }
            else if(nums[mid] == 2){
                nums[mid] = nums[end];
                nums[end] = 2;
                end--;
                mid--;
            }
            mid++;
        }

        // Two pass counting and then replacing elements
        int zeroes = 0;
        int ones = 0;
        int n = nums.size();
        
        for(int i = 0; i < n; i++){ // Count number of zeroes/ones in array
            switch(nums[i]){
                case 0: zeroes++; break;
                case 1: ones++; break; 
            }
        }
        for(int i = 0; i<n; i++){ // Fill array in sorted order
            if(i < zeroes){ nums[i] = 0; }
            else if(i < zeroes + ones){ nums[i] = 1; }
            else { nums[i] = 2; }
        }
    }
};