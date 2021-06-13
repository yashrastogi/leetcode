class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        var map = new HashMap<Integer, Integer>();
        var heap = new PriorityQueue<Integer>((a, b) -> map.get(a) - map.get(b));
        for(var num: nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for(var entry: map.entrySet()) {
            heap.add(entry.getKey());
            if(heap.size() > k) heap.poll();
        }
        var ret = new int[k];
        int i=0;
        while(heap.size() > 0) {
            ret[i++] = heap.poll();
        }
        return ret;
    }
}