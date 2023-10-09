#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iterator>
#include <cmath>

using std::cout, std::cin, std::endl;

std::vector<int> tokenizer(std::string toSplit, char splitter){ // Tokenizes a string of integers with delimiter splitter
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

int main(){
    std::string input;
    std::getline(cin, input);
    std::vector<int> positions = tokenizer(input, ',');
    std::vector<int> costs;
    std::vector<int> distPrice;
    int cost;
    int distance;

    //Get highest position
    int max = 0;
    for(int val: positions){
        if(val > max){
            max = val;
        }
    }
    // Calculate prices for different distances
    distPrice.push_back(0);
    for(int i = 1; i <= max; i++){
        distPrice.push_back(distPrice[i-1] + i);
    }
    // Calculate price to move to each position
    for(int i = 0; i <= max; i++){
        cost = 0;
        for(int j = 0; j < positions.size(); j++){
            distance = std::abs(i - positions[j]);
            cost += distPrice[distance];
        }
        costs.push_back(cost);
    }
    // Retreive minimum cost
    int min = cost;
    for(int val: costs){
        if(val < min){
            min = val;
        }
    }
    cout << min;
}