class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]

        node.is_word = True
            

    def search(self, word: str) -> bool:
        node = self._find(word)

        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self._find(prefix)

        return node is not None

    def _find(self, s: str) -> TrieNode:
        node = self.root

        for ch in s:
            if ch not in node.children:
                return None

            node = node.children[ch]

        return node
        