https://leetcode.com/problems/koko-eating-bananas/description/
Input: piles = [3,6,7,11], h = 8
Output: 4 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # 
        res = r  # maximum koto hour lagbe ?11 in this case 

        while l <= r:
            k = (l + r) // 2   # 1+11//2 = 6

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)  # piles r value vag korbo 
            if totalTime <= h:   # time kom mane k value beshi, hence right k komabo,, 
                res = k      # res update, 6 hobe initial 
                r = k - 1
            else:
                l = k + 1
        return res
