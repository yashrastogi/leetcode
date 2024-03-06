class Solution {
public:
    int minEatingSpeed(std::vector<int>& piles, int h) {
        int lo = 1;
        int hi = *std::max_element(piles.begin(), piles.end());
        while (lo <= hi) {
            int k = (hi - lo) / 2 + lo;
            int kSum = 0;
            for (int pile : piles) {
                kSum += std::ceil(static_cast<double>(pile) / k);
            }
            if (kSum <= h) {
                hi = k - 1;
            } else if (kSum > h) {
                lo = k + 1;
            }
        }
        return lo;
    }
};
