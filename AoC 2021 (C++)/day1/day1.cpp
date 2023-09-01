#include <iostream>
#include <limits>
#include <string>
using std::cout, std::cin;

int main() {
    int oneago = -1;
    int twoago = -1; 
    int threeago = -1;
    std::string input;
    int counter = 0;
    while(std::getline (std::cin,input)){
        int current = std::stoi(input);
        if(threeago != -1){
            if(current > threeago){
                counter++;
            }
        }
        threeago = twoago;
        twoago = oneago;
        oneago = current;
    }
    cout << counter;

}