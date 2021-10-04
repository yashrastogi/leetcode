class Solution {
   public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(),
             [](vector<int> a, vector<int> b) { return a[1] > b[1]; });
        int loadedUnits = 0;
        for (int j = 0; j < boxTypes.size(); j++) {
            while (boxTypes[j][0] > 0 && truckSize > 0) {
                truckSize -= 1;
                loadedUnits += boxTypes[j][1];
                boxTypes[j][0] -= 1;
            }
        }
        return loadedUnits;
    }
};