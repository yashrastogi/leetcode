class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        return binarySearch(matrix, target, 0, (matrix.size() * matrix[0].size()) - 1);
    }

    std::vector<int> indexMapper(int i, std::vector<std::vector<int>>& matrix) {
        return {i / static_cast<int>(matrix[0].size()), i % static_cast<int>(matrix[0].size())};
    }

    bool binarySearch(std::vector<std::vector<int>>& matrix, int target, int lo, int hi) {
        if (lo > hi) {
            return false;
        }
        int mid = (hi - lo) / 2 + lo;
        auto ix = indexMapper(mid, matrix);
        if (matrix[ix[0]][ix[1]] == target) {
            return true;
        } else if (matrix[ix[0]][ix[1]] < target) {
            return binarySearch(matrix, target, mid + 1, hi);
        } else {
            return binarySearch(matrix, target, lo, mid - 1);
        }
    }
};
