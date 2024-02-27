https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
Input:   ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
         [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output:   [null,null,null,null,false,true,true,true]
class TrieNode:
    def __init__(self):
        self.children = {}  # a hashmap
        self.word = False   # end of word=false 

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()                        # root as trienode 

    def addWord(self, word: str) -> None:             # same as before ///curr.end =true after a word 
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):  # '.a'
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":                             # c='.'
                    for child in cur.children.values():  # lets say current node has 26 (root >a,b,..z)children
                        if dfs(i + 1, child):            # for each child, it recusively search remaining part of the word and starting from the next character after the dot.... dfs (j= 1, root= child)>> a aslo, sp else condition 
                            return True                  # c ='..'  > dfs(1, child= .)-- 
                    return False
                else:
                    if c not in cur.children:           # same as before return curr.word ///end of the word as true 
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
