/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let l = nums.length;
    const reducer = (sum, val) => sum + val;
    let sum = nums.reduce(reducer);
    return ((l * (l+1)) / 2) - sum;
};