#include <vector>
using namespace std;
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        /*Find the k:th missing positive number in a sorted strictly positive array*/
        /*For example, in the array [1, 3, 6, 7] the 3rd missing number is 5 (2 and 4 are the 1st and 2nd)*/

        // O(n) solution
        int target_value = 1;
        int target_index = 0;
        int n = arr.size();
        while(target_index < n){
            if(arr[target_index] != target_value){ // A missing value detected
                k--;
                if(k==0){ return target_value; } 
            }
            else{ target_index++; }
            target_value++;
        }

        return target_value + k-1; // If we don't hit k:th index in array, remaining k dictates how much further to iterate


        // Insight: Strictly increasing order means no duplicates
        // In a full array, index N would have the value N+1 (0-indexing)
        // If instead index N has some value P > N+1, we know that there are P-(N+1) numbers missing before it.
        // This should be usable in a O(log n) binary search to find the number that has k numbers missing before it.
        int low = 0;
        int high = arr.size() - 1;

        while(low <= high){ // Binary search for lowest index with k missing to its left
            int mid = low + (high - low)/2;

            if(arr[mid] - mid <= k){ low = mid + 1; } // arr[mid] - mid = number of missing on left
            else{ high = mid - 1; }
        }
        return low + k; // index 5 has 3 missing on left => 3rd missing is 5+3=8
    }
};