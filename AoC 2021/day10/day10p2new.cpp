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
int getScore(std::string &input, std::map<char, char> &charMap, std::map<char, int> &scoreMap, int n){
    int score = 0;
    int len = input.length();
    //std::this_thread::sleep_until(std::chrono::system_clock::now() + std::chrono::seconds(1));

    //cout << input << " ";
    //cout << "Len: " << len << " n: " << n << endl;


    if(len == 0){ // An empty string gives score 0 since no fixing
        return 0;
    }
    if(n == len){ // n beyond the scope, go back
        return 0;
    }
    else if(n+1 == len){ // We are on the final index, if its an opener put the matching closer after and return score
        if(charMap.count(input[n])){ // if it's an opener remove it and return appropriate score
            score = scoreMap[input[n]];
            input.erase(n, 1); 
            cout << "removed" << endl;
            return score;
        }
        else{ //Contains a single closing bracket, broken syntax
            return -1;
        }
    }

    // We only get here if not on the final index (input[n+1] is still valid)

    while(charMap.count(input[n+1])){ // next is itself an opener, check next block first
        cout << "next is open, go forward (n=" << n << ")" << endl;
        int val = getScore(input, charMap, scoreMap, n+1);
        if(val == -1){ // Illegal thread, bail out
            return -1;
        }
        else if(val > 0){ //We 'fixed' an ending bracket
            score = score*5 + val;
            n--;
        }
        if(n == -1){ // String has one entry left which is an opener
            return score;
        }
    }

    //(input[n+1] is valid and a closing bracket
    if(input[n+1] == charMap[input[n]]){ //next closes current opener, remove both and continue
        input.erase(n, 2);
        n--;
        cout << "removed a pair" << endl;
    }
    else{ // next is an invalid move, purge this line of thought
        return -1;
    }
    
    cout << "Shouldnt be here" << endl;
    return -1000000;
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
    std::map<char, int> scoreMap;
    scoreMap['('] = 1;
    scoreMap['['] = 2;
    scoreMap['{'] = 3;
    scoreMap['<'] = 4;
    while(std::getline(cin, input)){
        int val = getScore(input, charMap, scoreMap, 0);
        cout << val;
        //cout << charMap[input[0]];
    }
    cout << "DONE! " << score;
}





