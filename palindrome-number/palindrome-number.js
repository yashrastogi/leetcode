/**
 * @param {number} x
 * @return {boolean}
 */

function isPalindrome(x) {
   let xStr = "" + x;
   let lo = 0, hi = xStr.length - 1;
   while(lo < hi) {
    if(xStr[lo++] == xStr[hi--]) {
    } else {
        return false;
    }
   }
    return true;
}