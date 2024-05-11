https://leetcode.com/problems/word-ladder/description/
https://leetcode.com/problems/word-ladder/solutions/4742440/88-1-approach-1-o-n-m-2-python-c-step-by-step-explanation/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
nei = {'*ot': ['hot', 'dot', 'lot'],
       'h*t': ['hot'],
       'ho*': ['hot'],
                      '*ot': ['dot', 'lot'],
                      'd*t': ['dot', 'dog'],
                      'do*': ['dot', 'dog'],
       '*og': ['dog', 'log', 'cog'],
       'd*g': ['dog'],
       'do*': ['dog'],
                      'l*t': ['lot'],
                      'lo*': ['lot', 'log'],
        'l*g': ['log'],
       'lo*': ['log'],
      '*og': ['log', 'cog'],
                      'c*g': ['cog'],
                      'co*': ['cog']}

