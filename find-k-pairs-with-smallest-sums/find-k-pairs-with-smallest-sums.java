class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        var pq = new PriorityQueue<List<Integer>>((a,b) -> (b.get(0)+b.get(1)) - (a.get(0)+a.get(1)));
        for(int i: nums1) {
            for (int j: nums2) {
                pq.add(List.of(i, j));
                if (pq.size() > k) 
                    pq.poll();
            }
        }
        var tempList = new ArrayList<List<Integer>>();
        while(pq.size() != 0) {
            tempList.add(pq.poll());
        }
        return tempList;
    }
    
    public void print(Object o) {
        System.out.println(o);
    }
}