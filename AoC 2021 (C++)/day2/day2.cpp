#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
using std::cout, std::cin;

int main() {
    std::string input;
    int x = 0;
    int y = 0;
    int aim = 0;
    std::string direction;
    std::string valString;
    while(std::getline (std::cin,input)){
        std::istringstream stream(input);
        stream >> direction;
        stream >> valString;
        int val = std::stoi(valString);
        if(direction == "forward"){
            x += val;
            y += val*aim;
        }
        else if (direction == "down")
        {
            aim += val;
        }
        else if (direction == "up")
        {
            aim-= val;
        }
    }
    cout << x*y;
}