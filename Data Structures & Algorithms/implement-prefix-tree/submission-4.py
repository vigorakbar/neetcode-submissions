class TrieNode:
    def __init__(self):
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if not getattr(current, char, None):
                setattr(current, char, TrieNode())
            current = getattr(current, char)
        current.end = True

    def search(self, word: str) -> bool:
        i = 0
        current = self.root
        while i < len(word):
            current = getattr(current, word[i], None)
            if not current: return False
            i += 1
        return current.end

    def startsWith(self, prefix: str) -> bool:
        i = 0
        current = self.root
        while i < len(prefix):
            current = getattr(current, prefix[i], None)
            if not current: return False
            i += 1
        return True

# Time: O(n) n is length of the string
# Space: O(t) where t is total number of nodes