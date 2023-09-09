#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <array>
#include <iterator>
#include <cmath>

using std::cout, std::cin, std::endl;

std::vector<std::string> stringTokenizer(std::string toSplit, char splitter){ // Tokenizes a string of integers with delimiter splitter
    std::vector<std::string> output;
    std::istringstream stream(toSplit);
    std::string s;
    while(std::getline(stream, s, splitter)){
        if (!s.empty()){ // Avoids appending blanks in case of double delimiter 
            output.push_back(s);
        }
    }
    return output;
}

// Takes two 7-segment strings and returns the number of matching segments
int _matchingSegments(std::string first, std::string second){
    int matches = 0;
    for(char i: first){
        for(char j: second){
            if(i == j){
                matches++;
            }
        }
    }
    return matches;
}

//Takes patterns and outputs them sorted by which digit they represent
std::array<std::string, 10> _solvePatterns(std::vector<std::string> patterns){
    std::sort(patterns.begin(), patterns.end(), [](std::string a, std::string b) {return a.length() < b.length();}); //Sorts by size (small first)
    std::array<std::string, 10> solutions;
    int temp;
    solutions[1] = patterns[0];
    solutions[7] = patterns[1]; 
    solutions[4] = patterns[2];
    solutions[8] = patterns[9];

    //Finds remaining digits by comparing how many segments match the established numbers
    for(int i = 3; i < 9; i++){
        std::string s = patterns[i];
        temp = _matchingSegments(s, solutions[8]);
        if(temp == 6){  // One of the 6-bands (0, 6, 9)
            temp = _matchingSegments(s, solutions[1]); // (0,6,9) with 1: (2,1,2)
            if(temp == 1){
                solutions[6] = s;
            }
            else{
                temp = _matchingSegments(s, solutions[4]); // (0,9) with 4: (3,4)
                if(temp == 3){
                    solutions[0] = s;
                }
                else{
                    solutions[9] = s;
                }
            }
        }
        else{ // One of the 5-bands (2, 3, 5)
            temp = _matchingSegments(s, solutions[1]); // (2,3,5) with 1: (1,2,1)
            if(temp == 2){
                solutions[3] = s;
            }
            else{
                temp = _matchingSegments(s, solutions[4]); // (2,5) with 4: (2,3)
                if(temp == 2){
                    solutions[2] = s;
                }
                else{
                    solutions[5] = s;
                }
            }

        }
    }
    return solutions;
}

//Calculates output number using solution cheet from _solvePatterns
int decodeAndSum(std::vector<std::string> patterns, std::vector<std::string> outputs){
    std::array<std::string, 10> solutions = _solvePatterns(patterns);
    std::string currentDigit;
    std::string currentKey;
    int numerical = 0;
    for(int i = 0; i < 4; i++){
        currentDigit = outputs[i];
        std::sort(currentDigit.begin(), currentDigit.end()); //Sorts lexicographically 
        for(int j = 0; j < 10; j++){
            currentKey = solutions[j];
            std::sort(currentKey.begin(), currentKey.end());
            if(currentDigit == currentKey){
                numerical += std::pow(10, 3-i)*j;
            }
        }
    }
    return numerical;
}

int main(){
    std::string input;
    std::vector<std::string> semiparsed, patterns, outputs;
    int sum = 0;
    while(std::getline(cin, input)){
        semiparsed = stringTokenizer(input, '|');
        patterns = stringTokenizer(semiparsed[0], ' ');
        outputs = stringTokenizer(semiparsed[1], ' ');

        sum += decodeAndSum(patterns, outputs);
        
        /* PART 1 
        int uniques;
        for(std::string digit: outputs){
            if(digit.size() == 2 || digit.size() == 3 || digit.size() == 4 || digit.size() == 7){
                uniques++;
            }
        }
        cout << uniques;
        */
    }

    cout << sum;
}