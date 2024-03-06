class Solution {
public:
    int minEatingSpeed(std::vector<int>& piles, int h) {
        cout.tie(0);
        cin.tie(0);
        ios_base::sync_with_stdio(0);
        int lo = 1, hi = *max_element(piles.begin(), piles.end());
        while (lo <= hi) {
            int k = (hi - lo) / 2 + lo;
            long kSum = 0;
            for (const auto& pile : piles) {
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
