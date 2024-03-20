class Node: CustomStringConvertible {
    var root: Character
    var children: [Character: Node] = [:]
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
            if let found = curr.children[word[i]] {
                curr = found
            } else {
                let newNode = Node(root: word[i])
                curr.children[word[i]] = newNode
                curr = newNode
            }
            i += 1
        }
        curr.wordEnd = true
    }

    func search(_ word: String, full: Bool? = true) -> Bool {
        var curr = rootNode
        var word = Array(word)
        var i = 0
        while i < word.count {
            if let found = curr.children[word[i]] {
                curr = found
            } else {
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
