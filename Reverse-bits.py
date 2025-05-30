https://leetcode.com/problems/reverse-bits/description/
32-bit 
Input: n = 00000010100101000001111010011100
Output:  = 00111001011110000010100101000000

class Solution:
    def reverseBits(self, n: int):
        res = 0
        for i in range(32):        01<<1=== shift all bits by 1,,,, 10
            bit = (n >> i) & 1        # right shift 32 ghor, then and 1 .... count whether 0/1.....00000000000000000000000000100
            res += (bit << (31 - i))  # left shift each bit to its postion                00100000000000000000000000000
        return res

