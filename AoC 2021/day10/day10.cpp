#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <array>
#include <iterator>
#include <cmath>
#include <queue>
#include <map>

#include <chrono>
#include <thread>


using std::cout, std::cin, std::endl;
//typedef std::map<char, char> mappy;


std::vector<int> stringTokenizer(std::string &toSplit, const char &splitter){ // Tokenizes a string of integers with delimiter splitter
    std::vector<int> output;
    std::istringstream stream(toSplit);
    std::string s;
    while(std::getline(stream, s, splitter)){
        if (!s.empty()){ // Avoids appending blanks in case of double delimiter 
            output.push_back(std::stoi(s));
        }
    }
    return output;
}

//Runs through a string of blocks recursively to find any mismatch in opened and closed
int getScore(std::string &input, std::map<char, char> &charMap, int n){

    //std::this_thread::sleep_until(std::chrono::system_clock::now() + std::chrono::seconds(1));

    //cout << input << " ";
    int len = input.length();
    //cout << "Len: " << len << " n: " << n << endl;


    if(len == 0 || (n+1 > len-1)){ // End of string, no syntax error (might be incomplete though)
        //cout << "REACHED THE END" << endl;
        return -1;
    }

    
    // We only get here if inp[n] and inp[n+1] are still valid
    int score = 0;
    //cout << "Looking at " << input[n] << " and " << input[n+1] << endl;


    while(charMap.count(input[n+1])){ // next is itself an opener, check next block first
        //cout << "next is open, go forward" << endl;
        score = getScore(input, charMap, n+1);
        if(score != 0){
            return score;
        }
    }

    //next is a closing bracket
    if(input[n+1] == charMap[input[n]]){ //next closes current opener, remove both and continue
        input.erase(n, 2);
        //cout << "removed a pair" << endl;
        return getScore(input, charMap, (n == 0 ? 0 : n-1)); // Continue with previous character as start (if possible)
    }
    else{ // next is an invalid move, calculate its score
        switch(input[n+1]){
            case ')':
                return 3;
            case ']':
                return 57;
            case '}':
                return 1197;
            case '>':
                return 25137;
            default:
                cout << "AAAAAAAAAH" << endl;
                return 0;
        }
    }
    
    cout << "Shouldnt be here" << endl;
    return 0;
}

int main(){
    std::string input;
    //std::vector<std::string> lines;
    int score = 0;
    std::map<char, char> charMap;
    charMap['('] = ')';
    charMap['['] = ']';
    charMap['{'] = '}';
    charMap['<'] = '>';
    while(std::getline(cin, input)){
        int val = getScore(input, charMap, 0);
        if(val != -1){
            score += val;
        }
        //cout << charMap[input[0]];
    }
    cout << "DONE! " << score;
}





