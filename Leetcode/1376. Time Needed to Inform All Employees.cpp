#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        // O(n^2) solution iterating from each employee to head 
        int longestTime = 0;
        // Go through each employee
        for(int i = 0; i < n; i++){
            int timeToTell = 0;
            int id = i;
            // Iterate up until the head and add informTimes to get total time
            while(id != headID){
                id = manager[id];
                timeToTell += informTime[id];
            }
            // Save highest time
            longestTime = max(longestTime, timeToTell);
        }
        return longestTime;
    }
};