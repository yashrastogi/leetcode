class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        Arrays.sort(potions);
        int[] searchValues = new int[spells.length];
        for (int i = 0; i < spells.length; i++) {
            searchValues[i] = (int) Math.ceil((double) success / spells[i]);
        }
        int[] pairs = new int[spells.length];
        for (int i = 0; i < spells.length; i++) {
            int count = potions.length - binarySearch(potions, searchValues[i]);
            pairs[i] = count;
        }
        return pairs;
    }

    private int binarySearch(int[] array, int search) {
        int low = 0;
        int high = array.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (array[mid] < search) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }
}
