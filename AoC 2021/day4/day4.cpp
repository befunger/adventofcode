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
        if (!s.empty()){ // Avoids appending blanks in case of double delimiter (single digit values are preceded by two spaces)
            output.push_back(std::stoi(s));
        }
    }
    return output;
}
std::vector<std::vector<int>> buildBoard(){ // Uses next 5 rows of input to build new Bingo board
    std::string unparsed;
    std::vector<std::vector<int>> board;
    std::vector<int> row;
    for(int i = 0; i < 5; i++){
        std::getline(cin, unparsed);
        row.clear();
        row = tokenizer(unparsed, ' ');
        board.push_back(row);
    }
    return board;
}

bool updateAndCheckBoard(std::vector<std::vector<int>>* board, int num){
    std::vector<int> colSums((*board)[0].size());
    std::vector<int> rowSums((*board)[0].size());
    bool won = false;
    for(int i = 0; i < (*board).size(); i++){
        for(int j = 0; j < (*board)[0].size(); j++){
            (*board)[i][j] = ((*board)[i][j] == num) ? -1 : (*board)[i][j];
            rowSums[i] += (*board)[i][j];
            colSums[j] += (*board)[i][j];
        }
    }
    for(int i = 0; i < colSums.size(); i++){
        if(rowSums[i] == -5||colSums[i] == -5){
            won = true;
        }
    }
    return won; 
}

bool checkBoard(std::vector<std::vector<int>> board, int num){
    int rowSum;
    int colSum;
    return false;
}

int score(std::vector<std::vector<int>> board, int drawnNum){ // Calculates the score of a winning board
    int boardSum = 0;
    for(std::vector<int> row: board){
        for(int val: row){
            if(val != -1){
                boardSum += val;
            }
        }
    }
    return boardSum*drawnNum;
}

int main() {
    std::string input;
    std::vector<int> drawSeq;
    std::getline(cin, input);
    drawSeq = tokenizer(input, ',');
    std::vector<std::vector<std::vector<int>>> boardList;
    std::vector<std::vector<int>> board;

    while(std::getline(cin, input)){ //Checks there are more boards left, also clears the newline 
        board = buildBoard();
        boardList.push_back(board);
    }
    for(int num: drawSeq){
        cout << "Next number is " << num << endl;
        bool won;
        for(int i = 0; i < boardList.size(); i++){
            won = updateAndCheckBoard(&boardList[i], num);
            if(won){
                cout << "won with score " << score(boardList[i], num);
                return 0;
            }
        }
    }
}