class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        /* Returns the number of contiguous subarrays of nums which have a product less than k 
        
        O(n^2): Iterate start index, and for each expand end index until product is too large 
        
        Faster: We can abuse the fact that if a certain interval has a product < k, then every possible sub-interval does too.
        If extending a subarray [a b c] to [a b c d], 4 new possible subarrays are included ([d], [c d], [b c d], [a b c d])
        More generally, extending subarray to length n adds n new subarrays.
        */

       // O(n) solution utilizing that a large product < k implies all subintervals < k without explicitly checking
        int n = nums.size(); // Size of window included
        int start = 0;
        int end = 0;
        int product = nums[start]; // First product is first  element
        int valids = 0;
        while(end < n){
            if(product < k){
                valids += end - start + 1; // n new subarrays in extended array of length n
                end++;
                if(end < n){
                    product *= nums[end];
                }
            }
            else{
                product /= nums[start]; // Shrink window
                start++;
                if(end<start){// Make sure start does not surpass end (Only happens if a single array element >= k)
                    end = start;
                    product = nums[start];
                }
            }
        }
        return valids;

        //O(n^2) solution:    
        int n = nums.size(); 
        int valids = 0;   // Num of subarrays with product less than k
        int start = 0;
        int end = 0;
        int product = 1;

        while(start < n){
            product = product*nums[end]; // Update product
            if(product < k){ // If valid, increment and move end pointer
                valids++;
                end++;
                
            }
            if(product >= k || end >= n){ // If product too large or end pointer reached end, reset to next start position
                start++;
                end = start;
                product = 1;
            }
        }
        return valids;
    }
};