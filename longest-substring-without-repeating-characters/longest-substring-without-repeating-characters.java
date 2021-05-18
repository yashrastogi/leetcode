class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        for (int i=0; i < s.length(); i++) {
            Set<Character> set = new HashSet<>();
            for(int j=i; j < s.length(); j++) {
                if(!set.contains(s.charAt(j))) {
                    maxLength = Math.max(maxLength, j-i+1);
                    set.add(s.charAt(j));
                } else {
                    break;
                }
            }
        }
        return maxLength;
    }
}