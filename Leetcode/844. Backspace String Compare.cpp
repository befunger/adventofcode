# include <iostream>
using namespace std;

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        /*Given two strings return true if they are equal after processing. 
        Processing consists of backspacing every time a # is hit in the string*/

        

        // Process strings sequentially, pop characters when hitting '#', compare end result
        string s_processed;
        for(char c : s){
            if(c == '#'){
                if(!s_processed.empty()){s_processed.pop_back();}
            }
            else{s_processed.push_back(c);}
        }

        string t_processed;
        for(char c : t){
            if(c == '#'){
                if(!t_processed.empty()){t_processed.pop_back();}
            }
            else{t_processed.push_back(c);}
        }
        return s_processed == t_processed;
    }
};