class Node: CustomStringConvertible {
    var root: Character
    var children: [Node] = []
    var wordEnd: Bool = false
 
    init(root: Character) {
        self.root = root
    }
    
    var description: String {
        return "[root: \(root), children: \(children)]"
    }
}

class Trie {
    var rootNode = Node(root: "-")
    
    func insert(_ word: String) {
        var curr = rootNode
        var word = Array(word)       
        var i = 0
        while i < word.count {
            var found = false
            for c in curr.children {
                if c.root == word[i] {
                    curr = c
                    found = true
                    break
                }
            }
            if !found {
                let newNode = Node(root: word[i])
                curr.children.append(newNode)
                curr = newNode
            }
            i += 1
        }
        curr.wordEnd = true
    }
    
    func search(_ word: String, full: Bool? = true)  -> Bool {
        var curr = rootNode
        var word = Array(word)
        var i = 0
        while i < word.count {
            var found = false
            for c in curr.children {
                if c.root == word[i] {
                    found = true
                    curr = c
                    break
                }
            }
            if !found {
                return false
            }
            i += 1
        }
        return full! ? curr.wordEnd : true
    }
    
    func startsWith(_ prefix: String) -> Bool {
        return search(prefix, full: false)
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie()
 * obj.insert(word)
 * let ret_2: Bool = obj.search(word)
 * let ret_3: Bool = obj.startsWith(prefix)
 */