class Solution {
    let rootNode = Node(root: "-")
    
    func getWords(_ curr: Node) -> [[Character]] {
        var ret = [[Character]]()
        var q = [(curr, [Character]())]
        while !q.isEmpty {
            let (curr, wordArr) = q.removeFirst()
            if curr.wordEnd {
                ret.append(wordArr)
            }
            for c in curr.children.values {
                q.append((c, wordArr + [c.root]))
            }
        }
        return ret
    }

    func suggestedProducts(_ products: [String], _ searchWord: String) -> [[String]] {
        for p in products { insertTrie(p) }
        var ret = [[String]]()
        var curr = rootNode
        var prefix = [Character]()
        for (i, c) in Array(searchWord).enumerated() {
            var temp = [String]()
            prefix.append(c)
            if let found = curr.children[c] {
                curr = found
                for suffix in getWords(curr) {
                    let builtWord = String(prefix + suffix)
                    temp.append(builtWord)
                }
                temp.sort()
                temp = Array(temp[..<min(temp.count, 3)])
                ret.append(temp)
            } else {
                for j in i ..< searchWord.count {
                    ret.append([])
                }
                break
            }
        }
        return ret
    }
    
    func insertTrie(_ p: String) {
        var curr = rootNode
        for el in p {
            curr = curr.children[el] ?? {
                curr.children[el] = Node(root: el)
                return curr.children[el]!
            }()
        }
        curr.wordEnd = true
    }
}

class Node: CustomStringConvertible {
    var root: Character
    var children: [Character: Node] = [:]
    var wordEnd: Bool = false

    init(root: Character) {
        self.root = root
    }

    var description: String {
        return "[\(root): \(children)]"
    }
}
