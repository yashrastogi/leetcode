function findKthLargest(nums, k) {
    let heap = new MaxPriorityQueue();
    for (let i = 0; i < nums.length; i++) {
        heap.enqueue(nums[i]);
    }
    let ret = 0;
    for (let _ = 0; _ < k; _++) {
        ret = heap.dequeue();
    }
    return ret.element;
};