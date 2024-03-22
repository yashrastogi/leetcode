class Solution:
    def suggestedProducts(self, products, searchWord):
        for p in products:
            self.insertTrie(p)
        ret = []
        curr = self.rootNode
        prefix = []
        for (i, char) in enumerate(searchWord):
            prefix.append(char)
            temp = []
            if curr.children[self.x(char)]:
                curr = curr.children[self.x(char)]
                for suffix in self.getWords(curr):
                    builtWord = "".join(prefix + suffix)
                    temp.append(builtWord)
            else:
                while i < len(searchWord):
                    ret.append([])
                    i += 1
                break
            ret.append(temp)

        return ret

    def __init__(self):
        self.rootNode = Node("-")

    def getWords(self, curr):
        def getWordsBacktrack(curr, built):
            if len(ret) >= 3:
                return
            if curr.wordEnd:
                ret.append(built)
            for c in curr.children:
                if c: getWordsBacktrack(c, built + [c.root])
        ret = []
        getWordsBacktrack(curr, [])
        return ret

    def insertTrie(self, p):
        curr = self.rootNode
        for c in p:
            if not curr.children[self.x(c)]:
                curr.children[self.x(c)] = Node(c)
            curr = curr.children[self.x(c)]
        curr.wordEnd = True
        
    def x(self, ch):
        return ord(ch) - ord('a')

class Node:
    def __init__(self, root):
        self.root = root
        self.children = [None] * 26
        self.wordEnd = False

    def __repr__(self):
        return f"[{self.root}: {[x for x in self.children if x is not None]}]"
