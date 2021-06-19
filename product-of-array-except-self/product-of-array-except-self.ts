let print = console.log;

function productExceptSelf(nums: number[]): number[] {
    let l = nums.length;
    let leftP = new Array(l), rightP = new Array(l);
    leftP[0] = 1, rightP[l - 1] = 1;
    
    for(let i = 1; i < l; i++) 
        leftP[i] = leftP[i - 1] * nums[i - 1];
    
    for(let i = l - 2; i >= 0; i--)
        rightP[i] = rightP[i + 1] * nums[i + 1];
    
    for(let i = 0; i < l; i++) 
        rightP[i] = leftP[i] * rightP[i];
    
    return rightP;
};