var findKthLargest = function(nums, k) {
    const heap = new MaxPriorityQueue();
    for (let i = 0; i < nums.length; i++) {
        heap.enqueue(nums[i]);
    }
    let ret = 0;
    for (let i = 0; i < k; i++) {
        ret = heap.dequeue();
    }
    return ret.element;
};