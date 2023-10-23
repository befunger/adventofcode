#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& new_interval) {
        /*Given a list of non-overlapping intervals and a new interval return the new list of non-overlapping intervals
        after merging all necessary intervals with the new insertion. intervals are sorted on first index.*/

        
        /*Find index of insertion (O(log n))*/
        
        /*Iterate forward while next index start is within interval*/
        vector<vector<int>> merged_intervals;

        for(vector<int> interval : intervals){
            if(interval[1] < new_interval[0]){ // Interval fully before
                merged_intervals.push_back(interval);
            }
            else if(interval[0] > new_interval[1]){ // Interval fully after
                merged_intervals.push_back(new_interval);
                new_interval = interval;
            }
            else{ // Some overlap, merge intervals
                new_interval[0] = min(new_interval[0], interval[0]);
                new_interval[1] = max(new_interval[1], interval[1]);
                
            }
        }
        merged_intervals.push_back(new_interval);
        return merged_intervals;
    }
};