class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int lo = 1;
        int hi = Arrays.stream(piles).max().getAsInt();
        while (lo <= hi) {
            int k = (hi - lo) / 2 + lo;
            int kSum = 0;
            for (int pile : piles) {
                kSum += Math.ceil((double) pile / k);
            }
            if (kSum <= h) {
                hi = k - 1;
            } else if (kSum > h) {
                lo = k + 1;
            }
        }
        return lo;
    }
}
