#include <iostream>
#include <unordered_set>
using namespace std;
class Solution {
public:
    bool isHappy(int n) {
        /*Return true or false depending on if n is happy.
        A happy number is one which terminates in 1 when applying the following algorithm:
        Split the digits of the number, square them individually, and sum the result.*/

        /*Set approach. (If a number is reached a second time, it will loop)*/
        unordered_set<int> prev_numbers;
        int square_sum = 0;
        while(n != 1){
            square_sum = 0;
            while(n > 0){
                int digit = n%10; // Get least significant digit
                square_sum += digit*digit;
                n /= 10; // Remove least significant digit.
            }
            int size = prev_numbers.size();
            prev_numbers.insert(square_sum);
            if(size == prev_numbers.size()){
                return false;
            }
            n = square_sum;
        }
        
        return true;
    }
};