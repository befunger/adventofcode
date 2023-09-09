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
long long int getScore(std::string &input, std::map<char, char> &charMap, std::map<char, int> &scoreMap, int n){
    //cout << "n=" << n << endl;
    long long int score = 0;
    int len = input.length();

    if(len == 0){ // Empty string, no syntax error (might be incomplete though)
        return -1;
    }
    else if(n+1 > len-1){ //End of string, but still openers left prior, add corresponding closer
        //cout << "Adding a " << charMap[input[len-1]] << endl;
        input.push_back(charMap[input[len-1]]);
        //cout << input << endl;
        return score*5 + scoreMap[input[len-1]];   
    }

    while(charMap.count(input[n+1])){ // next is itself an opener, check next block first
        //cout << "WE ARE LOOPING BECAUSE input[n+1] IS " << input[n+1] << "!" << endl;
        long long int thisScore = getScore(input, charMap, scoreMap, n+1);
        if(thisScore > 0){
            score = score*5 + thisScore;
            //cout << "New score is " << score << endl;
        }
        else if(thisScore == 0){
            n--;
        }
        else if(thisScore == -1){
            return -1;
        }
        //cout << "Current score: " << score << endl;
        if(input.length() == 0){
            return score;
        }
        //cout << "back up at n=" << n << endl;
        if(n==-2){
            n = 0;
        }
    }

    //next is a closing bracket
    if(input[n+1] == charMap[input[n]]){ //next closes current opener, remove both and continue
        //cout << "Removing the pair " << input[n] << " " << input[n+1] << endl;
        input.erase(n, 2);
        //cout << input << endl;
        return 0; // Continue with previous character as start (if possible)
    }
    else{
        //cout << "n = " << n << endl;
        //cout << "illegal because " << input[n] << " was followed by " << input[n+1] << endl;
        return -1;
    }
    
    cout << "Shouldnt be here" << endl;
    return 0;
}

int main(){
    std::string input;
    std::vector<long long int> values;
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
        //cout << input << endl;
        long long int val = getScore(input, charMap, scoreMap, 0);
        cout << val << " ";
        if(val != -1){
            values.push_back(val);
        }
        //cout << charMap[input[0]];
    }
    std::sort(values.begin(), values.end());
    cout << endl << values.size() << endl;
    //cout << (values.size()-1)/2;
    int mid = (values.size() - 1)/2;
    cout << values[mid];
    //cout << "DONE! " << score;
}





