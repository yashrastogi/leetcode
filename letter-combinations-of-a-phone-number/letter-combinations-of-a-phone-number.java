class Solution {
    List<String> ret = new ArrayList<>();
    Map<Integer, String[]> map = new HashMap<Integer, String[]>();
    
    public List<String> letterCombinations(String digits) {
        if(digits.length() == 0) return ret;
        map.put(2, "abc".split(""));
        map.put(3, "def".split(""));
        map.put(4, "ghi".split(""));
        map.put(5, "jkl".split(""));
        map.put(6, "mno".split(""));
        map.put(7, "pqrs".split(""));
        map.put(8, "tuv".split(""));
        map.put(9, "wxyz".split(""));
        
        recursion(digits, 0, "");
        
        return ret;
    }
    
    public void recursion(String digits, int idx, String curr) {
        if (idx == digits.length()) {
            ret.add(curr);
            return;
        }
        int currDigit = Character.getNumericValue(digits.charAt(idx));  
        String[] characters = this.map.get(currDigit);
        for(String c: characters) {
            recursion(digits, idx+1, curr + c);
        }
        
    }
}