/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    function fixWindow(idx: number) {
        let sI = idx + 1;
        for (let i = idx + 1; i < n; i++)
            if (nums[i] <= nums[sI] && nums[i] > nums[idx])
                sI = i;
        const temp = nums[idx];
        nums[idx] = nums[sI];
        nums[sI] = temp;
        console.log(nums.slice(idx));
        for (let i = idx + 1, j = n - 1; i < j; i++, j--) {
            const temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }

    let n = nums.length;
    let maxEl = -Number.MAX_VALUE;
    for (let i = n - 1; i >= 0; i--) {
        if (nums[i] < maxEl) {
            fixWindow(i);
            break;
        }
        else if (i == 0) {
            nums.reverse();
        }
        maxEl = Math.max(maxEl, nums[i]);
    }
};