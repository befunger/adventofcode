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

std::vector<int> updateFish(std::vector<int> fishVector){
    int max = fishVector.size();
    for(int i = 0; i < max; i++){
        if(fishVector[i] == 0){
            fishVector[i] = 6;
            fishVector.push_back(8);
        }
        else{
            fishVector[i]--;
        }
    }
    return fishVector;
}

int main(){
    std::string input;
    int days = 256;

    std::getline(cin, input);
    std::vector<int> fishVector = tokenizer(input, ',');
    for(int i = 0; i < days; i++){
        fishVector = updateFish(fishVector);
        /*cout << "After " << i+1 << " days: ";
        for(int fishval: fishVector){
            cout << fishval << ",";
        }
        cout << endl;*/
    }

    cout << fishVector.size();
}