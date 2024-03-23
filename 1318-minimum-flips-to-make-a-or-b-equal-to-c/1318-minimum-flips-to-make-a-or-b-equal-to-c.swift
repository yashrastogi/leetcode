class Solution {
    func minFlips(_ a: Int, _ b: Int, _ c: Int) -> Int {
        var a = a, b = b, c = c
        var flips = 0
        while a > 0 || b > 0 || c > 0 {
            let bitA = a & 1, bitB = b & 1, bitC = c & 1
            if bitA | bitB != bitC {
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