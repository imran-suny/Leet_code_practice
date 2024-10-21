https://leetcode.com/problems/sum-of-two-integers/solutions/4927043/blind-75-beats-100-00-11-75/
Input: a = 2, b = 3
Output: 5

class Solution {             # In Java integers, are by default 32-bit signed two's complement integers
    public int getSum(int a, int b) {
        while (b != 0){
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        } 
        return a;
    }
}

python: bitShort is initialized to 0xffffffff, which is a 32-bit integer with all bits set to 1 except for the sign bit.
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a  if b > 0 else a
