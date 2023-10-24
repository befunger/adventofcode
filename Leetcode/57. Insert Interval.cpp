#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& new_interval) {
        /*Given a list of non-overlapping intervals and a new interval return the new list of non-overlapping intervals
        after merging all necessary intervals with the new insertion. intervals are sorted on first index.*/

                

        /*In-place modification by finding index of insertion and combining proceeding elements*/
        vector<vector<int>>::iterator low = lower_bound(intervals.begin(), intervals.end(), new_interval,
            [](const vector<int>& a, const vector<int>& b){
                return a[1] < b[0];
        });

        if(low == intervals.end()){ // If no bound, interval starts higher than all current
            intervals.push_back(new_interval);
            return intervals;
        }

        
        // Iterate forward while next interval overlaps
        size_t index = low - intervals.begin();
        auto high = low;
        while(high != intervals.end() && intervals[index][0] <= new_interval[1]){
            new_interval[0] = min(intervals[index][0], new_interval[0]);
            new_interval[1] = max(intervals[index][1], new_interval[1]);
            index++;
            high++;
        }

        // Remove all merged interval and add new combined one
        intervals.erase(low, high);
        intervals.insert(low, new_interval);
        return intervals;
 

        /*O(n) solution iterating all intervals and building new array*/
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