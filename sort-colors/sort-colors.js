/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let i = 0;
    let numTwos = 0;
    while (i < nums.length) {
        if (nums[i] == 0) {
            nums.splice(i, 1);
            nums.unshift(0);
        }
        else if (nums[i] == 2) {
            nums.splice(i, 1);
            numTwos++;
            i--;
        }
        i++;
    }
    for (let i=0; i<numTwos; i++) {
        nums.push(2);
    }
};
