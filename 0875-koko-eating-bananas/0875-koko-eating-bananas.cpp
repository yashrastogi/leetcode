class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int min_bph = 1, max_bph = *max_element(piles.begin(), piles.end());
        int answer = 0;
        while (min_bph <= max_bph) {
            int mid = (max_bph + min_bph) / 2;
            int timeTaken = calculateTimeTaken(piles, mid);
            if (timeTaken <= h) {
                answer = mid;
                max_bph = mid - 1;
            } else {
                min_bph = mid + 1;
            }
        }
        return answer;
    }

    int calculateTimeTaken(vector<int>& piles, int bph) {
        int time = 0;
        for (int pile : piles) {
            time += ceil((double)pile / bph);
        }
        return time;
    }
};