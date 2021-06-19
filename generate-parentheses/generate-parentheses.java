class Solution {
    public List<String> generateParenthesis(int n) {
        var ret = new ArrayList<String>();    
        _genPar("", ret, n, 0, 0);
        return ret;
    }
    
    private void _genPar(String curr, List<String> ret, int n, int numOpen, int numClose) {
        if(numOpen == numClose && numOpen == n)  {
            ret.add(curr.toString());
            return;
        }
        if(numOpen < n) {
            _genPar(curr + "(", ret, n, numOpen + 1, numClose);
        }
        if(numClose < numOpen) {
            _genPar(curr + ")", ret, n, numOpen, numClose + 1);
        }
    }
}