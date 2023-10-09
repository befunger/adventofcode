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

std::vector<long long int> updateFish(std::vector<long long int> fishVector){
    long long int zeroes = fishVector[0];
    for(int i = 1; i < 9; i++){
        fishVector[i-1] = fishVector[i];
    }
    fishVector[6] += zeroes; //Parents resetting
    fishVector[8] = zeroes; //New babies
    return fishVector;
}

int main(){
    std::string input;
    int days = 256;
    std::vector<long long int> amountByTimer(9, 0);
    std::getline(cin, input);
    std::vector<int> fishVector = tokenizer(input, ',');
    for(int time: fishVector){
        amountByTimer[time]++;
    }
    for(int i = 0; i < days; i++){
        amountByTimer = updateFish(amountByTimer);
    }
    long long int sum = 0;
    for(long long int val: amountByTimer){
        sum += val;
    }
    cout << sum;
}