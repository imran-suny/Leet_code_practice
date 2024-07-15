Input: s1 = "ab", s2 = "eidbaooo"    Output: true
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1                           # s1= ac, s2 =acc  a:1, c:1,     a: 1 c: 2 --> match kom hobe 1 ta 
            elif s1Count[index] + 1 == s2Count[index]: # If count of character in s2 (after incrementing) exceeds count of character in s1 by exactly 1,
                                                       #it means this character's frequency was matching before incrementing, but now it doesn't match anymore, so matches is decremented by 1      
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)  # {'a': 1, 'b': 1}
        s2_map = Counter()    # {}

        if len(s1) > len(s2):
            return False

        for i in range(len(s2)):   # i = 0, s2[i] = 'e',// s2_map:  {'e': 1},  Window size is less than len(s1), no removal needed.
            s2_map[s2[i]] += 1     # i = 3, s2[i] = 'b'//  s2_map:  {'i': 1, 'd': 1, 'b': 1}  
            if i >= len(s1): 
                if s2_map[s2[i - len(s1)]] > 1:   // Remove s2[3-2] = 'i' from s2_map:
                    s2_map[s2[i - len(s1)]] -= 1                   
                else:
                    del s2_map[s2[i - len(s1)]]  // s2_map becomes {'d': 1, 'b': 1} 
            if s1_map == s2_map:
                return True 

        return False


