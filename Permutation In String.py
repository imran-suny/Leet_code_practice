Input: s1 = "ab", s2 = "eidbaooo"
Output: true

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26 
        for i in range(len(s1)):                   # in case same length and equal
            s1Count[ord(s1[i]) - ord("a")] += 1    # [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            s2Count[ord(s2[i]) - ord("a")] += 1    # [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0   # in case same length and equal

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")            # right pointer increase 
            s2Count[index] += 1                      # added a new char       
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:   # 1 add s2Count[index] += 1    howar pore count 1 ta beshi hole, reduce
                matches -= 1

            index = ord(s2[l]) - ord("a")            # left drcrease pointer increase/  
            s2Count[index] -= 1                      # remove the chracter
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
