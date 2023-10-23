#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        /*Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals*/
        
        /*
        Merging [a, b], [c, d]: If a < c < b or a < d < b: Merge into [max(a, c), max(b, d)]
        
        Approach: Sort all intervals on start before merging, then go through and build one interval at a time.
        As soon as we hit an interval that doesn't merge into the current one, we know we will never have to revisit it and can move on to next.
        This allows us to finish in linear time by building one merged at a time (no need to check each merged interval for every iteration)
        */

        // Sort intervals on start index with lambda expression
        sort(intervals.begin(), intervals.end(), 
            [](const vector<int>& a, const vector<int>& b){
                return a[0] < b[0]; // Sort on first element (start_i), smallest last
        });

        // Iterate each input interval, build up merged intervals one at a time
        vector<vector<int>> merged_intervals;
        vector<int> current_interval = intervals[0]; // First element is simply set
        for(vector<int>& input_interval: intervals){
            if(input_interval[0] <= current_interval[1]){ // Interval overlaps
                current_interval[1] = max(current_interval[1], input_interval[1]); // Merge by extending end of interval
            } 
            else { // No overlap, push current interval to output and start new one for merging
                merged_intervals.push_back(current_interval);
                current_interval = input_interval;
            }
        }
        merged_intervals.push_back(current_interval); // Push final interval 
        return merged_intervals;
    }
};