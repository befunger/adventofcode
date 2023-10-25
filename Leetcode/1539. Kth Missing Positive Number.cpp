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

    }
};