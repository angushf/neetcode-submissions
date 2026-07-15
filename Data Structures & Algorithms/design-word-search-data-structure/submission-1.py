class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        result = False
        
        def bt(start, node):
            nonlocal result
            if start == len(word):
                if node.is_word:
                    result = True
                return

            if word[start] == ".":
                for key, val in node.children.items():
                    bt(start + 1, val)
            elif word[start] in node.children:
                bt(start + 1, node.children[word[start]])
            else:
                return 

        bt(0, node)
        return result

          

            



            
        
