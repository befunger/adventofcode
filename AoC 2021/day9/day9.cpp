#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <array>
#include <iterator>
#include <cmath>
#include <queue>

using std::cout, std::cin, std::endl;

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

int partOne(const std::vector<std::string> &depthMatrix, const int &rows, const int &cols){
    bool isLow;
    int riskSum = 0;
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            isLow = true;
            if(i > 0){
                if(depthMatrix[i][j] >= depthMatrix[i-1][j]){
                    isLow = false;
                }
            }
            if(j > 0){
                if(depthMatrix[i][j] >= depthMatrix[i][j-1]){
                    isLow = false;
                }
            }
            if(i < rows-1){
                if(depthMatrix[i][j] >= depthMatrix[i+1][j]){
                    isLow = false;
                }
            }
            if(j < cols-1){
                if(depthMatrix[i][j] >= depthMatrix[i][j+1]){
                    isLow = false;
                }
            }
            if(isLow){
                //cout << "Low point of " << depthMatrix[i][j] << " at (" << i << ", " << j << ")" << endl;
                //cout << riskSum << endl;
                riskSum += (depthMatrix[i][j] - '0') + 1;
            }
        }
    }
    return riskSum;
}

// Takes an initial position (x,y) and returns the size of its basin. Also replaces the basin points with 9 to avoid rediscovery.
int getSize(std::vector<std::string> &depth, const int &rows, const int &cols, const int &x, const int &y){
    std::queue<std::array<int, 2>> toCheck;
    int i, j;
    toCheck.push({x, y});
    depth[x][y] = '9';
    int size = 1;
    while(!toCheck.empty()){
        i = toCheck.front()[0];
        j = toCheck.front()[1];
        toCheck.pop();
        if(i > 0){
            if(depth[i-1][j] < '9'){
                toCheck.push({i-1, j});
                size++;
                depth[i-1][j] = '9';
            }
        }
        if(j > 0){
            if(depth[i][j-1] < '9'){
                toCheck.push({i, j-1});
                size++;
                depth[i][j-1] = '9';
            }
        }
        if(i < rows-1){
            if(depth[i+1][j] < '9'){
                toCheck.push({i+1, j});
                size++;
                depth[i+1][j] = '9';
            }
        }
        if(j < cols-1){
            if(depth[i][j+1] < '9'){
                toCheck.push({i, j+1});
                size++;
                depth[i][j+1] = '9';
            }
        }
    }
    return size;
}

//Iterates through the grid and calculates the size of each found basin
std::vector<int> getBasins(std::vector<std::string> &depth, const int &rows, const int &cols){
    std::vector<int> basinSizes;
    int size = 0;
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            if(depth[i][j] < '9'){
                basinSizes.push_back(getSize(depth, rows, cols, i, j));
            }
        }
    }
    return basinSizes;
}

int main(){
    std::string line;
    std::vector<std::string> depthMatrix;
    int rows;
    int cols;
    bool isLow;
    while(std::getline(cin, line)){
        depthMatrix.push_back(line);
        rows++;
    }
    cols = line.size();
    //cout << partOne(depthMatrix, rows, cols);

    std::vector<int> basinSizes = getBasins(depthMatrix, rows, cols);
    std::sort(basinSizes.begin(), basinSizes.end(), [](int a, int b){return a > b;}); //Sorts greatest first
    cout << basinSizes[0]*basinSizes[1]*basinSizes[2];
}