#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        /*Given two lists of intervals, return the list of overlapping intervals
        Both input intervals are disjoint and sorted*/

        /*Iterate through all in firstList, compare to intervals in secondList as long as they are not strictly bigger. 
        Once second interval exceeds, consider next from firstList.*/
        vector<vector<int>> union_intervals;
        int b = 0;
        for(int a = 0; a < firstList.size(); a++){ // Iterate a-intervals
            while(b < secondList.size() && secondList[b][0] <= firstList[a][1]){ // b-interval starts before a-interval ends.
                if(secondList[b][1] < firstList[a][0]){ // b-interval strictly smaller, move on to next
                    b++;
                }
                else{ // Some overlap exists. Add union to output
                    vector<int> overlap = {max(firstList[a][0], secondList[b][0]), min(firstList[a][1], secondList[b][1])};
                    union_intervals.push_back(overlap);
                    b++;
                }
            }
            if(b > 0) b--; // Decrement b once when a increments in case multiple a-lists overlap same b-list 
        }
        return union_intervals;
    }
};