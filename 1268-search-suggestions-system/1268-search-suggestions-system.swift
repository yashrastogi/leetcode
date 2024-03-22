class Solution {
    var rootNode: Node
    
    init() {
        rootNode = Node(root: "-")
    }
    
    func suggestedProducts(_ products: [String], _ searchWord: String) -> [[String]] {
        for p in products {
            insertTrie(p)
        }
        var ret = [[String]]()
        var curr = rootNode
        var prefix = [Character]()
        for (i, char) in searchWord.enumerated() {
            prefix.append(char)
            var temp = [String]()
            if let child = curr.children[x(char)] {
                curr = child
                for suffix in getWords(curr) {
                    let builtWord = String(prefix + suffix)
                    temp.append(builtWord)
                }
            } else {
                var i = i
                while i < searchWord.count {
                    ret.append([])
                    i += 1
                }
                break
            }
            ret.append(temp)
        }
        return ret
    }
    
    func getWords(_ curr: Node) -> [[Character]] {
        func getWordsBacktrack(_ curr: Node, built: [Character]) {
            if ret.count >= 3 {
                return
            }
            if curr.wordEnd {
                ret.append(built)
            }
            for c in curr.children {
                if let c = c {
                    getWordsBacktrack(c, built: built + [c.root])
                }
            }
        }
        var ret = [[Character]]()
        getWordsBacktrack(curr, built: [])
        return ret
    }
    
    func insertTrie(_ p: String) {
        var curr = rootNode
        for c in p {
            let index = x(c)
            if curr.children[index] == nil {
                curr.children[index] = Node(root: c)
            }
            curr = curr.children[index]!
        }
        curr.wordEnd = true
    }
    
    func x(_ ch: Character) -> Int {
        return Int(ch.asciiValue!) - Int(Character("a").asciiValue!)
    }
}

class Node {
    var root: Character
    var children: [Node?]
    var wordEnd: Bool
    
    init(root: Character) {
        self.root = root
        self.children = Array(repeating: nil, count: 26)
        self.wordEnd = false
    }
}
