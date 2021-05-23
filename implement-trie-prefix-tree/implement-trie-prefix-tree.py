class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEndOfWord = False
        
    def __str__(self):
        ret_str = ''
        ret_str += '[TrieNode (C): '
        for i, el in enumerate(self.children):
            if el != None:
                ret_str += str(i) + ' '
        ret_str += ']\n'
        return ret_str

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        length = len(word)
        node = self.root
        
        for i in range(length):
            curr = self._idx(word[i])
            if not node.children[curr]:
                node.children[curr] = TrieNode()
            node = node.children[curr]
            
        node.isEndOfWord = True
            
    def _idx(self, ch):
        return ord(ch) - ord('a')

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        length = len(word)
        node = self.root
        for i in range(length):
            curr = self._idx(word[i])
            node = node.children[curr]
            if not node: return False
        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        length = len(prefix)
        node = self.root
        for i in range(length):
            curr = self._idx(prefix[i])
            node = node.children[curr]
            if not node: return False
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)