class TrieNode:
  def __init__(self):
    self.children = [None] * 26
    self.isEndOfWord = False

class Trie:
  def _charNum(self, ch):
    """
    Returns 0-25 for a-z
    """
    return ord(ch) - ord('a')

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = TrieNode()


  def insert(self, word: str) -> None:
    """
    Inserts a word into the trie.
    """
    level = len(word)
    curr = self.root
    for i in range(level):
      charNum = self._charNum(word[i])
      if not curr.children[charNum]:
        curr.children[charNum] = TrieNode()
      curr = curr.children[charNum]
    curr.isEndOfWord = True

  def search(self, word: str) -> bool:
    """
    Returns if the word is in the trie.
    """
    level = len(word)
    curr = self.root
    for i in range(level):
      charNum = self._charNum(word[i])
      if not curr.children[charNum]:
        return False
      curr = curr.children[charNum]
    if curr.isEndOfWord:
      return True
    return False


  def startsWith(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    level = len(prefix)
    curr = self.root
    for i in range(level):
      charNum = self._charNum(prefix[i])
      if not curr.children[charNum]:
        return False
      curr = curr.children[charNum]
    return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)