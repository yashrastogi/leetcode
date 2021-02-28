class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) {
            return 0;
        }
        int grpLen = needle.length();
        for(int i=0; i<haystack.length(); i+=1) {
            String curr = "";
            if (i + grpLen <= haystack.length()) {
                for(int j=i; j<i+grpLen; j++) {
                    curr += haystack.charAt(j);
                }
            }
            if (curr.equals(needle)) {
                return i;
            }
        }
        return -1;
    }
}