https://leetcode.com/problems/implement-trie-prefix-tree/description/
Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:  [null, null, true, false, true, null, true]

class TrieNode:
    def __init__(self):
        self.children = [None] * 26            # 26 none/ children 
        self.end = False                       ## mark every node if it is end of a word
class Trie:
    def __init__(self):
        self.root = TrieNode()                 # create a root node/ trienote 

    def insert(self, word: str) -> None:       ## if exist or not, na thakle create one 
        curr = self.root                       # initially start at the root --- set curr
        for c in word:                         # for evry single character 
            i = ord(c) - ord("a")              #
            if curr.children[i] == None:       # if not in hashmap 
                curr.children[i] = TrieNode()  # create a new empty trinote 
            curr = curr.children[i]            # if exist set curr to that child
        curr.end = True                        # after all char from a word, set the cur to True flag///   curr.rnd =True 

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:  # if a char not exist, return false 
                return False
            curr = curr.children[i]       #else finish the word
        return curr.end   # return true if end of word , if curr.end=True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]      ## finish the prefix and return true 
        return True
