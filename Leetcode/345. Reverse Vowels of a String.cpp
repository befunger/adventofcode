class Solution {
public:
    string reverseVowels(string s) {
        // Front and back pointer. Run until they meet. When front hits vowel iterate back until it hits vowel and swap.
        int front = 0;
        int back = s.size() - 1;
        set<char> vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'};
        while(front < back){
            if(vowels.count(s[front])){
                if(vowels.count(s[back])){
                    swap(s[front], s[back]);
                    front++;
                    back--;
                }
                else{back--;}
            }
            else {front++;}
        }
        return s;
    }
};