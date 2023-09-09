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

// Takes a set of dots and fold instruction and performs fold (removes overlapping dots)
std::set<std::tuple<int,int>> foldPaper(const char &dir, const int &foldAt, std::set<std::tuple<int,int>> &dots){
    std::tuple<int,int> tempTup;
    std::set<std::tuple<int,int>> newDots;
    int x, y;
    for(std::tuple<int,int> dot: dots){
        x = std::get<0>(dot);
        y = std::get<1>(dot);
        //cout << "Working on the dot (" << x << ", " << y << ")" << endl;
        //*
        if(dir == 'x'){
            if(x < foldAt){
                //cout << "x-fold this to (x,y) = (" << 2*foldAt-x << ", " << y << ")" << endl;
                //dots.erase(dot);
                newDots.insert(std::make_tuple(2*foldAt - x - foldAt - 1, y));
            }
            else if(x > foldAt){
                newDots.insert(std::make_tuple(x - foldAt - 1, y));
            }
            else{
                cout << "DOT ON FOLD LINE XXXXXXXXXXXXXX" << endl;
            }
        }
        else if(dir == 'y'){
            if(y > foldAt){
                //cout << "y-fold this to (x,y) = (" << x << ", " << 2*foldAt-y << ")" << endl;
                //dots.erase(dot);
                newDots.insert(std::make_tuple(x, 2*foldAt - y));
            }
            else if (y < foldAt){
                newDots.insert(dot);
            }
            else{
                cout << "DOT ON FOLD LINE YYYYYYYYYYYYYY" << endl;
            }
        }
    }
    return newDots;
}

int main(){
    std::string input;
    std::vector<int> parsed;
    std::tuple <int, int> xy;
    //xy = std::make_tuple(0, 0);
    std::set<std::tuple<int,int>> dots;
    char direction;
    int foldAt;
    int max_x = 10000000;
    int max_y = 10000000;
    // Parse input
    while(std::getline(cin, input)){
        if(!input.empty()){
            if(input[0] != 'f'){ // Do until fold instructions
                parsed = stringTokenizer(input, ',');
                xy = std::make_tuple(parsed[0], parsed[1]);
                dots.insert(xy);
            }
            else{
                direction = input[11];
                input.erase(0, 13);
                foldAt = std::stoi(input);

                if(direction == 'x'){
                    max_x = foldAt;
                }
                else if(direction == 'y'){
                    max_y = foldAt;
                }

                // Performs a fold and updates dots
                dots = foldPaper(direction, foldAt, dots);
                cout << dots.size() << " dots after fold." << endl; 

            }
        }
    }
    cout << "max_x: " << max_x << "\nmax_y: " << max_y << endl;
    for(int j = 0; j < max_y; j++){
        for(int i = 0; i < max_x; i++){
            if(dots.count(std::make_tuple(i, j))){
                cout << "#";
            }
            else{
                cout << " ";
            }
        }
        cout << endl;
    }

    
}