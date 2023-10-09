#include <vector>
#include <string>
#include <iostream>
#include <sstream>

using std::cout, std::cin, std::endl;

void spreadTheLove(std::vector<std::vector<int>> &octos, const int &x, const int &y){
    if(x>0){
        //cout << "(" << x-1 << "," << y << ")" << endl;
        octos[x-1][y]++;
        if(y>0){
            //cout << "(" << x-1 << "," << y-1 << ")" << endl;
            octos[x-1][y-1]++;
        }
        if(y < 9){
            
            //cout << "(" << x-1 << "," << y+1 << ")" << endl;
            octos[x-1][y+1]++;
        }
    }
    if(x<9){
        
        //cout << "(" << x+1 << "," << y << ")" << endl;
        octos[x+1][y]++;
        if(y > 0){
            //cout << "(" << x+1 << "," << y-1 << ")" << endl;
            octos[x+1][y-1]++;
        }
        if(y < 9){
            //cout << "(" << x+1 << "," << y+1 << ")" << endl;
            octos[x+1][y+1]++;
        }
    }
    if(y > 0){
        octos[x][y-1]++;
    }
    if(y < 9){
        octos[x][y+1]++;
    }
}

// Increases all energies by 1
void boostEnergies(std::vector<std::vector<int>> &octos){
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            //cout << "bo ";
            octos[i][j]++;
        }
    }
}

// Resets any negative energies up to 0
void resetEnergies(std::vector<std::vector<int>> &octos){
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            if(octos[i][j] < 0){
                //cout << "re ";
                octos[i][j] = 0;
            }
        }
    }
}

void updateOctos(std::vector<std::vector<int>> &octos, int &flashes){
    boostEnergies(octos);

    int i = 0;
    int j = 0;
    while(i < 10){
        //cout << "Checking index (" << i << ", " << j << ")" << endl; 
        if(octos[i][j] > 9){ // Flashes and sets position back to account for updated octos
            octos[i][j] = -9; // Ensures octo cant reach positive energy again from neighbours
            flashes++;
            //cout << "Boom found, retreating to index (" << i << ", " << j << endl;
            spreadTheLove(octos, i, j);
            if(i > 0){
                i--;
            }
            if(j > 0){
                j--;
            }
        }
        else{ // No explosion, move on to next index
            if(j < 9){
                j++;
            }
            else{
                j = 0;
                i++; // If we are on final position (i,j) = (9,9) it will update to (i,j) = (10,0) and quit the while loop
            }
        }
    }
    //cout << "Quit updating at (i,j) = " << i << " " << j << endl;

    resetEnergies(octos);
}

int main(){
    std::vector<std::vector<int>> octos;
    std::vector<int> temp; 
    std::string input;
    int flashes = 0;
    int steps = 1000;
    int oldNum;

    // Initialize octopus matrix
    while(std::getline(cin, input)){
        temp.clear();
        for(char i: input){
            temp.push_back(i - '0');
        }
        octos.push_back(temp);
    }

    // Simulates all the steps
    for(int i = 0; i < steps; i++){
        oldNum = flashes;
        updateOctos(octos, flashes);

        cout << i+1 << " steps have passed, " << flashes << " flashes have occured" << endl;
        if(flashes - oldNum == 100){
            cout << "ALL OCTOPUSES FLASHED DURING THIS STEP" << endl;
            steps = 0;
        }
        
    }
    //cout << "Flashes = " << flashes;


    

}