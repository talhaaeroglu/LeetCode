class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        double rev = 0, rem = 0;
        double y = x;
        while(x != 0){
            rem = x %10;
            rev = rev*10 + rem;
            x /= 10;
        }
        if(rev==y) return true;
        else return false;
    }
};