https://leetcode.com/problems/word-search-ii/description/
https://leetcode.com/problems/word-search-ii/solutions/4702197/62-1-approach-1-o-m-n-4-k-python-c-step-by-step-explanation/

@ We start by constructing a Trie data structure and adding all the words from the list to the Trie.
         (root)
         / | \  \
        o  p  e  r
        |  |  |  |
        a  e  a  a
       /   |   \  \
      t    a    t  i
      |            \
      h             n
@DFS Search on the Board:
#We iterate through each cell of the board.
#At each cell, we perform a DFS search starting from that cell, considering each cell as a potential starting point for a word.
#During the DFS, we traverse in all four directions (up, down, left, right), checking if the sequence of characters forms a word in the Trie.
#If a word is found, we add it to the result set, mark it as not a word in the Trie, and remove it from the Trie to avoid duplicates.

#DFS starting at (0, 0): Path: "o" → "oa" → "oat" → "oath" (Found "oat" in Trie)  Result: {"oath"}
 DFS starting at (0, 1): 
            Path: "a" → "at" (Not in Trie) 
No word found and so on, exploring all possible paths. 
The final result set contains all the words found on the board that exist in the given list of words.
            
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):                    # inserts a word into the trie by traversing the trie from the root 
        cur = self
        cur.refs += 1                           # increments the refs counter for each node visited.
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):   # It is used to remove words from the trie when found on the board.
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()         # We initialize an empty trie and insert all words from the dictionary into it using the addWord method
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()       # visit=uniqque , res-- unique 

        def dfs(r, c, node, word):      # (r,c, root, word)
            if (
                r not in range(ROWS) 
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return
              
            visit.add((r, c))       # visit hole, remove korbo trie theke, since we got a new node, we need to update variables
            
            node = node.children[board[r][c]]  # current position in board 
            word += board[r][c]                # need to form a word using the board position 
            if node.isWord:                    # if node is end of work, we add the word in res
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
