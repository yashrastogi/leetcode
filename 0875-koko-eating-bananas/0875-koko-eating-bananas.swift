class Solution {
    func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {
        var lo = 1
        var hi = piles.max()!
        while lo <= hi {
            let k = (hi + lo) / 2
            let kSum = piles.map { Int(ceil(Double($0) / Double(k))) }.reduce(0, +)
            if kSum <= h {
                hi = k - 1
            } else if kSum > h {
                lo = k + 1
            }
        }
        return lo
    }
}

func runCode() {
    var outputStream = OutputStream(url: URL(fileURLWithPath: "user.out"), append: false)!
    outputStream.open()

    while let pilesString = readLine(), let hString = readLine() {
        let piles = try! JSONDecoder().decode([Int].self, from: pilesString.data(using: .utf8)!)
        let h = try! JSONDecoder().decode(Int.self, from: hString.data(using: .utf8)!)
        let resultString = String(Solution().minEatingSpeed(piles, h))
        outputStream.write(resultString, maxLength: resultString.utf8.count)
        outputStream.write("\n", maxLength: 1)
    }

    outputStream.close()
    exit(EXIT_SUCCESS)
}

runCode()
