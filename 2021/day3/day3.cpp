#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iterator>
#include <cmath>
using std::cout, std::cin, std::endl;

int bintodec(std::string bin){
    int decimal = 0;
    for(int i = 11; i > -1; i--){
        if(bin[i] == '1'){
            decimal += pow(2, (11-i));
        }
    }
    return decimal;
}

std::vector<int> getFrequencies(std::vector<std::string> list){
    std::vector<int> freq(12);
    for(std::string input: list){
        for(int i = 0; i < 12; i++){
            char current = input[i];
            if(current == '0'){
                freq[i]--;
            }
            else{
                freq[i]++;
            }
        }
    }
    return freq;
}
int getOxyOrCO2(std::vector<std::string>list, bool isOxy){
    for(int i = 0; i<12; i++){
        std::vector<int>freq = getFrequencies(list);
        if(list.size() == 1){
            return bintodec(list[0]);
        }
        char match = isOxy ? ((freq[i] >= 0) ? '0' : '1'): ((freq[i] >= 0) ? '1' : '0');
        std::vector<std::string>::iterator it;
        it = remove_if(list.begin(), list.end(), [match, i](auto a){return (a[i] == match);});
        list.erase(it, list.end());
    }
    return bintodec(list[0]);
}

int getCO2(std::vector<std::string>list, std::vector<int>freq){
    return 0;
}

int main() {
    std::string input;
    std::vector<std::string> list1(0);
    std::vector<std::string> list2(0);
    
    while(std::getline (std::cin,input)){
        list1.push_back(input);
        list2.push_back(input);
    }
    int oxy = getOxyOrCO2(list1, true);
    int co2 = getOxyOrCO2(list2, false);
    cout << oxy*co2;
}

