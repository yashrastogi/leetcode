class Solution {
    static int TRUE = 1, FALSE = 5, NOT_SET = 0;
        
    public String longestPalindrome(String s) {
        int[][] dp = new int[s.length()][s.length()];
        
        int lo = 0, hi = 0;
        
        // dp bases cases
        for (int i=0; i<s.length(); i++) {
            dp[i][i] = 1;   // single character is palindrome
        
            if (i<s.length()-1) {
                if (s.charAt(i) == s.charAt(i+1)) { // if char i = char i+1 then str i:i+1 is palindrome
                    dp[i][i+1] = TRUE;
                    if (1 > hi-lo) {
                        lo = i; hi = i+1;
                    }
                } else {
                    dp[i][i+1] = FALSE;
                }
            }
        }
        
        // str i:j is palindrome if str i+1:j-1 is palindrome and char i = char j
        for(int palindromeLength=2; palindromeLength < s.length(); palindromeLength++) {
            for(int i=0; i<s.length()-palindromeLength; i++) {
                if (dp[i+1][i+palindromeLength-1] == 1 && s.charAt(i) == s.charAt(i+palindromeLength)) {
                    dp[i][i+palindromeLength] = TRUE;
                    if (palindromeLength > hi-lo) {
                        lo = i; hi = i+palindromeLength;
                    }
                } else {
                    if (dp[i+1][i+palindromeLength-1] == NOT_SET) {
                     System.out.println("Not set");   
                    }                        
                    dp[i][i+palindromeLength] = FALSE;
                }
            }
        }
        
        
        
        return s.substring(lo, hi+1);
    }
    
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if(s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}