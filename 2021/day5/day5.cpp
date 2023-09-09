#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iterator>
#include <cmath>
#include <map>
#include <regex>

using std::cout, std::cin, std::endl;

std::vector<int> tokenizer(std::string toSplit, char splitter){ // Tokenizes a string of integers with delimiter splitter
    std::vector<int> output;
    std::istringstream stream(toSplit);
    std::string s;
    while(std::getline(stream, s, splitter)){
        if (!s.empty()){ // Avoids appending blanks in case of double delimiter (single digit values are preceded by two spaces)
            output.push_back(std::stoi(s));
        }
    }
    return output;
}

int main() {
    cout << "moink" << endl;
    std::string input;
    int x1, x2, y1, y2;
    std::map<std::pair<int, int>, int> mappo;

    while(std::getline(cin, input)){ //Checks there are more boards left, also clears the newline
        //cout << "Original input: " << input << endl;
        input = std::regex_replace(input, std::regex(" -> "), ","); 
        //cout << "Regexed: " << input << endl;
        std::vector<int> parsed = tokenizer(input, ',');
        int x1 = parsed[0];
        int y1 = parsed[1];
        int x2 = parsed[2];
        int y2 = parsed[3];
        //cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
        //*
        if(x1 == x2){
            if(y1 > y2){ // Make sure y1 is lower
                int temp = y1;
                y1 = y2;
                y2 = temp;
            }
            for(int j = y1; j <= y2; j++){ //Iterate over the y diff
                mappo[std::make_pair(x1, j)]++;
            }
        }
        else if (y1 == y2){ // Iterate over the x diff
            if(x1 > x2){
                int temp = x1;
                x1 = x2;
                x2 = temp;
            }
            for(int i = x1; i <= x2; i++){
                mappo[std::make_pair(i, y1)]++;
            }
        }
        else if(std::abs(x1-x2) == std::abs(y1-y2)){ //diagonal line
            mappo[std::make_pair(x1, y1)]++;
            //cout << x1 << ", " << y1 << "    " << x2 << ", " << y2 << endl;
            
            while(x1 != x2){
                x1 = (x1 < x2) ? x1+1 : x1-1;
                y1 = (y1 < y2) ? y1+1 : y1-1;
                mappo[std::make_pair(x1, y1)]++;
                //cout << x1 << ", " << y1 << "    " << x2 << ", " << y2 << endl;
            }
        }
    }
    cout << "freep" << endl;
    int counter = 0;
    for(const auto &myPair: mappo){
        if(myPair.second > 1){
            //cout << myPair.first.first << ", " << myPair.first.second << endl;
            counter++;
        }
    }
    cout << counter;
}

