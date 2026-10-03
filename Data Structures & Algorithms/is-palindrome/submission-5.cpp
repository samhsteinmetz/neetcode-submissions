class Solution {
public:

    bool isAlphaNum(char c)  {
        // TO DO
        return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') || ('0' <= c && c <= '9');
    }  

    bool isPalindrome(string s) {
        
        int left = 0;
        int right = s.length() - 1;

        while (right>left){
            while(right>left && !isAlphaNum(s[left])) left++;
            while(right>left && !isAlphaNum(s[right])) right--;
            if(tolower(s[left]) != tolower(s[right])){
                return false;
            }
            left++;
            right--;
        }
        return true;
        
        
        // int x = 5;
        // int *y = &x;

        // x = x << 2;
        // int* z;

        // std::cout << z;
        return false;
    }
};
