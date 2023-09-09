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

#include <set>
#include <regex>

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

std::string grow(const std::string &polymer, std::map<std::string, char> &rules){
    std::string newPolymer;
    newPolymer.push_back(polymer[0]);
    for(int i = 1; i < polymer.length(); i++){
        try{
            std::string key = polymer.substr(i-1, 2);
            char val = rules.at(key);
            newPolymer.push_back(val);
        }
        catch(const std::out_of_range&){
            continue;
        }
        newPolymer.push_back(polymer[i]);
    }
    return newPolymer;
}

void diff(std::string &polymer){
    char maxChar, minChar, curr;
    int max = 0;
    int min = polymer.length();
    int amount;

    
    while(polymer.length()){
        curr = polymer[0];
        amount = std::count(polymer.begin(), polymer.end(), curr); // Counts occurences of curr
        polymer = std::regex_replace(polymer, std::regex(polymer.substr(0,1)), ""); // Removes occurences of curr
        if(amount > max){
            max = amount;
            //maxChar = curr;
        }
        if(amount < min){
            min = amount;
            //minChar = curr;
        }
        cout << curr << " had " << amount << " occurences." << endl;
    }
    cout << max - min;
}

int main(){
    std::string input;
    std::string polymer;
    std::map<std::string, char> rules;

    std::getline(cin, polymer); //Sets first line 
    std::getline(cin, input); //Flushes empty second line
    while(std::getline(cin, input)){ // Builds rulebook
        std::string key = input.substr(0,2);
        rules[key] = input[6];
        //cout << input << endl;
    }

    for(int i = 0; i < 20; i++){
        polymer = grow(polymer, rules);
        //cout << "Step " << i+1 << ": " << polymer << endl;
    }
    diff(polymer);
}