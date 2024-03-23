class Solution {
    func minFlips(_ a: Int, _ b: Int, _ c: Int) -> Int {
        var flips = 0
        var a = a, b = b, c = c
        
        while c > 0 || a > 0 || b > 0 {
            let bitA = a & 1
            let bitB = b & 1
            let bitC = c & 1
            
            if (bitA | bitB) != bitC {
                if bitC == 1 {
                    flips += 1
                } else {
                    flips += (bitA == 1 ? 1 : 0) + (bitB == 1 ? 1 : 0)
                }
            }
            
            a >>= 1
            b >>= 1
            c >>= 1
        }
        
        return flips
    }
}
