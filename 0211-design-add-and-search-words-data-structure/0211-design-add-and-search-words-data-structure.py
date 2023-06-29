class TreeNode:
    def __init__(self, val, is_word=False):
        self.val = val
        self.children = list()
        self.is_word = is_word

    # def __str__(self):
    #     return self._tree_to_string(self, "")

    # def _tree_to_string(self, node, indent):
    #     result = indent + str(node.val) + "\n"
    #     for child in node.children:
    #         result += self._tree_to_string(child, indent + "  ")
    #     return result


class WordDictionary:
    def __init__(self):
        self.root = TreeNode(-1)

    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            c = word[i]
            found = False
            for curr_node in node.children:
                if curr_node.val == c:
                    node = curr_node
                    found = True
                    break
            if not found:
                new_child = TreeNode(c)
                node.children.append(new_child)
                node = new_child
        node.is_word = True

    def search(self, word: str, node=None) -> bool:
        if not node:
            node = self.root
        for i in range(len(word)):
            c = word[i]

            if c == ".":
                for curr_node in node.children:
                    if self.search(word[i + 1 :], curr_node):
                        return True
                return False

            found = False
            for curr_node in node.children:
                if curr_node.val == c:
                    found = True
                    node = curr_node
                    break
            if not found:
                return False

        return node.is_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
