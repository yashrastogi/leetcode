class Solution {
    int[] height;
    
    public int maxArea(int[] height) {
        this.height = height;
        int lo=0, hi=height.length-1;
        int area=0, maxArea=0;
        while (lo < hi) {
            area = calcArea(lo, hi);
            maxArea = Math.max(maxArea, area);
            if(height[lo] < height[hi]) {
                lo++;
            } else {
                hi--;
            }    
        }
        
        return maxArea;
    }
    
    private int calcArea(int lo, int hi) {
        return (hi - lo) * Math.min(height[hi], height[lo]);
    }
}